import pytest
from brownie import MyToken, MyTokenV2, MyTokenV3

@pytest.fixture
def my_token_v1(accounts):
    my_token = MyToken.deploy({'from' : accounts[0]})
    my_token.initialize()
    return my_token

@pytest.fixture
def my_token_v2(accounts):
    my_token = MyTokenV2.deploy({'from' : accounts[0]})
    my_token.initialize()
    return my_token

@pytest.fixture
def my_token_v3(accounts):
    my_token = MyTokenV3.deploy({'from' : accounts[0]})
    my_token.initialize()
    return my_token