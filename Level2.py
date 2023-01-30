from AbstractPowerCalculator import AbstractPowerCalculator


class Level2(AbstractPowerCalculator):
    def __init__(self):
        super(Level2, self).__init__()
          
    A = 1.13636E-06
    B = -0.000441919
    C = 0.078977273
    D = 2.759992785
    E = -0.465367965

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
