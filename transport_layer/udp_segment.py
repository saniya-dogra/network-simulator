class UDPSegment:

    def __init__(
        self,
        source_port,
        destination_port,
        data
    ):

        self.source_port = source_port
        self.destination_port = destination_port
        self.data = data

    def show(self):

        print("\nUDP SEGMENT")

        print("Source Port :", self.source_port)

        print("Destination Port :", self.destination_port)

        print("Data :", self.data)