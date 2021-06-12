import uvicorn
from fastapi import FastAPI

from app.routers import api
from app.utils.setting import config

app = FastAPI(title=config.name, version=config.version, debug=config.debug)


@app.get("/", description="hello world")
async def index():
    return {"message": f"Welcome to {config.name}"}


app.include_router(api.router, prefix="/api")

if __name__ == '__main__':
    print(config)
    uvicorn.run(app, host="0.0.0.0", port=8000)
