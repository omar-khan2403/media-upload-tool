from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes import router as api_router

import db.models as models
from database import engine

models.Base.metadata.create_all(bind=engine)


def get_application():
    app = FastAPI(title="Map Upload Tool", version="1.0.0")

    app.add_middleware(
        CORSMiddleware, allow_origins = ["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")

    return app

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)