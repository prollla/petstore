import pytest

from base_endpoint import BaseEndpoint

base_url = 'https://petstore.swagger.io/v2'


@pytest.fixture
def base_endpoint_fixture(request):
    return BaseEndpoint()


@pytest.fixture
def headers():
    return {
        'Content-Type': 'application/json'
    }
