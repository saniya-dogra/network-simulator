from physical_layer.device import Device


class Hub(Device):

    def __init__(self, name):
        super().__init__(name)

    def broadcast(self, sender, data):

        print(f"\n{self.name} broadcasting data")

        for connection in self.connections:

            device = connection.get_other_device(self)

            if device != sender:
                device.receive_data(data)