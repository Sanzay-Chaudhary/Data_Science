# What is the shape of this array?
# What is the average age of the passengers?
# What is the passenger number of the oldest passenger? Who is the youngest?
# What is the percentage of folks that survived?

import numpy as np
passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])
# Shape of the array
shape = passengers.shape

# Average age of the passengers
average_age = np.average(passengers[:, 3]) #find average of the age column (index 3)

# Passenger number of the oldest passenger
# argmax = Returns the index position of the largest element.
oldest_passenger_index = np.argmax(passengers[:, 3]) #find index of the oldest passenger 
oldest_passenger_number = passengers[oldest_passenger_index, 0] #find passenger number of the oldest passenger

# Passenger number of the youngest passenger
youngest_passenger_index = np.argmin(passengers[:, 3]) #find index of the youngest passenger
youngest_passenger_number = passengers[youngest_passenger_index, 0]

# Percentage of folks that survived
total_passengers = passengers.shape[0] #find total number of passengers
survived_passengers = np.sum(passengers[:, 1]) #sum the second column (index 1) to find number of survivors
percentage_survived = (survived_passengers / total_passengers) * 100
# Output results

print(f"Shape of the array: {shape}")
print(f"Average age of the passengers: {average_age:.2f}")      
print(f"Passenger number of the oldest passenger: {oldest_passenger_number}")
print(f"Passenger number of the youngest passenger: {youngest_passenger_number}")   
print(f"Percentage of folks that survived: {percentage_survived:.2f}%")
# Titanic Passenger Data Analysis