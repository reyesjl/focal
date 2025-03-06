# create 2 4x6 matrices with random values.
# Use a for-loop to compute the dot products between corresponding columns.

# Jose Reyes
# March 06, 2025

import numpy as np
import matplotlib.pyplot as plt

def dotit():
    rows = 50
    cols = 100

    # Create 2 4x6 matrices with random values
    matrix1 = np.random.rand(rows, cols)
    matrix2 = np.random.rand(rows, cols)

    # Use a for-loop to compute the dot products between corresponding columns
    dot_products = []
    for i in range(cols):
       dot_product = np.dot(matrix1[:, i], matrix2[:, i])
       print(f"Dot product of column {i} is {dot_product}")
       dot_products.append(dot_product)

    
    norm = np.linalg.norm(dot_products)
    print(f"Norm of dot products: {norm}")
    # How would I do this manually without numpy dot()
    # for i in range(cols):
    #     dot_product = 0
    #     for j in range(rows):
    #         dot_product += matrix1[j, i] * matrix2[j, i]
    #         print(f"Result of value: {matrix1[j, i]} + value: {matrix2[j, i]} is = {matrix1[j, i] * matrix2[j, i]}")
    #     print(f"Dot product of column {i} is {dot_product}")
    #     dot_products.append(dot_product)

    print("Matrix 1:")
    print(matrix1)

    print("Matrix 2:")
    print(matrix2)


    # Plot the matrices
    plt.bar(range(cols), dot_products)
    plt.xlabel("Column")
    plt.ylabel("Dot Product")
    plt.title("Dot Products of Corresponding Columns")
    plt.savefig("dot_products_bar.png")

    plt.figure().clear()

    plt.plot(range(cols), dot_products)
    plt.xlabel("Column")
    plt.ylabel("Dot Product")
    plt.title("Dot Products of Corresponding Columns")
    plt.savefig("dot_products_line.png")

dotit()