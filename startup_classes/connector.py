from gpiozero.pins.pigpio import PiGPIOFactory


class PiConnect:

    def __init__(self, multi_ip=None):
        """ multi_ip: list"""
        self.multi_ip = multi_ip

    @staticmethod
    def single_factory_connector(ip):
        """
        :return: returns the connection object for remote GPIO
        """
        return PiGPIOFactory(host=str(ip))

    def multi_factory_connector(self):  # TODO: ADD MULTI IP SUPP
        pass
