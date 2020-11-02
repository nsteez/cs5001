from lightrail import is_valid_station, get_direction, get_num_stops


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))


def test_is_valid_station2():
    assert(is_valid_station("Capitol Hill"))
    assert(is_valid_station("Westlake"))
    assert(is_valid_station("University Street"))
    assert(is_valid_station("Pioneer Square"))
    assert(is_valid_station("SODO"))
    assert(is_valid_station("Othello"))
    assert(is_valid_station("Rainier Beach"))
    assert(is_valid_station("Mount Baker"))
    assert(is_valid_station("Beacon Hill"))


def test_get_direction():
    assert(get_direction("University of Washington", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "University of Washington")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_direction2():
    assert(get_direction("Capitol Hill", "Angle Lake")
           == "Southbound")
    assert(get_direction("Westlake", "Angle Lake")
           == "Southbound")
    assert(get_direction("Columbia City", "Othello")
           == "Southbound")
    assert(get_direction("University Street", "SeaTac/Airport")
           == "Southbound")
    assert(get_direction("Angle Lake", "SeaTac/Airport")
           == "Northbound")
    assert(get_direction("SeaTac/Airport", "Beacon Hill")
           == "Northbound")
    assert(get_direction("Columbia City", "Mount Baker")
           == "Northbound")


def test_get_num_stops():
    assert(get_num_stops("University of Washington", "Angle Lake") == 15)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University Street", "Tacoma") == 0)


def test_get_num_stops2():
    assert(get_num_stops("University of Washington", "SeaTac/Airport") == 14)
    assert(get_num_stops("SeaTac/Airport", "University of Washington") == 14)
