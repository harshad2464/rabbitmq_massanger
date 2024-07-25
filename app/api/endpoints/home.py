from typing import Any
from fastapi import APIRouter

router = APIRouter()

@router.get("/home")
def read_api() -> Any:
    return {
        "Message": "Hello Welcome"
    }