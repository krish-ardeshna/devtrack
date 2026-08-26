from fastapi import Request
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from storage import Storage

def get_http_client(request: Request):
    return request.app.state.http_client

def get_storage():
    return Storage("../tasks.json")