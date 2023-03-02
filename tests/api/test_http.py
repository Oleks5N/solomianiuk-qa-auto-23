import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['login'] == 'defunkt'
    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_third_request():
    r = requests.get('https://api.github.com/versions')
    print(f"Response is {r.text}")

    assert r.status_code == 200


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/oleksandr_solomianiuk')

    assert r.status_code == 404
