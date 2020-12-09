import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])[0:2]
    ext_years = np.arange(df['Year'].iloc[0], 2050)
    plt.plot(ext_years, intercept + slope*ext_years, 'r')

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()