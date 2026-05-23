class Connection:

    def __init__(self, device1, device2):
        self.device1 = device1
        self.device2 = device2

    def get_other_device(self, current_device):

        if current_device == self.device1:
            return self.device2

        return self.device1