from gpiozero import LEDBoard


class LED:

    def __init__(self, leds, factory):
        """leds must be a list"""
        self.leds = leds
        self.factory = factory

    def pins(self):  # review this. left in this state purely for test (READ LEDS FROM CONFIG)
        return LEDBoard(5, 6, 13, 19, 26, pwm=True, pin_factory=self.factory)
