import brownie
from brownie import accounts, ZERO_ADDRESS, chain
import time


def test_deploy_v1(my_token_v1):
    assert my_token_v1.name() == "MyToken"
    assert my_token_v1.balanceOf(accounts[0])

def test_deploy_v2(my_token_v2):
    assert my_token_v2.version() == "V2!"
    assert my_token_v2.name() == "MyToken"

def test_deploy_v3(my_token_v3):
    assert my_token_v3.version() == "V3!"