#!/usr/bin/env python3
"""
Test script to verify different port configurations work correctly.
"""

import subprocess
import time
import requests
import signal
import os
from multiprocessing import Process


def test_port(port, timeout=5):
    """Test if a port is working by starting the server and making a request"""
    print(f"\n=== Testing port {port} ===")
    
    # Start the server in a separate process
    def run_server():
        os.system(f"python run_app.py custom {port}")
    
    server_process = Process(target=run_server)
    server_process.start()
    
    # Wait for server to start
    time.sleep(3)
    
    try:
        # Test the API
        response = requests.get(f"http://127.0.0.1:{port}/people/count", timeout=timeout)
        if response.status_code == 200:
            print(f"✅ Port {port} is working! Response: {response.json()}")
            return True
        else:
            print(f"❌ Port {port} returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print(f"❌ Port {port} is not accessible")
        return False
    except requests.exceptions.Timeout:
        print(f"❌ Port {port} timed out")
        return False
    except Exception as e:
        print(f"❌ Port {port} failed with error: {e}")
        return False
    finally:
        # Stop the server
        server_process.terminate()
        server_process.join(timeout=2)
        if server_process.is_alive():
            server_process.kill()
        time.sleep(1)


def check_port_availability(port):
    """Check if a port is already in use"""
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0


def main():
    """Test different port configurations"""
    print("FastAPI Port Configuration Test")
    print("=" * 40)
    
    # Test ports to check
    test_ports_list = [8000, 8080, 9000, 3000]
    
    for port in test_ports_list:
        if check_port_availability(port):
            print(f"⚠️  Port {port} is already in use, skipping test")
            continue
        
        test_port(port)
    
    print("\n" + "=" * 40)
    print("Port testing completed!")
    print("\nTo run your FastAPI app on different ports:")
    print("1. python run_app.py dev          # Port 8080 with reload")
    print("2. python run_app.py prod         # Using config.py settings")
    print("3. python run_app.py custom 9000  # Custom port 9000")
    print("4. uvicorn app.main:app --port 3000  # Direct uvicorn command")


if __name__ == "__main__":
    main()