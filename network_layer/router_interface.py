class RouterInterface:

    def __init__(self, name, ip):

        self.name = name

        self.ip = ip

    def show(self):

        print(
            f"{self.name} -> {self.ip}"
        )