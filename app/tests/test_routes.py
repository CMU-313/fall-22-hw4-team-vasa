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
    # Testing for an unexpected behavior
    # Since the studytime is a str when it should be an int should be error
    url = '/predict?age=20&absences=1&studytime=lots'

    response = client.get(url)

    assert response.status_code == 500


def test_predict2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an unexpected behavior
    # Since the age is a str when it should be an int should be error
    url = '/predict?age=twenty&absences=6&studytime=2'

    response = client.get(url)

    assert response.status_code == 500


def test_predict3():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an unexpected behavior
    # Since the absences is a str when it should be an int should be error
    url = '/predict?age=20&absences=six&studytime=2'

    response = client.get(url)

    assert response.status_code == 500


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

    assert response.status_code == 500


def test_predict6():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The absences should not be negative
    url = '/predict?age=20&absences=-2&studytime=6'

    response = client.get(url)

    assert response.status_code == 500


def test_predict7():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The study time should not be negative
    url = '/predict?age=20&absences=2&studytime=-6'

    response = client.get(url)

    assert response.status_code == 500


def test_predict8():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The study time is more than absences so we should accept
    url = '/predict?age=20&absences=2&studytime=6'

    response = client.get(url)

    assert response.get_data() == b'Welcome user, you have been accepted!'

def test_predict9():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The study time is less than absences so we should reject
    url = '/predict?age=20&absences=10&studytime=6'

    response = client.get(url)

    assert response.get_data() == b'Welcome user, you have been rejected!'


def test_predict10():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The student is too young
    url = '/predict?age=13&absences=10&studytime=6'

    response = client.get(url)

    assert response.get_data() == b'Welcome user, you have been rejected because you are too young!'


def test_predict11():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    # Testing for an edge case
    # The student is too young
    url = '/predict?age=13&absences=6&studytime=10'

    response = client.get(url)

    assert response.get_data() == b'Welcome user, you have been rejected because you are too young!'


