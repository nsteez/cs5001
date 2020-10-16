from Lab5_1 import average, median, lowest_score, highest_score

def test_1_even_number_of_scores():
    assert(average([80,20,40,89],4) == 57.25)
    assert(median([80,20,40,89],4) == 60.0)
    assert(lowest_score([80,20,40,89],4) == 20)
    assert(highest_score([80,20,40,89],4) == 89)


def test_2_odd_number_of_scores():
    assert(average([87, 89, 94, 95, 96],5) == 92.2)
    assert(median([87, 89, 94, 95, 96],5) == 94)
    assert(lowest_score([87, 89, 94, 95, 96],5) == 87)
    assert(highest_score([87, 89, 94, 95, 96],5) == 96)

def test_3_empty():
    assert(average([], 0)== "No values")
    assert(median([],0)== "No values")
    assert(lowest_score([],0)== "No values")
    assert(highest_score([],0)== "No values")





