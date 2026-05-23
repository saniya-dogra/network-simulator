class RoutingTable:

    def __init__(self):

        self.routes = []

    def add_route(self, network, mask, next_hop):

        self.routes.append((network, mask, next_hop))

    def show_routes(self):

        print("\nROUTING TABLE")

        for route in self.routes:

            print(route)