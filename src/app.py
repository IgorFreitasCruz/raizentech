from fastapi import FastAPI

from api.routes import forecast_router


def create_app():
    app = FastAPI()

    app.include_router(forecast_router.router)

    return app


app = create_app()
