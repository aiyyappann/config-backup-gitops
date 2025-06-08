import os
from datetime import datetime
from netmiko import ConnectHandler
from dotenv import load_dotenv
import re

# Load credentials
load_dotenv()
username = os.getenv("SSH_USERNAME")
password = os.getenv("SSH_PASSWORD")

# Define device (update with real values)
device = {
    "device_type": "cisco_xr",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": username,
    "password": password,
    "port": 22,
}


# Create folder if it doesn't exist
os.makedirs("backups", exist_ok=True)

try:
    print(f"Connecting to {device['host']}...")
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show running-config")
    raw_prompt = net_connect.find_prompt()
    hostname = raw_prompt.replace("#", "").strip()
    hostname = re.sub(r"[^\w\-]", "_", hostname)  # Replace /, :, etc. with underscore
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"backups/{hostname}_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write(output)

    print(f"✅ Backup saved to {filename}")

except Exception as e:
    print(f"❌ Error: {e}")
