import json


def load_data(filepath):
    with open(filepath, 'r') as raw_content:
        data = json.load(raw_content)
    return data


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
    current_location = data[0]['Cells']['geoData']['coordinates']
    current_longitude, current_latitude = current_location
    min_distance = ((current_longitude - longitude) ** 2
                    + (current_latitude - latitude) ** 2) ** 0.5
    for bar in data:
        lon, lat = bar['Cells']['geoData']['coordinates']
        dist_to_bar = ((current_longitude - longitude) ** 2
                       + (current_latitude - latitude) ** 2) ** 0.5
        if dist_to_bar < min_distance:
            closest_bar = bar
    return closest_bar


if __name__ == '__main__':
    data = load_data('bars.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    longitude = float(input('Enter longitude: '))
    latitude = float(input('Enter latitude: '))
    print(get_closest_bar(data, longitude, latitude))
