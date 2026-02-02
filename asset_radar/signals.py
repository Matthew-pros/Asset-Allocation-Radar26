def generate_signal(z):
    if z > 1.5:
        return "PRODAT"
    elif z < -1.5:
        return "KOUPIT"
    return "DRŽET"
