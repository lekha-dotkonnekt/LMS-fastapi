from fastapi import APIRouter
from models.health_response import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok")
