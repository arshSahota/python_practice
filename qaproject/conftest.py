import pytest
from api.building_api import BuildingAPI


@pytest.fixture
def building_api():
    return BuildingAPI()