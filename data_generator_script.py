from random import random, seed

FIELDS = ["AIRPORT", "SEATS", "OCCUPIED", "TIME"]
AIRPORTS = {"LAX", "ORD", "JFK", "YVR"} # Los Angeles, Chicago, New York, Vancouver
AIRPLANES = {"LAX": [200, 250, 450],
             "ORD": [250, 350, 450],
             "JFK": [250, 450],
             "YVR": [200, 250, 450]}
TIMES = {"WEEKDAY", "WEEKNIGHT", "WEEKEND"}

def format_line_item(airport, seats, occupied, time):
    return "{},{},{},{}".format(airport, seats, occupied, cost)

def add_information(airport, seats, occupied_percent, time):


    occupied = occupied_percent if port = "YVR" else seats * occupied_percent

    return airport, seats, occupied, cost

def create_book(line_count, seed):
    seed(1)
    lines = []
    for port in AIRPORTS:
        occupied_avg = random() / 10 + 0.8  # between 80-90% avg occupied
        seat_options = AIRPLANES[port]
        for i in range(line_count // len(AIRPORTS)):
            seats = seat_options[i % len(seat_options)]
            occupied_del = random() / 5 - 0.1  # shift of up to 10% from the average
            occupied_percent = occupied_avg + occupied_del
            occupied_seats = occupied_percent * seats

            data = add_information(airport, seats, occupied, cost)

            lines.append(format_line_item(data))

    return lines
