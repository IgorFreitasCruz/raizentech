from typing import Callable

import httpx
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from db.repository import ForecastRepository
from schemas.forecast import ForecastResponse
from services.forecast_service import ForecastService

router = APIRouter(prefix="/forecast", tags=["forecast"])

# Dependency injections
def http_client() -> Callable:
    return httpx.AsyncClient()

@router.get("/", response_model=ForecastResponse)
async def get_forecast(
    http_client: httpx.AsyncClient = Depends(http_client),
):
    # Hard-coded values for demonstration purposes only; consider making them dynamic.
    lat, lon = -23.8002117, -45.5535105
    try:
        data = await ForecastService.fetch_forecast(http_client, lat, lon)
        ForecastRepository.save_forecast(data)
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail="Failed to retrieve data from the API")
    except httpx.RequestError:
        raise HTTPException(status_code=httpx.codes.SERVICE_UNAVAILABLE, detail="Connection error with the API")
    except Exception:
        raise HTTPException(status_code=httpx.codes.INTERNAL_SERVER_ERROR, detail="Error saving data to the database")

    del data['_id']
    return JSONResponse(content=data)
