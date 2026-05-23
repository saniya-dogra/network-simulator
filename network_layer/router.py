from network_layer.routing_table import RoutingTable
from network_layer.longest_prefix import LongestPrefixMatching


class Router:

    def __init__(self, name):

        self.name = name

        self.routing_table = RoutingTable()

        self.prefix_matcher = LongestPrefixMatching()

        self.interfaces = []

    def add_interface(self, interface):

        self.interfaces.append(interface)

    def show_interfaces(self):

        print("\nROUTER INTERFACES")

        for interface in self.interfaces:

            interface.show()

    def add_route(self, network, mask, next_hop):

        self.routing_table.add_route(
            network,
            mask,
            next_hop
        )

    def route_packet(self, packet):

        print(f"\n{self.name} routing packet")

        best_route = self.prefix_matcher.match(
            packet.destination_ip,
            self.routing_table.routes
        )

        if best_route:

            print("Best Route Found :", best_route)

            print(
                f"Packet forwarded to next hop {best_route[2]}"
            )

        else:

            print("No Route Found")