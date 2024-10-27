# middleware/error_handling.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from ..utils import create_response

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except HTTPException as exc:
            return JSONResponse(
                status_code=exc.status_code,
                content=create_response(
                    code=1,
                    status="error",
                    message=exc.detail,
                    data=None
                ),
            )
        except Exception as exc:
            return JSONResponse(
                status_code=500,
                content=create_response(
                    code=1,
                    status="error",
                    message="Internal Server Error",
                    data=None
                ),
            )