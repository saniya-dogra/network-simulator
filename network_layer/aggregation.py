import ipaddress

class AddressAggregation:

    def summarize(self, networks=None):

        if networks is None:
            networks = ["192.168.1.0/24", "192.168.2.0/24"]

        print("\nAddress Aggregation")

        net_objects = [ipaddress.IPv4Network(n, strict=False) for n in networks]

        for net in net_objects:
            print(f"  Network : {net}")

        supernet = ipaddress.collapse_addresses(net_objects)
        collapsed = list(supernet)

        if len(collapsed) == 1:
            print(f"  Summarized to : {collapsed[0]}")

        else:
            print(f"  Cannot summarize to single block. Collapsed:")
            for net in collapsed:
                print(f"    {net}")