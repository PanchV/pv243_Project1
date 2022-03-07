"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/Git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/Docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/Python-Flask">Python-Flask</a>' in response.data
    assert b'<a class="nav-link" href="/CI-CD">CI-CD</a>' in response.data
    #assert b'<a class="nav-link" href="/page4">Page 4</a>' in response.data

def test_request_Home(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_Git(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_Docker(client):
    """This makes the index page"""
    response = client.get("/Docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_PythonFlask(client):
    """This makes the index page"""
    response = client.get("/Python-Flask")
    assert response.status_code == 200
    assert b"Python-Flask" in response.data

def test_request_CICD(client):
    """This makes the index page"""
    response = client.get("/CI-CD")
    assert response.status_code == 200
    assert b"CI-CD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404