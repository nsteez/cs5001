from Lab3_1 import down_payment, saves_per_month

def test_down_payment():
    assert(down_payment(50000)== 12500)
    #assert(down_payment(10) == 40)

def test_saves_per_month():
   # assert(saves_per_month(1000)==3)
    assert(saves_per_month(75000, .2) == 1250)