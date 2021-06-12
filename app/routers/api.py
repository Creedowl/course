from fastapi import APIRouter

router = APIRouter()


@router.get("/", description="hello world")
async def index():
    return {"message": "Hello world"}
