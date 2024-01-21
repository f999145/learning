import streamlit as sl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests


@sl.cache_data
def load_data():
    return pd.read_csv('new-site.zip', sep='\t')

@sl.cache_data
def load_style():
    return requests.get('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle').json()


def main():
    val = sl.slider('test',10,300,50)   
    df = load_data()
    df1 = df.query('index < @val')
    # sl.sidebar.write('test')
    # fig = plt.figure(figsize=(8,6))
    # plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    # sl.write(load_style())
    # plt.style.use(load_style())
    
    # plt.plot(df1.index, df1['dwell-time'])
    # sl.write(fig)
    sl.line_chart(data=df1,y='dwell-time',)
    
    slice_ = ['sum']
    tmp = df1.groupby('site').agg(sum=('dwell-time','sum'), mean=('dwell-time','mean'), median=('dwell-time','median'))
    tmp = tmp.style.set_properties(**{'background-color': '#2b1212'}, subset=slice_)
    sl.dataframe(tmp)


    


if __name__ == "__main__":
    main()