class ClassfulAddressing:

    def identify_class(self, ip):

        first_octet = int(ip.split('.')[0])

        if first_octet <= 127:
            return "Class A"

        elif first_octet <= 191:
            return "Class B"

        elif first_octet <= 223:
            return "Class C"

        return "Unknown"