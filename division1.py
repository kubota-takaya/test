x = 1003
y = 5

d = 0
r = 0

r = x
while (True):
    if r >= y:
        d += 1
        r -= y
    else:
        break

print "d=%d, r=%d" % (d, r)