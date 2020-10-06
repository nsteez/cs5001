from expenses import get_actual_mileage_rate,\
    get_actual_trip_cost, get_reimbursement_amount, calculate_mileage


def test_():
    assert(calculate_mileage(0, 0) == 0)
    assert(calculate_mileage(10, 5) == 0)
    assert(calculate_mileage(1000, 1010) == 10)


def test_2():
    assert(get_reimbursement_amount(10) == 5.75)
    assert(get_reimbursement_amount(20) == 11.50)


def test_3():
    assert(get_actual_mileage_rate(0, 2.99) == 0.0)
    assert(get_actual_mileage_rate(30, 0) == 0.0)
    assert(get_actual_mileage_rate(24, 2.99) == 0.1246)


def test_4():
    assert(get_actual_trip_cost(1000, 1010, 0, 3.09) == 0.0)
    assert(get_actual_trip_cost(1000, 1010, 36, 0) == 0.0)
    assert(get_actual_trip_cost(1010, 1000, 36, 3.09) == 0.0)
    assert(get_actual_trip_cost(1000, 1010, 36, 3.09) == 0.86)
