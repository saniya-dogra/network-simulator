from datalink_layer.address_table import AddressTable


class Switch:

    def __init__(self, name):

        self.name = name
        self.mac_table = AddressTable()
        self.devices = []

    def connect_device(self, device):

        self.devices.append(device)

    def send_frame(self, sender, receiver_mac, data):

        print(f"\n{self.name} received frame")

        self.mac_table.learn(sender.mac, sender.name)

        found = False

        for device in self.devices:

            if device.mac == receiver_mac:

                print(f"Switch forwarding frame to {device.name}")

                device.receive_data(data)

                found = True

        if not found:

            print("Unknown destination MAC")
            print("Broadcasting frame")

            for device in self.devices:

                if device != sender:
                    device.receive_data(data)

    def show_mac_table(self):

        self.mac_table.show_table()