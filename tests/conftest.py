import pytest
from brownie import MyToken, MyTokenV2

@pytest.fixture
def my_token_v1(accounts):
    return MyToken.deploy({'from' : accounts[0]})

@pytest.fixture
def my_token_v2(accounts):
    return MyTokenV2.deploy({'from' : accounts[0]})