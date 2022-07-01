from cv2 import mean
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("/tAverage Distance of Sports.csv")
sports_list=df["Sports"].tolist()
distance_list=df["Distance(Km)"].tolist

fig=go.Figure(go.Bar(
    x=df["Sports"].mean(),
    y=["Distance(Km)"],
    orientation="h"
))
fig.show()