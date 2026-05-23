class LineCoding:

    def nrz(self, bits):

        result = ""

        for bit in bits:

            if bit == '1':
                result += "HIGH "

            else:
                result += "LOW "

        return result

    def manchester(self, bits):

        result = ""

        for bit in bits:

            if bit == '1':
                result += "10 "

            else:
                result += "01 "

        return result