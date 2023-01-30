from AbstractPowerCalculator import AbstractPowerCalculator


class Level7(AbstractPowerCalculator):
    def __init__(self):
        super(Level7, self).__init__()
            
    A = 9.81061E-05
    B = -0.013467172
    C = 0.640037879
    D = 4.88546176
    E = -1.025974026


    # Data provided by Elite Support
    # This is a 4th order polynomial, where
    #  Power = A * v ^ 4 + B * v ^ 3 + C * v ^2 + D * v + E
    # where v is speed in miles/hour and constants A, B, C , D, & E are as defined above.
    
    def power_from_speed(self, revs_per_sec):
        if self._DEBUG: print("power_from_speed")

        kms_per_rev = self.wheel_circumference / 1000
        speed = revs_per_sec * 3600 * kms_per_rev
        power = self.correction_factor * (self.A * speed * speed * speed* speed +
                                          self.B * speed * speed * speed+
                                          self.C * speed * speed+
                                          self.D * speed+
                                          self.E)
        return power

    def set_wheel_circumference(self, circumference):
        self.wheel_circumference = circumference
