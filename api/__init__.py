from fastapi import FastAPI
from . import public_addresses

server = FastAPI()
server.include_router(public_addresses.router)

@server.get('/api')
def check():
    return {"status": 200}
