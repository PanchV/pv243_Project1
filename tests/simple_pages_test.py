"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">Page 1</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Page 2</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Page 3</a>' in response.data
    assert b'<a class="nav-link" href="/page4">Page 4</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/Docker")
    assert response.status_code == 200
    assert b"Docker Page" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/Python-Flask")
    assert response.status_code == 200
    assert b"Python Flask Page" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/CI-CD")
    assert response.status_code == 200
    assert b"CI-CD Page" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404