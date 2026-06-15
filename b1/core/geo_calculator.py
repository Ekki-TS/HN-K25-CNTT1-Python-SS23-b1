import math

def calculate_distance(lat1,lon1,lat2,lon2):
    x = lat2 - lat1
    y = lon2 - lon1

    distance = (math.sqrt(x ** 2 + y ** 2)* 111)

    return distance