from sizefinder import size_chart, results


def test_():
    assert(size_chart("K", 32.5) == "XL")
    assert(size_chart("W", 32.5) == "M")
    assert(size_chart("M", 32.5) == "not available")


def test_2():
    assert(size_chart("K", 78) == "not available")
    assert(size_chart("W", 78) == "not available")
    assert(size_chart("M", 78) == "not available")


def test_3():
    assert(size_chart("K", 53) == "not available")
    assert(size_chart("W", 53) == "not available")
    assert(size_chart("M", 53) == "XXXL")


def test_4():
    assert(results("L", "XL", "XXL") is True)
    assert(results("not available", "XL", "XXL") is True)
    assert(results("not available", "not available", "not available") is False)
