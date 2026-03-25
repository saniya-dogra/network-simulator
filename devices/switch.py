class Switch:
    def __init__(self, name):
        self.name = name
        self.mac_table = {}
        self.devices = []

    def connect(self, device):              #connect devices Like plugging cable into switch
        self.devices.append(device)
        if hasattr(device, "switch"):
            device.switch = self

    def _deliver(self, node, packet):
        try:
            node.receive(packet, None)
        except TypeError:
            node.receive(packet)

    def receive(self, packet, sender):
        print(f"\n{self.name} received {packet}")         #Switch gets data

        # MAC Learning
        self.mac_table[packet.src] = sender              #where sender is located
        print(f"Learning: {packet.src} -> {sender.name}")

        # Show MAC Table
        print("MAC Table:", {k: v.name for k, v in self.mac_table.items()})

        # Forwarding
        if packet.dest in self.mac_table:     #destination known : Sends ONLY to correct device
            print("Forwarding to specific device")
            target = self.mac_table[packet.dest]
            if target != sender:
                self._deliver(target, packet)
        else:
            print("Broadcasting (unknown MAC)")
            for d in self.devices:               #unknown destination : Sends to ALL devices
                if d != sender:
                    self._deliver(d, packet)