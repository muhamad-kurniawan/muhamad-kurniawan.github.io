import streamlit as st
import numpy as np

# A dummy function simulating a neural network's output
def simple_model(inputs):
    # For demonstration, just use a sine of the sum of inputs
    return np.round(np.sin(sum(inputs)), 2)

st.title("Neural Network Simulation Game")
st.write("Adjust the sliders to match the target output!")

# Create sliders for input variables
x1 = st.slider("Input 1", -5.0, 5.0, 0.0)
x2 = st.slider("Input 2", -5.0, 5.0, 0.0)
x3 = st.slider("Input 3", -5.0, 5.0, 0.0)

# Calculate model output
output = simple_model([x1, x2, x3])
st.write("Output:", output)

# Define a target output for the game
target_output = 0.87

if output == target_output:
    st.success("Congratulations! You hit the target output!")
else:
    st.info("Keep trying to match the target output!")
