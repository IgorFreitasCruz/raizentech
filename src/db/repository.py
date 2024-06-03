from core.logger import get_logger
from db.database import forecast_collection

logger = get_logger(__name__)


class ForecastRepository:
    @staticmethod
    def save_forecast(data: dict) -> None:
        try:
            forecast_collection.insert_one(data)
        except Exception as exc:
            logger.error(f"Error inserting document into database: {exc}")
            raise
