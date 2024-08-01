# -*- coding: utf-8 -*-
"""
    This file contains functions for simulation visualization
"""
import seaborn as sns
import matplotlib.pyplot as plt

def plot_signals(model : str, signals : dict):
    '''Function which loads data output from model data folder and plot it'''
    sns.set_theme()
    fig = plt.figure(figsize=(16,9))
    fig.suptitle(''.join(('Modulacja ', model)))
    gs = plt.GridSpec(nrows=2, ncols=2)

    ax0 = fig.add_subplot(gs[0,0])
    ax0.plot(signals['message'],color='indigo', alpha=0.90)
    ax0.set_xlabel('Wiadomość')
    ax1 = fig.add_subplot(gs[0,1])
    ax1.plot(signals['signal'],color='mediumorchid', alpha=0.90)
    ax1.set_xlabel('Czas')
    ax1.set_ylabel('Sygnał s(t)')
    ax2 = fig.add_subplot(gs[1,0])
    ax2.plot(signals['noises'],color='deeppink', alpha=0.90)
    ax2.set_xlabel('Czas')
    ax2.set_ylabel('Sygnał s(t)+n(t)')
    ax3 = fig.add_subplot(gs[1,1])
    ax3.plot(signals['received'],color='tomato', alpha=0.90)
    ax3.set_xlabel('Odebrana wiadomość')
    
    plt.tight_layout()
    plt.show()