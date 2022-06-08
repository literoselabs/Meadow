import uvicorn
from fastapi import FastAPI
from . import public_addresses

server = FastAPI()
server.include_router(public_addresses.router)

@server.get('/api')
def check():
    return {"status": 200}

def start(bind_ip='0.0.0.0', port=8000):
    uvicorn.run(server, host=bind_ip, port=port)