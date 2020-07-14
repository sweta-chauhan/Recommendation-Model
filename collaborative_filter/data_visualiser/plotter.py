#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:55:19 2020

@author: sweta
"""
from matplotlib import pyplot
import seaborn as sns


def plotdistribution(dataframe, size=15):
    numerical_col = dataframe.select_dtypes(include=['int64', 'float64']).columns
    subset = dataframe[numerical_col]
    subset.hist(figsize=(size, size))
    pyplot.show()

def plot_models(results, names,showmeans = True):
    pyplot.boxplot(results, labels=names, showmeans=True)
    pyplot.show()
    
def plotcorrelation(dataframe, size=12):
    corr= dataframe.corr()
    fig, ax =pyplot.subplots(figsize=(size,size))
    sns.heatmap(corr)