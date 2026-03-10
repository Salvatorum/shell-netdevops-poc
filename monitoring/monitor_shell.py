import requests
import time
from datetime import datetime

URL = "http://api.shell-local.com"

def check_status():
    try:
        response = requests.get(URL, timeout=3)
        status = "✅ ONLINE" if response.status_code == 200 else f"⚠️ STATUS {response.status_code}"
    except requests.exceptions.RequestException:
        status = "❌ OFFLINE (Error de conexión o Firewall bloqueando)"
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Monitoreando {URL} -> {status}")

if __name__ == "__main__":
    print("--- Shell Network Monitoring Tool ---")
    while True:
        check_status()
        time.sleep(10)
