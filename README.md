# 🔐 Cisco Config Backup + GitOps

This project automates Cisco device configuration backups over SSH, commits them to Git, and detects config changes.

## 🚀 Features

- SSH into Cisco IOS devices using Netmiko
- Save `running-config` with timestamps
- Auto-commit each backup to Git
- Show diff between latest configs
- Secure credential storage via `.env`

## 🧪 Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Configure `.env` with SSH credentials
3. Run: `python backup_config.py`
4. View diff: `python diff_configs.py`

## 📂 Backup Samples

Stored in `/backups` with filename format: `hostname_YYYYMMDD-HHMMSS.txt`
