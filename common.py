import datetime
import urllib.request
import json


class Range:
    def __init__(self, time):
        self.startTime = time
        self.endTime = time
        self.count = 0

    def inc(self):
        self.count += 1

    def label(self):
        return self.startTime.strftime("%H:%M") + " - " + self.endTime.strftime("%H:%M")


class External:
    KEY_10KM = '10548 m'
    KEY_21KM = '21097 m'
    KEY_42KM = '42195 m'

    def __init__(self, step, number):
        self.ranges = []
        self.step = step
        self.step_number = number * self.step
        self.results = []

    def request(self, key):
        file = open('data/2014.json')
        x = file.read()
        data = json.loads(x)
        self.results = data['data'][key]['M']

    def calculate(self, hour, minute):
        base = datetime.datetime(1900, 1, 1, hour, minute)
        for i in range(0, self.step_number, self.step):
            r = Range(base + datetime.timedelta(minutes=i))
            self.ranges.append(r)

        for man in self.results:
            t = datetime.datetime.strptime(man[9], "%H:%M:%S.%f")
            for n in self.ranges:
                n.endTime = n.startTime + datetime.timedelta(minutes=self.step)
                if n.startTime < t < n.endTime:
                    n.inc()
                    break

    def print(self):
        for r in self.ranges:
            print(r.time)
            print(r.count)
