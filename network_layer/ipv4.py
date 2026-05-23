class IPv4Address:

    def __init__(self, ip, subnet_mask):

        self.ip = ip
        self.subnet_mask = subnet_mask

    def show(self):

        print(f"IP Address : {self.ip}/{self.subnet_mask}")