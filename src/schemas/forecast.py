from pydantic import BaseModel, Field


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Clouds(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Sys(BaseModel):
    pod: str


class ListItem(BaseModel):
    dt: int
    main: Main
    weather: list[Weather]
    clouds: Clouds
    wind: Wind
    visibility: int
    pop: float
    sys: Sys
    dt_txt: str


class Coord(BaseModel):
    lat: float
    lon: float


class City(BaseModel):
    id: int
    name: str
    coord: Coord
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


class ForecastResponse(BaseModel):
    cod: str
    message: int
    cnt: int
    list: list[ListItem] | None
    city: City

    class Config:
        json_schema_extra = {
            "example": {
                "cod": "200",
                "message": 0,
                "cnt": 40,
                "list": [
                    {
                        "dt": 1661871600,
                        "main": {
                            "temp": 296.76,
                            "feels_like": 296.98,
                            "temp_min": 296.76,
                            "temp_max": 297.87,
                            "pressure": 1015,
                            "sea_level": 1015,
                            "grnd_level": 933,
                            "humidity": 69,
                            "temp_kf": -1.11,
                        },
                        "weather": [
                            {
                                "id": 500,
                                "main": "Rain",
                                "description": "light rain",
                                "icon": "10d",
                            }
                        ],
                        "clouds": {"all": 100},
                        "wind": {"speed": 0.62, "deg": 349, "gust": 1.18},
                        "visibility": 10000,
                        "pop": 0.32,
                        "rain": {"3h": 0.26},
                        "sys": {"pod": "d"},
                        "dt_txt": "2022-08-30 15:00:00",
                    }
                ],
                "city": {
                    "id": 3163858,
                    "name": "Zocca",
                    "coord": {"lat": 44.34, "lon": 10.99},
                    "country": "IT",
                    "population": 4593,
                    "timezone": 7200,
                    "sunrise": 1661834187,
                    "sunset": 1661882248,
                },
            }
        }
