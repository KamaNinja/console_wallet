import pytest


@pytest.mark.parametrize('value, expected_result', [('2024-04-20', '2024-04-20'),
                                                    ('2024-4-2', '2024-04-02'),
                                                    ('2024-02-30', False),
                                                    ('1995-04-20', False),
                                                    ('2050-04-20', False)])
def test_validate_date(deal_interface, value, expected_result):
    assert deal_interface._validate_date(value) == expected_result


@pytest.mark.parametrize('value, expected_result', [('1', 'Доход'),
                                                    ('2', 'Расход'),
                                                    ('15', False),
                                                    ('0', False),
                                                    ('hello', False)])
def test_validate_category(deal_interface, value, expected_result):
    assert deal_interface._validate_category(value) == expected_result


@pytest.mark.parametrize('value, expected_result', [('1', 1.0),
                                                    ('1.1', 1.1),
                                                    ('0', False),
                                                    ('hello', False)])
def test_validate_amount(deal_interface, value, expected_result):
    assert deal_interface._validate_amount(value) == expected_result
