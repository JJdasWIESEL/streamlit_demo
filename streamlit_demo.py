import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
def load_data():
    return sns.load_dataset('iris')

data = load_data()

# Title
st.title("Iris Dataset Plotting App")

# Dropdowns for selecting x and y columns
x_axis = st.selectbox("Select X-axis", data.columns[:-1])  # Exclude 'species' for the x-axis
y_axis = st.selectbox("Select Y-axis", data.columns[:-1])  # Exclude 'species' for the y-axis

# Plot the selected columns
if st.button("Plot"):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_axis, y=y_axis, hue='species', style='species', s=100)
    plt.title(f"{y_axis} vs {x_axis}")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)
