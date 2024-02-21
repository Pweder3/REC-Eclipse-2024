

# REMEBER X IS FORWOARD AND BACKWARD
def inchtoM(inch):
    return inch/39.37


COLOR_MAT_SIZE = inchtoM(12)

MAT_D = [inchtoM(42),inchtoM(96)]

Y_KEYHOLE_XY = [inchtoM(72),0]
Y_KEYHOLE_BASE_HEIGHT = inchtoM(38) # not including the keyhole just the pole

G_KEYHOLE_XY = [MAT_D[1] + MAT_D[0]/2 + COLOR_MAT_SIZE/2 ,MAT_D[1]/2]
# print(G_KEYHOLE_XY[0]*39.37)

G_KEYHOLE_BASE_HEIGHT = inchtoM(46) # not including the keyhole just the pole

KEYHOLE_DIAMATER = inchtoM(30)



LANDING_PAD = [G_KEYHOLE_XY[0],(MAT_D[1] - MAT_D[0]/2 ),0]
# 2.438795804977417, 1.451956033706665

# 2.7232189178466797, 1.4411605596542358
print(LANDING_PAD)