import datetime
import urllib.request
import json


class Range:
    def __init__(self, time):
        self.time = time
        self.count = 0

    def json_dump(self):
        return {
            'time': self.time,
            'count': self.count,
        }

    def inc(self):
        self.count += 1


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
        url = "http://my3.raceresult.com/RRPublish/data/list.php?callback=x&eventid=37962&key=2eb115d624f04b49c9d0146f183365a8&listname=2+Final+results%7CResult+List+MF&page=results&contest=0&r=all&l=0&_=1445038649760"
        response = urllib.request.urlopen(url)
        x = response.readall().decode('utf-8')
        x = x[2:-2]
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
                prev = n.time
                next = n.time + datetime.timedelta(minutes=self.step)
                if prev < t < next:
                    n.inc()
                    break

    def print(self):
        for r in self.ranges:
            print(r.time)
            print(r.count)
