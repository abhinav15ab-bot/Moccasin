# from src import favorites
from script.deploy import deploy_favorites
# import pytest

# @pytest.fixture(scope="session")

# def favorites_contract():
#     return deploy_favorites()

def test_starting_value(favorites_contract):
    # favorites_contract = deploy_favorites()

    assert favorites_contract.retrieve() == 77

def test_can_chnage_value(favorites_contract):
    #Arrange
    # favorites_contract = deploy_favorites()
    #Act
    favorites_contract.store(42)
    #Assert
    assert favorites_contract.retrieve() == 42

def test_can_add_people(favorites_contract):
    #Arrange
    new_person = "Becca"
    favorite_number = 16
    # favorites_contract = deploy_favorites()
    #Act
    favorites_contract.add_person(new_person, favorite_number)
    #Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)

    