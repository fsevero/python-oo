class Clock:
    def __init__(self, h=0, m=0, s=0, *args, **kwargs):
        super(Clock, self).__init__(*args, **kwargs)
        self.h, self.m, self.s = h, m, s

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.h, self.m, self.s)

    def adjust(self, h, m, s=0):
        self.h, self.m, self.s = h, m, s

    def tick(self):
        if self.s == 59:
            self.s = 0
        else:
            self.s += 1

        if self.s == 0 and self.m == 59:
            self.m = 0
        elif self.s == 0:
            self.m += 1

        if self.s == 0 and self.m == 0 and self.h == 23:
            self.h = 0
        elif self.s == 0 and self.m == 0:
            self.h += 1


# clock = Clock(10, 3, 59)
# print(clock)
# clock.tick()
# print(clock)

class Calendar:
    def __init__(self, day=1, month=1, year=2018, *args, **kwargs):
        super(Calendar, self).__init__(*args, **kwargs)
        self.day, self.month, self.year = day, month, year

    def adjust(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    def __str__(self):
        return "{0:02d}/{1:02d}/{2:4d}".format(self.day, self.month, self.year)

    def tick(self):
        if self.day == 30:
            self.day = 1
        else:
            self.day += 1

        if self.day == 1 and self.month == 12:
            self.month = 1
        elif self.day == 1:
            self.month += 1


        if self.day == 1 and self.month == 1:
            self.year += 1

# calendar = Calendar(30, 1, 2018)
# print(calendar)
# calendar.tick()
# print(calendar)

class ClockAndCalendar(Clock, Calendar):
    def __init__(self, h, m, s, day, month, year):
        super(ClockAndCalendar, self).__init__(h=h, m=m, s=s, day=day, month=month, year=year)

    def __str__(self):
        # return super(ClockAndCalendar, self).__str__()
        return Clock.__str__(self) + ', ' + Calendar.__str__(self)

    def tick(self):
        Clock.tick(self)

        if self.h == 0 and self.m == 0 and self.s == 0:
            Calendar.tick(self)

digital = ClockAndCalendar(23, 59, 58, 30, 12, 2017)
print(digital)
digital.tick()
print(digital)
digital.tick()
print(digital)