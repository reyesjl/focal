import numpy as np
import pyttsx3
from print_utils import p, p_with_typing, printServerCall, printTransfer, loading_bar

printServerCall("Loading Scalar Simulation")
engine = pyttsx3.init()
engine.say("Loading Scalar Simulation")
engine.runAndWait()

# generate two random vectors
a = np.random.rand(5)
b = np.random.rand(5)
aTb = np.dot(a, b)

p_with_typing(f"Generating random vectors...", 1)
loading_bar(total=10)
p_with_typing(f"a: {a}")
p_with_typing(f"b: {b}")
p_with_typing(f"aTb: {aTb}")

printTransfer()

# generate two random scalers
s1 = np.random.rand()
s2 = np.random.rand()
p_with_typing("Generating random scalers...", 1)
loading_bar(total=10)
p_with_typing(f"s1: {s1}, s2: {s2}")

# scale the vectors
a = a * s1
b = b * s2
aTb = np.dot(a, b)

printTransfer()

p_with_typing(f"Scaled random vectors...", 1)
loading_bar(total=5)
p_with_typing(f"a: {a}")
p_with_typing(f"b: {b}")
p_with_typing(f"aTb: {aTb}")

# generate two new vectors
