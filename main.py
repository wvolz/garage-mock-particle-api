from datetime import datetime, timezone
from typing import Union

from fastapi import FastAPI

app = FastAPI()

"""
Mock particle API for testing garage doorstate/move
- no validation of api keys/tokens

Sample API call: https://api.particle.io/v1/devices/deadbeef123/doorstate?access_token=123
"""


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/devices/{device_id}/doorstate")
def read_item(device_id: int, access_token: Union[str, None] = None):
    return {
        "name": "doorstate",
        "result": "down",
        "coreInfo": {
            "name": "testDeviceName",
            "deviceID": device_id,
            "connected": True,
            "last_handshake_at": datetime.now(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
        },
    }


@app.post("/v1/devices/{device_id}/door1move")
def read_item(device_id: int, access_token: Union[str, None] = None):
    return {
        "id": device_id,
        "name": "testDeviceName",
        "connected": True,
        "return_value": 1,
    }
