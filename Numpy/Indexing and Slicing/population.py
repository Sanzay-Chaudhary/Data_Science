# Print the first item and the last item
# Now find the difference between them using subtraction. How did the population change in the last ten years?
# COVID-19 happened during 2020-2022; those were some crazy years. Use slicing, and print the population during those years for your city.


import numpy as np
nyc_population = np.array([19571216, 19673200, 19854526, 20104710, 19463131, 19544098, 19593849, 19636391, 19657321, 19653431, 19626488])
print(nyc_population[0,])  # First element
print(nyc_population[-1])  # Last element
population_change = nyc_population[-1] - nyc_population[0]
print("The population change in the last ten years is:",population_change)
nyc_population_covid = nyc_population[3:6]  # Slicing for the years 2020-2022
print(f"Population during COVID-19 years (2020-2022): {nyc_population_covid}")
