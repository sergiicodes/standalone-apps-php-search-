#Import Libaries
import pandas as pd
import matplotlib.pyplot as pplt

xls = pd.ExcelFile(r"C:\Users\shacosta\Desktop\Motion Calcs/TylerThoennesData.xlsx")    #Read Excel File
df = pd.read_excel(xls, 'Graphs')                                                       #Read from specific sheet, 'Graphs'
df_clean = df.dropna()                                                                  #Clear any rows that have NaN (Not a Number) value 

#Establish the X,Z, and Path Velocities 
x_velocity = df_clean.iloc[:,0]
z_velocity = df_clean.iloc[:,1]
path_velocity = df_clean.iloc[:,2]

# Import the necessary modules
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D scatter plot
ax.plot(x_velocity, path_velocity, z_velocity, color='red', label='X Velocity')
ax.plot(x_velocity + 1, path_velocity, z_velocity, color='blue', label='Z Velocity')
ax.plot(x_velocity, path_velocity, z_velocity + 1, color='green', label='Path')

# Set the axis labels
ax.set_xlabel('X Velocity')
ax.set_zlabel('Z Velocity')
ax.set_ylabel('Path Velocity')

# Add the legend
ax.legend()

# Show the plot
plt.show()