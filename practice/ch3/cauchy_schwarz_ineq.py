import numpy as np
import matplotlib.pyplot as plt

a = np.random.randn(5)
b = np.random.randn(5)
c = np.random.randn()*a

an = np.linalg.norm(a)
bn = np.linalg.norm(b)
cn = np.linalg.norm(c)

aTb = np.dot(a, b)
aTc = np.dot(a, c)

print(f"aTb: {abs(aTb)}, norm: {an * bn}")
print(f"aTc: {aTc}, norm: {an * cn}")


print("NEW CHALLENGE")
print("a = [1, -2], b = [2, 3], c = [0, 2]")
print("Which two vectors meet an an obtuse angle?")

def determineAngle(angle):
    if ( angle > 0 ) :
        print("Angle is acute")
    elif ( angle < 0 ):
        print("Angle is obtuse")
    else:
        print("Angle is right")
    
a = np.array([1, -2])
b = np.array([2, 3])
c = np.array([0, 2])

aTb = np.dot(a, b)
print(f"aTb: {aTb}")
aTc = np.dot(a, c)
print(f"aTc: {aTc}")
bTc = np.dot(b, c)
print(f"bTc: {bTc}")

determineAngle(aTb)
determineAngle(aTc)
determineAngle(bTc)


