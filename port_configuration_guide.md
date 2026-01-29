# FastAPI Port Configuration Guide

This guide explains the different ways to change the port for your FastAPI application.

## Methods to Change FastAPI Port

### 1. Using Uvicorn Command Line (Most Common)

When running your FastAPI app with uvicorn, you can specify the port directly:

```bash
# Default port (8000)
uvicorn app.main:app

# Custom port (8080)
uvicorn app.main:app --port 8080

# Custom port with host
uvicorn app.main:app --host 0.0.0.0 --port 3000

# With reload for development
uvicorn app.main:app --reload --port 9000
```

### 2. Using Environment Variables

Add a PORT variable to your `.env` file:

```bash
# .env file
PORT=8080
```

Then run with:
```bash
uvicorn app.main:app --port $PORT
```

### 3. Programmatic Configuration (In Code)

You can also configure the port programmatically in your main.py:

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
```

**Important Note**: When using `reload=True`, you must pass the application as an import string:

```python
# ✅ Correct - using import string for reload
uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

# ❌ Incorrect - will show warning
uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
```

### 4. Using Configuration File

Create a configuration file and load it:

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 8000))  # Default to 8000 if not set
HOST = os.getenv("HOST", "127.0.0.1")
```

Then in your main.py:
```python
import uvicorn
from fastapi import FastAPI
from config import PORT, HOST

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
```

## Recommended Approach for Your Project

Based on your current setup, here's the recommended approach:

1. **For Development**: Use command line with custom port
2. **For Production**: Use environment variables
3. **For Flexibility**: Add port configuration to your existing config.py

## Common Port Numbers

- **8000**: Default FastAPI port
- **8080**: Common alternative (often used for development)
- **3000**: Popular for web applications
- **5000**: Another common alternative
- **9000**: Often used for APIs
- **80**: HTTP standard port (requires sudo)
- **443**: HTTPS standard port (requires sudo)

## Troubleshooting

### Port Already in Use
```bash
# Check which process is using a port
lsof -i :8000

# Kill process using port
kill -9 <PID>
```

### Permission Denied (Ports < 1024)
```bash
# Use sudo for ports below 1024
sudo uvicorn app.main:app --port 80
```

### Docker Port Mapping
```bash
# Map container port 8000 to host port 8080
docker run -p 8080:8000 your-fastapi-app