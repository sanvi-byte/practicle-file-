import streamlit as st
import numpy as np
import pandas as pd

# ====================================================================
# FEATURE 1: DISPLAY THE REQUIRED HEADING
# ====================================================================
st.title("Welcome to AI")
st.subheader("Class 12 Interactive Student Dashboard")
st.write("---")

# ====================================================================
# FEATURE 2: TUPLE OPERATIONS (MAX/MIN VALUES)
# ====================================================================
st.header("1. Tuple Analytics")

# Create a tuple of sample scores
scores_tuple = (42, 17, 89, 5, 63, 21)
max_val = max(scores_tuple)
min_val = min(scores_tuple)

st.write("The dataset tuple is:", scores_tuple)
st.write("Maximum value found in the tuple:", max_val)
st.write("Minimum value found in the tuple:", min_val)
st.write("---")

# ====================================================================
# FEATURE 3: DICTIONARY OPERATIONS (STUDENT DETAILS)
# ====================================================================
st.header("2. Student Registry (Dictionary)")

# Create an initial student details dictionary
student_details = {
    "Name": "Ananya Iyer",
    "Marks": 94,
    "Grade": "A+"
}

# Access values using keys
student_name = student_details["Name"]
student_marks = student_details["Marks"]
student_grade = student_details["Grade"]

# Add a new key-value pair to the existing dictionary
student_details["Subject"] = "Informatics Practices"

st.write("Accessed Name from key:", student_name)
st.write("Accessed Marks from key:", student_marks)
st.write("Accessed Grade from key:", student_grade)
st.write("Updated Dictionary with new Subject key:", student_details)
st.write("---")

# ====================================================================
# FEATURE 4: NUMPY ARRAY OPERATIONS (SHAPE & MATH)
# ====================================================================
st.header("3. Matrix Computations (NumPy)")

# Create a 2D NumPy array
matrix_array = np.array([[10, 20, 30], [40, 50, 60]])

# Perform math operations with another array
modifier_array = np.array([[2, 2, 2], [2, 2, 2]])
added_array = matrix_array + modifier_array
multiplied_array = matrix_array * modifier_array

st.write("Original 2D NumPy Matrix:")
st.dataframe(matrix_array)

st.write("Shape of the array (rows, columns):", matrix_array.shape)
st.write("Dimensions of the array:", matrix_array.ndim)
st.write("Result of Element-wise Addition (+ 2):")
st.dataframe(added_array)
st.write("Result of Element-wise Multiplication (* 2):")
st.dataframe(multiplied_array)
st.write("---")

# ====================================================================
# FEATURE 5: PANDAS DATAFRAME & STATISTICS
# ====================================================================
st.header("4. Performance Reporting (Pandas)")

# Create a DataFrame containing student marks and attendance
student_data = {
    "Name": ["Rohan", "Sneha", "Amit", "Priya"],
    "Marks": [85, 92, 78, 95],
    "Attendance": [90, 95, 82, 98]
}
df = pd.DataFrame(student_data)

# Find average marks using the mean() function
average_marks = df["Marks"].mean()

st.write("Generated Student DataFrame:")
st.dataframe(df)

st.write("Calculated Class Average Marks:", average_marks)
st.write("---")

# ====================================================================
# INTERACTIVE STREAMLIT ELEMENT (BONUS FOR PROJECT MARKS)
# ====================================================================
st.header("5. Interactive Data Filter")
selected_student = st.selectbox("Select a student to check records:", df["Name"])
filtered_data = df[df["Name"] == selected_student]
st.write("Records for selected student:")
st.dataframe(filtered_data)
