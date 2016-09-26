import json


def load_data(filepath):
    with open(filepath, 'r') as raw_content:
        data = json.load(raw_content)
    return data


def get_biggest_bar(data):
    return max(data, key=lambda bar: bar['Cells']['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda bar: bar['Cells']['SeatsCount'])


def get_distance(bar, longitude, latitude):
    current_location = bar['Cells']['geoData']['coordinates']
    current_longitude, current_latitude = current_location
    return ((current_longitude - longitude) ** 2 +
            (current_latitude - latitude) ** 2) ** 0.5


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda bar: get_distance(bar, longitude, latitude))


if __name__ == '__main__':
    data = load_data('bars.json')
    print("The biggest bar is: ", get_biggest_bar(data))
    print("The smallest bar is: ", get_smallest_bar(data))
    longitude = float(input('Enter longitude: '))
    latitude = float(input('Enter latitude: '))
    print("The closest bar is: ", get_closest_bar(data, longitude, latitude))
