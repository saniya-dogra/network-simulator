class Bridge:

    def __init__(self, name):
        self.name = name

    def forward(self, data):

        print(f"\n{self.name} forwarding data: {data}")