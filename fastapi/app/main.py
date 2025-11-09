import os
import socket
import uvicorn
from fastapi import FastAPI

HOST = socket.gethostname()
APP_NAME = os.getenv("APP_NAME", "FastAPI")
ENV = os.getenv("ENV", "Dev")
VERSION = os.getenv("ENV", "0.0.1")

app = FastAPI(title="FastAPI App", version=VERSION)


@app.get("/")
async def home():
    return {
        "hostname": f"{HOST}",
        "app_name": f"{APP_NAME}",
        "env": f"{ENV}"
    }

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=80)
