import pytest

from view import DealInterface, WalletInterface


@pytest.fixture
def deal_interface():
    return DealInterface()


@pytest.fixture
def wallet_interface():
    return WalletInterface()