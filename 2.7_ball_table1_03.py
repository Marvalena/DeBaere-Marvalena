t = 0 #seconds
g = 9.81 #m/s**2
v = 50 #m/s
T = [] #list of times
print ('Time:')
while t <= int(2*v/g):
    T.append(t)
    t = t + 1
print (T)
print('Height:')
Y = [] # list of heights
for t in T:
    y = v*t - (1/2)*g*t**2
    Y.append(y)
print (Y)
print ('end of table')