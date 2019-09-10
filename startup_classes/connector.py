from gpiozero.pins.pigpio import PiGPIOFactory


class PiConnect:

    def __init__(self, ip_add):
        self.ip_add = ip_add

    def factory_connector(self):
        """
        :return: returns the connection object for remote GPIO
        """
        return PiGPIOFactory(host=str(self.ip_add))
