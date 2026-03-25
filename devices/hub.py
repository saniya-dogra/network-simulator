class Hub:
    def __init__(self, name):
        self.name = name
        self.devices = []
        self.switch = None
                                               #Connect device to hub
    def connect(self, device):
        self.devices.append(device)
        device.hub = self

    def connect_uplink(self, switch):
        self.switch = switch
        switch.connect(self)

    def receive(self, packet, sender=None):
        print(f"{self.name} broadcasting {packet}")

        # Frame came from one local node; relay to switch uplink too.
        if sender is not None and self.switch is not None:
            self.switch.receive(packet, self)

        for device in self.devices:
            if device != sender:             #Hub sends data to ALL devices(broadcasting)
                device.receive(packet)                    