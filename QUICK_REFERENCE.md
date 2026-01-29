# FastAPI Port Configuration - Quick Reference

## Quick Commands

### 1. Command Line (Most Common)
```bash
# Default port (8000)
uvicorn app.main:app

# Custom port
uvicorn app.main:app --port 8080

# With host and reload
uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
```

### 2. Using Your New Scripts
```bash
# Development mode (port 8080 with reload)
python run_app.py dev

# Production mode (using config.py)
python run_app.py prod

# Custom port
python run_app.py custom 9000
```

### 3. Environment Variables
```bash
# Set in .env file
PORT=8080

# Then run
uvicorn app.main:app --port $PORT
```

### 4. Programmatic (In main.py)
```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
```

**⚠️ Important**: When using `reload=True`, use import string:
```python
# ✅ Correct
uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

# ❌ Will show warning
uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
```

## Your Project Structure
```
apildap_test/
├── app/
│   ├── main.py          # Your FastAPI app
│   ├── config.py        # Updated with port config
│   ├── ldap_client.py   # LDAP functionality
│   └── schemas.py       # Pydantic models
├── run_app.py           # New startup script
├── test_ports.py        # Port testing script
├── port_configuration_guide.md  # Detailed guide
└── .env                 # Environment variables
```

## Common Use Cases

### Development
```bash
python run_app.py dev
# or
uvicorn app.main:app --reload --port 8080
```

### Production
```bash
python run_app.py prod
# or set PORT in .env and use:
uvicorn app.main:app --port $PORT
```

### Testing Different Ports
```bash
python test_ports.py
```

### Docker
```bash
docker run -p 8080:8000 your-fastapi-app
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

### Check Port Availability
```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    in_use = s.connect_ex(('127.0.0.1', 8000)) == 0
    print(f"Port 8000 in use: {in_use}")