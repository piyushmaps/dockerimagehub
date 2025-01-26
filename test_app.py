from app import app

def test_home():
    response=app.test_client().get("/") #get the home page ,test_client is func in flask

    assert response.status_code==200
    assert response.data== "Hello world"