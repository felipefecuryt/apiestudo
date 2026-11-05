from app import app


def test_home():
    client = app.test_client()
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.get_data(as_text=True) == "Olá, mundo!"
