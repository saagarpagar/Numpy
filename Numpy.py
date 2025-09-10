# My personal learning notes of NumPy
# ================================

import numpy as np
# --------------------------------
# 1. Creating Arrays
# --------------------------------
print("\n=== Array Creation ===")

# Creating a simple array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Array of zeros
zeros = np.zeros(5)
print("Zeros:", zeros)

# Array of ones
ones = np.ones(5)
print("Ones:", ones)

# Array with range
r = np.arange(1, 10)  # from 1 to 9
print("Range Array:", r)

# Practice:
# 👉 Create an array of numbers from 10 to 50 with a step of 5.


# --------------------------------
# 2. Array Properties
# --------------------------------
print("\n=== Array Properties ===")
print("Shape of arr:", arr.shape)
print("Data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)
print("Size (total elements):", arr.size)


# --------------------------------
# 3. Indexing and Slicing
# --------------------------------
print("\n=== Indexing and Slicing ===")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice 2 to 4:", arr[1:4])

# Practice:
# 👉 Print every second element from the array r.


# --------------------------------
# 4. Array Operations
# --------------------------------
print("\n=== Array Operations ===")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

print("Square of a:", np.square(a))
print("Square root of b:", np.sqrt(b))

# Practice:
# 👉 Multiply array a by 10 using broadcasting.


# --------------------------------
# 5. Useful Functions
# --------------------------------
print("\n=== Useful Functions ===")

nums = np.array([10, 20, 30, 40, 50])
print("Sum:", np.sum(nums))
print("Mean:", np.mean(nums))
print("Max:", np.max(nums))
print("Min:", np.min(nums))

# Practice:
# 👉 Find the average of [5, 15, 25, 35, 45] using NumPy.


# --------------------------------
# 6. Reshaping
# --------------------------------
print("\n=== Reshaping Arrays ===")

m = np.arange(1, 13)
print("Original:", m)

reshaped = m.reshape(3, 4)  # 3 rows, 4 columns
print("Reshaped (3x4):\n", reshaped)

# Practice:
# 👉 Reshape array of 16 numbers (1-16) into a 4x4 matrix.


# --------------------------------
# 7. Random Numbers
# --------------------------------
print("\n=== Random Numbers ===")

rand_arr = np.random.rand(3, 3)  # 3x3 random numbers between 0 and 1
print("Random Array:\n", rand_arr)

rand_ints = np.random.randint(1, 10, size=(2, 5))  # random ints 1-9
print("Random Integers:\n", rand_ints)

# Practice:
# 👉 Generate a 5x5 array of random integers between 50 and 100.


# --------------------------------
# 8. Practice Mini Project
# --------------------------------
print("\n=== Mini Project: Student Marks ===")

# Suppose we have marks of 5 students in 3 subjects
marks = np.array([
    [85, 90, 95],
    [78, 88, 92],
    [80, 70, 75],
    [90, 95, 85],
    [60, 65, 70]
])

print("Marks:\n", marks)

# Average marks of each student
avg_per_student = np.mean(marks, axis=1)
print("Average per student:", avg_per_student)

# Average marks per subject
avg_per_subject = np.mean(marks, axis=0)
print("Average per subject:", avg_per_subject)

# Practice:
# 👉 Find the highest marks scored in each subject.
