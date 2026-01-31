# LAN Chat (Python TCP)

A tiny TCP chat for **two machines in the same local network (LAN)**.

- **Windows** runs the **server**
- **Debian/Linux** runs the **client**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Networking](https://img.shields.io/badge/Networking-TCP-informational)

---

## Features
- TCP socket communication
- Server supports multiple clients (thread per connection)
- UTF-8 messages
- Zero dependencies (standard library only)

---

## Project Structure
```
lan-chat/
  server/server.py
  client/client.py
  common/config.py
```

---

## Requirements
- Python 3.x on both machines

No extra packages needed.

---

## Setup & Run

### 1) Clone repo
```bash
git clone https://github.com/mororpm/lan-chat
cd lan-chat
```

### 2) Start server on Windows
```powershell
python server/server.py
```

If Windows Firewall asks — allow access, or open TCP port **5000** inbound.

### 3) Set server IP on Debian client
Edit `client/client.py`:
```python
SERVER_IP = "192.168.1.10"  # put your Windows LAN IPv4 here
```

### 4) Run client on Debian/Linux
```bash
python3 client/client.py
```

Type messages on Debian; server replies on Windows.

To exit client: type `exit` or `quit`.

---

## Troubleshooting
### Get Windows IP
```powershell
ipconfig
```
Use **IPv4 Address**.

### Check server is listening
```powershell
netstat -ano | findstr :5000
```

### Test port from Debian
```bash
nc -vz <WINDOWS_IP> 5000
```
If `nc` is missing:
```bash
sudo apt-get update && sudo apt-get install -y netcat-openbsd
```

---

## Ideas to upgrade (for portfolio)
- Nicknames & commands (`/nick`, `/who`)
- Broadcast auto-discovery
- TLS/SSL encryption
- Message history logging
- Simple GUI (Tkinter) or Web UI

---

## License
MIT — do whatever you want with it.
