class ARPTable:

    def __init__(self):

        self.table = {}

    def add_entry(self, ip, mac):

        self.table[ip] = mac

    def get_mac(self, ip):

        return self.table.get(ip, "MAC NOT FOUND")

    def show_table(self):

        print("\nARP TABLE")

        for ip, mac in self.table.items():

            print(ip, "->", mac)