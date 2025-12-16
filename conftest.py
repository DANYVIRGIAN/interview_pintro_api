import pytest
from utils.api_client import APIClient
from services.post_service import PostService

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture
def post_service(api_client):
    # Fixture ini langsung mengembalikan Object Service
    return PostService(api_client)