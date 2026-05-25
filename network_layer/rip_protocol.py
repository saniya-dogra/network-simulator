class RIPProtocol:

    def __init__(self):
        self.routing_table = []

    def add_route(self, network, hops):

        self.routing_table.append({
            "network": network,
            "hop_count": hops
        })

    def start(self):

        print("\nRIP PROTOCOL")

        print("Distance Vector Routing Started")
        print("Metric Used : Hop Count")
        print("Routing Updates Exchanged")

        if not self.routing_table:
            print("No Routes Available")
            return

        print("\nRouting Table")

        for route in self.routing_table:
            print(
                f"{route['network']} -> "
                f"{route['hop_count']} hop(s)"
            )

        best_route = min(
            self.routing_table,
            key=lambda x: x["hop_count"]
        )

        print(
            f"\nBest Route Selected : "
            f"{best_route['network']}"
        )