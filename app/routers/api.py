from fastapi import APIRouter

from app.routers.endpoints import user, auth

router = APIRouter()

router.include_router(user.router, prefix="/users")
router.include_router(auth.router, prefix="/auth")


@router.get("/", summary="hello world")
async def index():
    return {"message": "Hello world"}
