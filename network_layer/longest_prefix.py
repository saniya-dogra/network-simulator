class LongestPrefixMatching:

    def match(self, destination_ip, routes):

        best_match = None

        longest_mask = -1

        for network, mask, next_hop in routes:

            if destination_ip.startswith(network[:-1]):

                if mask > longest_mask:

                    longest_mask = mask

                    best_match = (network, mask, next_hop)

        return best_match