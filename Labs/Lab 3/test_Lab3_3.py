from Lab3_3 import validation, days_from_friday

def test_validation():
    assert(validation("M")==True)
    assert(validation("July")==False)

def test_days_from_friday():
    assert(days_from_friday("M")==4)

