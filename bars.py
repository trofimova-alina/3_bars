import json


def load_data(filepath):
    return json.load( open(filepath, 'r') )


def get_biggest_bar(data):
    max_seatscount = 0
    huge_bar = None
    for bar in data:
        seatscount = bar['Cells']['SeatsCount']
        if seatscount > max_seatscount: 
            max_seatscount = seatscount  
            huge_bar = bar
    return huge_bar


def get_smallest_bar(data):
    min_seatscount = data[0]['Cells']['SeatsCount']
    small_bar = None
    for bar in data:
        seatscount = bar['Cells']['SeatsCount']
        if seatscount < min_seatscount: 
            min_seatscount = seatscount  
            small_bar = bar
    return small_bar


def get_closest_bar(data, longitude, latitude):
    closest_bar = data[0]
    long, lat = data[0]['Cells']['geoData']['coordinates']  
    min_distance = ((long - longitude) ** 2 + (lat - latitude) ** 2) ** 0.5
    for bar in data:
        long, lat = bar['Cells']['geoData']['coordinates']  
        distance_to_bar = ((long - longitude) ** 2 + (lat - latitude) ** 2) ** 0.5
        if distance_to_bar < min_distance:
            closest_bar = bar
    return closest_bar        


if __name__ == '__main__':
    data = load_data('bars.json')
    print (get_biggest_bar(data))
    print (get_smallest_bar(data))
    longitude = float(input('Enter longitude: '))
    latitude = float(input('Enter latitude: '))
    print (get_closest_bar(data, longitude, latitude))
