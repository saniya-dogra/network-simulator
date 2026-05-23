from physical_layer.device import Device


class EndDevice(Device):

    def __init__(self, name, mac):
        super().__init__(name)
        self.mac = mac

    def send_data(self, data):

        print(f"\n{self.name} sending data: {data}")

        for connection in self.connections:

            other_device = connection.get_other_device(self)

            if hasattr(other_device, "broadcast"):
                other_device.broadcast(self, data)

            else:
                other_device.receive_data(data)

    def receive_data(self, data):
        print(f"{self.name} received data: {data}")