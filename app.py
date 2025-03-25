import ipywidgets as widgets
from IPython.display import display
import numpy as np

def simple_model(x):
    return np.round(np.sin(sum(x)), 2)

slider1 = widgets.FloatSlider(min=-5.0, max=5.0, value=0.0, description='Input 1:')
slider2 = widgets.FloatSlider(min=-5.0, max=5.0, value=0.0, description='Input 2:')
slider3 = widgets.FloatSlider(min=-5.0, max=5.0, value=0.0, description='Input 3:')

output = widgets.Output()

def update_output(change):
    with output:
        output.clear_output()
        inputs = [slider1.value, slider2.value, slider3.value]
        result = simple_model(inputs)
        print("Output:", result)
        
slider1.observe(update_output, names='value')
slider2.observe(update_output, names='value')
slider3.observe(update_output, names='value')

display(slider1, slider2, slider3, output)
