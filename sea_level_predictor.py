import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import scipy.stats as stats 

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data Points')


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    #extend the line of best fit to year 2050
    line = slope * range(1880, 2051) + intercept
    plt.plot(range(1880,2051), line, color='r', label='Line of Best Fit')

    # Create second line of best fit
    dt_since_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = stats.linregress(dt_since_2000['Year'], dt_since_2000['CSIRO Adjusted Sea Level'])
    line_2000 = slope_2000 * range(2000, 2051) + intercept_2000
    plt.plot(range(2000, 2051), line_2000, color='g', label='Line of Best Fit (since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()    