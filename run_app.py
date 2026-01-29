#!/usr/bin/env python3
"""
FastAPI Application Startup Script

This script demonstrates different ways to run your FastAPI application
with various port configurations.
"""

import uvicorn
from app.main import app
from app.config import HOST, PORT, DEBUG


def run_with_config():
    """Run the application using configuration from config.py"""
    print(f"Starting FastAPI server on {HOST}:{PORT}")
    print(f"Debug mode: {DEBUG}")
    if DEBUG:
        # Use import string for reload functionality
        uvicorn.run(
            "app.main:app",
            host=HOST,
            port=PORT,
            reload=True,
            log_level="info"
        )
    else:
        uvicorn.run(
            app,
            host=HOST,
            port=PORT,
            log_level="warning"
        )


def run_with_custom_port(port=8080, host="127.0.0.1", reload=False):
    """Run the application with a custom port"""
    print(f"Starting FastAPI server on {host}:{port}")
    if reload:
        # Use import string for reload functionality
        uvicorn.run(
            "app.main:app",
            host=host,
            port=port,
            reload=True,
            log_level="info"
        )
    else:
        uvicorn.run(
            app,
            host=host,
            port=port,
            log_level="info"
        )


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "dev":
            # Development mode with custom port and reload
            run_with_custom_port(port=8080, reload=True)
        elif command == "prod":
            # Production mode using config
            run_with_config()
        elif command == "custom":
            # Custom port from command line
            if len(sys.argv) > 2:
                custom_port = int(sys.argv[2])
                run_with_custom_port(port=custom_port, reload=True)
            else:
                print("Usage: python run_app.py custom <port>")
                print("Example: python run_app.py custom 9000")
        else:
            print("Usage: python run_app.py [dev|prod|custom]")
            print("  dev    - Run on port 8080 with reload enabled")
            print("  prod   - Run using config.py settings")
            print("  custom - Run on custom port (requires port number)")
    else:
        # Default: use configuration from config.py
        run_with_config()