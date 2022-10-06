import brownie
from brownie import accounts, ZERO_ADDRESS, chain
import time


def test_state_order_between_v2_and_v3(my_token_v2,my_token_v3):
    assert my_token_v2.fee() == 1
    assert my_token_v2.fee() == my_token_v3.fee()
    assert my_token_v3.tax() == "perpetual"

    