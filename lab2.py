from pickle import FALSE
import re

class Clock:
    def __init__(self, watch):
        self.watch = watch

    def show(self):
        self.watch.get_time(time)


class DigitalWatch:
    def get_time(self, time):
        print(time[0] + ":" + time[-1])

class AnalogWatch:
    def arrowHH(self, time, angle):
        hh = int(time[0])
        mm = int(time[-1])
        HH  = int(angle / 30)
        hh += HH
        if hh >= 24 :
            hh -= 24
        MM = int((angle % 30 * 12) / 30)
        mm += MM
        if mm >= 60 :
            mm -=60
        print(str(hh) + ":" + str(mm))
        time[0] = hh
        time[-1] = mm
        
    def arrowMM(self, time, angle):
        hh = int(time[0])
        mm = int(time[-1])
        MM = int((angle / 30) * 5)
        mm += MM
        if mm >= 60 :
            mm -=60
            hh += 1
        print(str(hh) + ":" + str(mm))
        time[0] = hh
        time[-1] = mm


class AdapterAnalogToDigital:
    def __init__(self):
        self._analogWatch_ = AnalogWatch()

    def get_time(self, time):
        if option == 1:
            self._analogWatch_.arrowHH(time, angle)
        if option == 2:
            self._analogWatch_.arrowMM(time, angle)


print("Enter time (format hh:mm): ")
_str = input()
match = re.fullmatch(r'[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}', _str)
while(match == None):
    print("Enter time (format hh:mm): ")
    _str = input()
    match = re.fullmatch(r'[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}', _str)
    time = _str.split(":")
time = _str.split(":")
dw = DigitalWatch()
dc = Clock(dw)
print("Digital Watch: ")
dc.show()
adapter = AdapterAnalogToDigital()
dc = Clock(adapter)
while(True):
    print("1 - HH \n"
      + "2 - MM")
    option = int(input())
    print("Enter angle: ")
    angle = int(input())
    if angle < 0 :
        print("Angle can't be negative!")
        exit()
    if option == 1:
        print("Analog Watch after arowHH: ")
        dc.show()
    if option == 2:
        print("Analog Watch after arowMM: ")
        dc.show()
