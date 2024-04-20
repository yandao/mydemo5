from fastapi import APIRouter, Response, status

health_router = APIRouter()


@health_router.get(
    '/health',
    description='Endpoint to monitor service uptime.'
)
async def health() -> Response:
    return Response(status_code=status.HTTP_200_OK)
