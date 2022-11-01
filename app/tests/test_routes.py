from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'Welcome user!'

def test_predict1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Since the studytime is a str when it should be an int should be error
    url = '/predict?age=20&absences=1&studytime=lots'

    response = client.get(url)

    assert response.status_code == 500


def test_predict2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Since the age is a str when it should be an int should be error
    url = '/predict?age=twenty&absences=6&studytime=0'

    response = client.get(url)

    assert response.status_code == 500


def test_predict3():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Since the absences is a str when it should be an int should be error
    url = '/predict?age=20&absences=six&studytime=0'

    response = client.get(url)

    assert response.status_code == 500
<<<<<<< Updated upstream
=======

def test_predict4():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an expected behavior/edge case
    # Most likely the age wont be 1 but it should still run
    url = '/predict?age=1&absences=2&studytime=6'

    response = client.get(url)

    assert response.status_code == 200


def test_predict5():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The age should not be negative
    url = '/predict?age=-20&absences=2&studytime=6'

    response = client.get(url)

    assert response.status_code == 400
>>>>>>> Stashed changes


