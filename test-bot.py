from bot import app

def test_bot():
    response = app.test_client().get("/bot")

    assert response.status_code == 200
    assert response.data == b"Hello World"