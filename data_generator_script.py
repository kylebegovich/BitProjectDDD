from random import random, seed

FIELDS = ["AIRPORT", "SEATS", "OCCUPIED", "COST"]
AIRPORTS = {"LAX", "ORD", "JFK", "YVR"} # Los Angeles, Chicago, New York, Vancouver

def format_line_item(airport, seats, occupied, cost):
    return "{},{},{},{}".format(airport, seats, occupied, cost)

def create_book(line_count, seed):
    seed(1)
    lines = []
    for port in AIRPORTS:
        occupied_avg = random() / 10 + 0.8  # between 80-90% avg occupied

        for i in range(line_count // len(AIRPORTS)):
            occupied_del = random() / 5 - 0.1  # shift of up to 10% from the average
            occupied_percent = occupied_avg + occupied_del
            lines.append(format_line_item(port, ))

    return lines
