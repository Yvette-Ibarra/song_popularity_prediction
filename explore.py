import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import wrangle as w




# Global Variables____________________________________________________________________
# obtain data frame as df
df = w.acquire_data()
# prep data frame
df = w.data_prep(df)

# obrain train dataframe as train
train, _, _ = w.split_data(df)

#____________________________________________________________________________________

def viz_target_dist():    
    # set figure size
    plt.figure(figsize = (15,7))
    # define graph
    graph = sns.distplot( a=train["song_popularity"], hist=True, kde=True, rug=False,
             hist_kws={"color": "gray", "alpha": 0.65, "linewidth": 2,"fill":True,"edgecolor":'dimgrey'},
             kde_kws={"color": "skyblue", "alpha": 0.8, "linewidth": 3, "shade": True})
    # set vertical lines for mean and median
    graph.axvline(train.song_popularity.mean(), color = 'darkslateblue', linewidth = 1.5, linestyle="--",label="Mean Song Popularity Score" )
    graph.axvline(train.song_popularity.median(), color = 'navy', linewidth = 1.5, linestyle="--",label="Median Song Popularity Score" )
    # set labels for title, axis and vertical lines
    plt.title( 'Distribution of Song Popularity Score',c="Black",fontsize = 25)
    graph.set_xlabel('Song Popularity Score', fontsize=20)
    graph.set_ylabel('Density', fontsize=20)
    graph.set_yticklabels(graph.get_yticks(), size = 15)
    graph.text(train.song_popularity.mean()-2, .01, f'Mean = {round(train.song_popularity.mean(),2)}', rotation = 90, fontsize= 12, color='darkslateblue');
    graph.text(train.song_popularity.median()-2, .01, f'Median = {round(train.song_popularity.median(),2)}', rotation = 90, fontsize= 12, color='navy');
    graph.set_xticklabels([-20,0,20,40,60,80,100], size = 15,)
    graph.legend(loc=0)

    # set background color
    graph.set(facecolor='aliceblue')

    plt.show();