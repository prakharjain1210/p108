from numpy import average
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data108.csv")
average=df["Avg Rating"].tolist()
fig=ff.create_distplot([average],["rating"],show_hist=False)
fig.show()