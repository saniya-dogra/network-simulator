class TCPSegment:

    def __init__(
        self,
        source_port,
        destination_port,
        sequence_number,
        data
    ):

        self.source_port = source_port
        self.destination_port = destination_port
        self.sequence_number = sequence_number
        self.data = data

    def show(self):

        print("\nTCP SEGMENT")

        print("Source Port :", self.source_port)

        print("Destination Port :", self.destination_port)

        print("Sequence Number :", self.sequence_number)

        print("Data :", self.data)