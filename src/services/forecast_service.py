import httpx

from core.config import settings
from core.logger import get_logger

logger = get_logger(__name__)

class ForecastService:
    BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

    @staticmethod
    async def fetch_forecast(http_client: httpx.AsyncClient, lat: float, lon: float) -> dict:
        url = f"{ForecastService.BASE_URL}?lat={lat}&lon={lon}&appid={settings.API_KEY}&cnt=1"
        try:
            response = await http_client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            logger.error(f"Error response {exc.response.status_code} while requesting {exc.request.url}.")
            raise
        except httpx.RequestError as exc:
            logger.error(f"An error occurred while requesting {exc.request.url}: {str(exc)}.")
            raise
