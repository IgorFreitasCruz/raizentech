import pytest
from httpx import (
    AsyncClient,
    MockTransport,
    Response,
)

from services.forecast_service import ForecastService


async def mock_fetch(request):
    return Response(200, json={"data": "some weather data"})


@pytest.mark.asyncio
async def test_fetch_forecast_success():
    transport = MockTransport(mock_fetch)

    async with AsyncClient(transport=transport) as client:
        weather_data = await ForecastService.fetch_forecast(client, 0, 0)
        assert weather_data == {"data": "some weather data"}
