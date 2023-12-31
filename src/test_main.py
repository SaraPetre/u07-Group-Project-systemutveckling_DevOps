from .main import collect_s, collect_f, collect_p
from unittest.mock import patch


def test_collect_s():

    """Testing collect_s with mocked result"""

    mock_response = [{'status': 'SUCCESSFUL'}]

    with patch('requests.get') as mock:
        mock.return_value.json.return_value = mock_response
        obj = collect_s()
        response = obj
        assert response == 1


def test_collect_f():

    """Testing collect_f with mocked result"""

    mock_response = [{'status': 'FAILED'}]

    with patch('requests.get') as mock:
        mock.return_value.json.return_value = mock_response
        obj = collect_f()
        response = obj
        assert response == 1


def test_collect_p():

    """Testing collect_p with mocked result"""

    mock_response = [{'id': 'ID'}]

    with patch('requests.get') as mock:
        mock.return_value.json.return_value = mock_response
        obj = collect_p()
        response = obj
        assert response == 1
