from fastapi.testclient import TestClient

from server import app

client = TestClient(app)


def test_read_main():
    response = client.post(
        "/predict",
         
        data={'file': open('2.png', 'rb')},

    )
    print(response.text)

test_read_main()