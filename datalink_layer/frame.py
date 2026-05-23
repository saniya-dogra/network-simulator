class Frame:

    def __init__(self, source_mac, destination_mac, data):

        self.source_mac = source_mac
        self.destination_mac = destination_mac
        self.data = data

    def show_frame(self):

        print("\nFrame Details")
        print("Source MAC:", self.source_mac)
        print("Destination MAC:", self.destination_mac)
        print("Data:", self.data)