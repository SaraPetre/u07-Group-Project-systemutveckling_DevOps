from operator import indexOf
import requests
from requests.auth import HTTPBasicAuth
from .main import collect_s, collect_f, collect_p
from .main import start_http_server

# def test_status_code():
#     assert main == requests.status_codes(200)

print(collect_s())
print(collect_p())
print(collect_f())


def test_status_code_metrics():
    assert requests.get('http://localhost:8000/').status_code == 200

def test_status_code_onedev():
    assert requests.get('http://localhost:6610/').status_code == 200

def test_status_code_prometheus():
    assert requests.get('http://localhost:9090/').status_code == 200

def test_status_code_grafana():
    assert requests.get('http://localhost:3000/').status_code == 200


def test_get_metrics():
    res = requests.get('http://localhost:8000/')
    for data in res:
        assert data != ""
