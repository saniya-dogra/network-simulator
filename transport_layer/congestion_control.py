class CongestionControl:

    def simulate(self):

        print("\nCONGESTION CONTROL")      # congestion control prevents the sender from overwhelming the network.(slowdown)

        print("Slow Start Phase")          #until limit reached(double 2 4 8)

        print("Congestion Avoidance")       #thn slow down to 1 inc at each round

        print("Fast Recovery")              #divide by half, start from 1 again