from http import HTTPStatus


def test_get_forecast_success(client):
    response = client.get("/forecast")

    assert response.status_code == HTTPStatus.OK
    assert "list" in response.json()
