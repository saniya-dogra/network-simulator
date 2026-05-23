class Signal:

    def show_signal(self, bits):

        print("\nDigital Signal Representation")

        for bit in bits:

            if bit == '1':
                print("HIGH", end=" ")

            else:
                print("LOW", end=" ")

        print()