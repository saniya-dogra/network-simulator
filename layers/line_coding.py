def nrz_encode(binary):
    signal = []
    for bit in binary.replace(" ", ""):
        if bit == '1':
            signal.append(1)
        else:
            signal.append(0)
    return signal