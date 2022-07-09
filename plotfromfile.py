import pandas as pd
import plotly
import plotly.graph_objs as go
INPATH='C:\\Automations2\\project1\\'

df=pd.read_csv(INPATH+'raw.txt', sep='\t')

data = [go.stocks(
    x = df['Begin Time'],
    y = df['DL IP Throughput'])]
layout = go.Layout(
        xaxis=dict(
            title='Begin Time',    
        ),
        yaxis=dict(
            title='DL IP Throughput',  
        )
    )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig,filename='throughput.html',config={'displayModeBar': False})



import plotly.express as px

df = px.data.stocks(indexed=True)-1
fig = px.area(df, facet_col="company", facet_col_wrap=2)
fig.show()