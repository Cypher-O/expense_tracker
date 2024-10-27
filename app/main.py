# main.py
from fastapi import FastAPI
from .routers import router
from .database import init_db
from .middleware import ErrorHandlingMiddleware 

app = FastAPI(
    title="Expense Tracker API",
    description="An API for tracking expenses, allowing users to create, retrieve, update, and delete expense entries.",
    version="1.0.0",
)

app.add_middleware(ErrorHandlingMiddleware)

init_db()

app.include_router(router)

@app.get("/", summary="Root Endpoint", response_model=dict)
def read_root():
    """
    Root endpoint to check the API status.

    Returns a welcome message indicating the API is running.
    """
    return {
        "code": 0,
        "status": "success",
        "message": "Welcome to the Expense Tracker API"
    }