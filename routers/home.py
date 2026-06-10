from fastapi import APIRouter
from models.homeRsponse import HomeResponse
router = APIRouter()
router = APIRouter(prefix="", tags=["home"])
# For non-root routers (e.g. users): prefix="/users", tags=["users"]



@router.get("/", response_model=HomeResponse)
async def root() -> HomeResponse:
    return HomeResponse(message="Hello World")
