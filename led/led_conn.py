from gpiozero import LEDBoard


class LED:

    def __init__(self, LEDs, factory):
        """leds must be a list"""
        self.LEDs = LEDs
        self.factory = factory

    def board(self):  # review this. left in this state purely for test (READ LEDS FROM CONFIG)
        return LEDBoard(*self.LEDs, pin_factory=self.factory)
