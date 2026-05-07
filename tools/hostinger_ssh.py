"""
Hostinger SSH Agent — win-board deployment tool
Usage: python hostinger_ssh.py "command here"
       python hostinger_ssh.py  (drops into interactive mode)
"""

import paramiko
import sys
from secrets import HOSTINGER_HOST as HOST, HOSTINGER_PORT as PORT, HOSTINGER_USER as USER, HOSTINGER_PASSWORD as PASSWORD

BASE_DIR = "domains/drtakaful.com/public_html/life"


def run(commands: list[str]) -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, port=PORT, username=USER, password=PASSWORD, timeout=30)

    for cmd in commands:
        full_cmd = f"cd {BASE_DIR} && {cmd}"
        print(f"\n$ {cmd}")
        stdin, stdout, stderr = client.exec_command(full_cmd)
        out = stdout.read().decode()
        err = stderr.read().decode()
        if out:
            print(out, end="")
        if err:
            print("[stderr]", err, end="")

    client.close()


def interactive() -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(HOST, port=PORT, username=USER, password=PASSWORD, timeout=30)
    print(f"Connected to {HOST}:{PORT} — working dir: ~/{BASE_DIR}")
    print("Type 'exit' to quit.\n")

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
        out = stdout.read().decode()
        err = stderr.read().decode()
        if out:
            print(out, end="")
        if err:
            print("[stderr]", err, end="")

    client.close()
    print("Disconnected.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1:])
    else:
        interactive()
