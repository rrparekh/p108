import plotly.figure_factory as ff
#Plotting the graph 

import pandas as pd 
# Process the data 

import csv
#read each data in the data files
 
df=pd.read_csv("data.csv")
# Reads the data file

fig = ff.create_distplot([df["Mobile Brand"].tolist()],["Brand"],show_hist=True)
#Plotting the graph 

fig.show()
#displays the graph 