"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/pyflask">Python/Flask</a>' in response.data


def test_request_cicd(client):
    """This tests the cicd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"Continuous Integration/Continuous Deployment" in response.data

def test_request_docker(client):
    """This tests the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_git(client):
    """This tests the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_pyflask(client):
    """This tests the pyflask page"""
    response = client.get("/pyflask")
    assert response.status_code == 200
    assert b"Python" in response.data

