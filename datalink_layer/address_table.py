class AddressTable:

    def __init__(self):
        self.table = {}

    def learn(self, mac, port):

        self.table[mac] = port

    def show_table(self):

        print("\nMAC Address Table")

        for mac, port in self.table.items():
            print(mac, "->", port)