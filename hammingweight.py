HW = []
for v in range(256):
    c = 0
    for i in range(8):
        c += (v >> i) & 0x01
    HW.append(c)

def HD(a,b):
    return HW[a^b]
