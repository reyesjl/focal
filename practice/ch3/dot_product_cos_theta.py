import numpy as np
import matplotlib.pyplot as plt

# Create two vectors in 3d space
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

vector3 = np.array([ 1, 1, 1 ])
vector4 = np.array([ 1, -2, -1 ])

vector3_norm = np.linalg.norm(vector3)
vector4_norm = np.linalg.norm(vector4)
print(f"Norm of vector3 is {vector3_norm}")
print(f"Norm of vector4 is {vector4_norm}")

dot_product2 = np.dot(vector3, vector4)
print(f"Dot product of vector3 and vector4 is {dot_product2}")

# Verify the Cauchy-Schwarz inequality
lhs = abs(dot_product2)
rhs = vector3_norm * vector4_norm
print(f"Absolute value of dot product: {lhs}")
print(f"Product of norms: {rhs}")
print(f"Cauchy-Schwarz inequality holds: {lhs <= rhs}")

theta = dot_product2 / (vector3_norm * vector4_norm)
angle = np.arccos(theta)
print(f"Theta between vector3 and vector4 is {theta}")
print(f"Angle between vector3 and vector4 is {angle}")


# Compute the dot product manually
dot_product = 0
for i in range(3):
    dot_product += vector1[i] * vector2[i]

# OR

# Compute the dot product
dot_product = np.dot(vector1, vector2)

# Compute angle between vectors
cos_theta = dot_product / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
theta = np.arccos(cos_theta)
