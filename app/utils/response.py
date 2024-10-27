# utils/response.py
from typing import Any, List, Optional

def create_response(code: int, status: str, message: str, data: Optional[List[Any]] = None) -> dict:
    return {
        "code": code,
        "status": status,
        "message": message,
        "data": data
    }