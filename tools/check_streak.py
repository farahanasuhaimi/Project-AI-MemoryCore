import sys
sys.path.insert(0, r'D:\Kerja\Codes\Project-AI-MemoryCore\tools')
from secrets import HOSTINGER_HOST as HOST, HOSTINGER_PORT as PORT, HOSTINGER_USER as USER, HOSTINGER_PASSWORD as PASSWORD
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, port=PORT, username=USER, password=PASSWORD, timeout=30)

db = "u667484948_life"
db_user = "u667484948_life_admin"
db_pass = "dP43T8N>"

def run(label, cmd):
    print(f"\n--- {label} ---")
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read().decode('utf-8', errors='replace')
    if out: print(out)

run("user_stats", f"""mysql -u{db_user} -p'{db_pass}' {db} -e "SELECT * FROM user_stats;" 2>/dev/null""")

client.close()
