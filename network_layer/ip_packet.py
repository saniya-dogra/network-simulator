class IPPacket:

    def __init__(self, source_ip, destination_ip, data):

        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.data = data

    def show_packet(self):

        print("\nIP PACKET")

        print("Source IP :", self.source_ip)

        print("Destination IP :", self.destination_ip)

        print("Data :", self.data)