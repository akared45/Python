from endpoints import app
import socket
import uvicorn

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) 
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "0.0.0.0" 

if __name__ == "__main__":
    host = get_local_ip()
    print(f"Starting server on http://{host}:8000")
    uvicorn.run(app, host=host, port=8000)