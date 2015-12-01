import datetime
import json
from trans import RomanianLanguagePack
from transliterate import translit, get_available_language_codes
from transliterate.base import registry


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

    def __init__(self):
        self.ranges = []
        self.results = []

    def request(self, key, gender):
        file = open('data/2014.json')
        x = file.read()
        data = json.loads(x)

        if gender == 'ALL':
            self.results += data['data'][key]['M']
            self.results += data['data'][key]['F']
        elif gender == 'M' or gender == 'F':
            self.results = data['data'][key][gender]

    def calculate(self, step, number, hour, minute):
        step = step
        step_number = number * step

        base = datetime.datetime(1900, 1, 1, hour, minute)
        for i in range(0, step_number, step):
            r = Range(base + datetime.timedelta(minutes=i))
            self.ranges.append(r)

        for man in self.results:
            t = datetime.datetime.strptime(man[9], "%H:%M:%S.%f")
            for n in self.ranges:
                n.endTime = n.startTime + datetime.timedelta(minutes=step)
                if n.startTime < t < n.endTime:
                    n.inc()
                    break

    def search(self, query):
        registry.register(RomanianLanguagePack)

        options = []
        print(get_available_language_codes())
        for elem in self.results:
            searchable = elem[0] + elem[3] + translit(elem[3], 'ro')
            if searchable.find(query) != -1:
                options.append(elem)

        return query, options

    def print(self):
        for r in self.ranges:
            print(r.time)
            print(r.count)
