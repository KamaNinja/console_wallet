import pytest


@pytest.mark.parametrize('index, lst, expected_result', [('3', [1, 2, 3, 4], True),
                                                         ('0', [1], True),
                                                         ('0', [], False),
                                                         ('10', [1, 2, 3, 4], False),
                                                         ('hello', [1], False)])
def test_validate_index(wallet_interface, index, lst, expected_result):
    assert wallet_interface._validate_index(index, lst) == expected_result
