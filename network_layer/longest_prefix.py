import ipaddress


class LongestPrefixMatching:

    def match(self, destination_ip, routes):

        best_match = None

        longest_prefix = -1

        dest_ip = ipaddress.IPv4Address(destination_ip)

        for network, mask, next_hop in routes:

            subnet = ipaddress.IPv4Network(
                f"{network}/{mask}",
                strict=False
            )

            if dest_ip in subnet:

                if mask > longest_prefix:

                    longest_prefix = mask

                    best_match = (
                        network,
                        mask,
                        next_hop
                    )

        return best_match