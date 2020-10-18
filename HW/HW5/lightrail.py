"""
Netti Welsh
Fall 2020 CS5001
Problem 3: Lightrail
"""

'''
YOUR FILE COMMENT HERE
'''
LINK_STATIONS = ("University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")

def is_valid_station(station):


    #station.title()
    if station in LINK_STATIONS:
        return True
    else:
        return False


def get_direction(start, end):
    '''Function -- get_direction
           Given start and end station names, determines if the direction is
           Northbound or Southbound.
       Parameters:
           start - The starting station name
           end - The ending station name.
    Returns:
          "Northbound" if the end station is north of the start station, or
          "Southbound" if the end station is south of the start station. If
          either station is invalid, or start and end stations are the same,
          return "No destination found".
    '''


    if start == end or start not in LINK_STATIONS or end not in LINK_STATIONS:
        return("No destination found")

    if LINK_STATIONS.index(start) < LINK_STATIONS.index(end):
        #print("Southbound")
        return("Southbound")

    elif LINK_STATIONS.index(start) > LINK_STATIONS.index(end):
        #print("Northbound")
        return ("Northbound")
    #else:
    #    return ("No destination found")

def get_num_stops(start, end):
    starting_stop = LINK_STATIONS.index(start)
    ending_stop = LINK_STATIONS.index(end)
    if starting_stop > ending_stop:
        print("yes northbound")
        return starting_stop - ending_stop
    elif ending_stop > starting_stop:
        print("yes Southbound")
        return ((ending_stop- starting_stop) + starting_stop)
    else:
        return 0
'''
    Function -- get_num_stops
        Calculates the number of stops from start to end.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        The number of stops from start to end. If either station is invalid
        or both stations are the same, return 0.
'''

def main():
    start =input("Enter start")
    end = input("Enter end")
    print(get_direction(start, end))
    print(get_num_stops(start, end))

if __name__ == "__main__":
    main()