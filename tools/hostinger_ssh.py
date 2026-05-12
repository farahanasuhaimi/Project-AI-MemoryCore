"""
Hostinger SSH Agent — drtakaful.com deployment tool
Usage: python hostinger_ssh.py "command here"
       python hostinger_ssh.py  (drops into interactive mode)

Optional env var: SSH_BASE overrides BASE_DIR (e.g. SSH_BASE=../list python hostinger_ssh.py ...)
"""

import os
import paramiko
import sys
from secrets import HOSTINGER_HOST as HOST, HOSTINGER_PORT as PORT, HOSTINGER_USER as USER, HOSTINGER_PASSWORD as PASSWORD

BASE_DIR = os.environ.get("SSH_BASE", "domains/drtakaful.com/public_html/life")

# Reconfigure stdout to UTF-8 so Laravel's unicode progress chars don't crash
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def _safe_print(text: str) -> None:
    sys.stdout.write(text)
    sys.stdout.flush()


def run(commands: list[str]) -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, port=PORT, username=USER, password=PASSWORD, timeout=30)

    for cmd in commands:
        full_cmd = f"cd {BASE_DIR} && {cmd}"
        _safe_print(f"\n$ {cmd}\n")
        stdin, stdout, stderr = client.exec_command(full_cmd)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        if out:
            _safe_print(out)
        if err:
            _safe_print("[stderr] " + err)

    client.close()


def interactive() -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, port=PORT, username=USER, password=PASSWORD, timeout=30)
    _safe_print(f"Connected to {HOST}:{PORT} — working dir: {BASE_DIR}\n")
    _safe_print("Type 'exit' to quit.\n\n")

    while True:
        try:
            cmd = input("$ ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if cmd.lower() in ("exit", "quit"):
            break
        if not cmd:
            continue
        full_cmd = f"cd {BASE_DIR} && {cmd}"
        stdin, stdout, stderr = client.exec_command(full_cmd)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        if out:
            _safe_print(out)
        if err:
            _safe_print("[stderr] " + err)

    client.close()
    _safe_print("Disconnected.\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1:])
    else:
        interactive()
