from pathlib import Path
from fastapi import FastAPI, APIRouter,Request
from app.api.api import api_router

BASE_PATH = Path(__file__).resolve().parent
app = FastAPI(title="Test REST API.")

root_router = APIRouter()

app.include_router(api_router)
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    # Use this for debugging purposes only       
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
    # uvicorn.main()