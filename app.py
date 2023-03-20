import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_limit = 100
df = pd.DataFrame()
df['X'] = np.arange(x_limit)
df['Y'] = np.random.randn(100)

st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_circle(size=60).encode(x='X',
    y='Y')

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Gave positive and negative values different colors.
- Added a tooltip to show the X, Y and class values.
- Changed the data point to circles with a specified size.
- Changed the opacity of the points.
- Gave our chart a title.
""")
            
df['class'] = ['class 1' if df.loc[ind,'Y'] > 0 else 'class 2' for ind in df.index]
scatter1 = alt.Chart(df,title="Just random values dude!!").mark_circle(size=60).encode(x='X',
    y='Y',
    color = 'class',
    tooltip=['X', 'Y', 'class']
    ).configure_mark(
    opacity=0.5)
st.altair_chart(scatter1, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

np.random.seed(42)

# Generating Data
source = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.normal(3, 2, 1000)
})

hists = alt.Chart(source).transform_fold(
    ['Trial A', 'Trial B', 'Trial C'],
    as_=['Experiment', 'Measurement']
).mark_bar(
    opacity=0.3,
    binSpacing=0
).encode(
    alt.X('Measurement:Q', bin=alt.Bin(maxbins=20)),
    alt.Y('count()', stack=None),
    alt.Color('Experiment:N', legend=alt.Legend(orient="left"))
    #alt.Color('Experiment:N')
)
st.altair_chart(hists, use_container_width=True)

st.markdown("""
The 2 changes I made were:
- Changed the bin size
- Changed the legend orientation to the left side.
"""
)

