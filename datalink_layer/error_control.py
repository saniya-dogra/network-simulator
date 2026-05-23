class ParityCheck:

    def generate_parity(self, bits):

        ones = bits.count('1')

        if ones % 2 == 0:
            return '0'

        return '1'

    def check_error(self, bits, parity):

        total_ones = bits.count('1')

        if parity == '1':
            total_ones += 1

        if total_ones % 2 == 0:
            return "No Error"

        return "Error Detected"