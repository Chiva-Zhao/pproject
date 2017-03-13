import csv
import pprint
from datetime import datetime


def convert():
    with open("buzzers.csv") as raw_data:
        # for line in csv.reader(raw_data):
        #     print(line)
        # for line in csv.DictReader(raw_data):
        #     print(line)
        raw_data.readline()  # Ignore the header info
        flight = {}
        for line in raw_data:
            # This code strips the line, then splits it, to produce the data in the format required
            k, v = line.strip().split(",")
            flight[k] = v
        pprint.pprint(flight)
        return flight


def convert1(flight: dict) -> dict:
    vset = set(flight.values())
    dest_time = {dest: [k for k, v in flight.items() if v == dest] for dest in vset}
    # for dest in vset:
    #     dest_time[dest] = [k for k, v in flight.items() if v == dest]
    pprint.pprint(dest_time)
    return dest_time


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


convert1(convert())
