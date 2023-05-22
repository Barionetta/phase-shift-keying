# -*- coding: utf-8 -*-
"""
    This module contains simulation methods
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import load
from src import amplitude_shift_keying
from src import binary_shift_keying
from src import quadrature_shift_keying

def plotASK():
    '''Function which loads data output from  ASK model and plot it'''

    data1 = load('data/output/ASK/message.npy')
    data2 = load('data/output/ASK/noisy_signal.npy')
    data3 = load('data/output/ASK/signal.npy')
    data4 = load('data/output/ASK/recieved_signal.npy')
    fig = plt.figure(figsize=(16,9))
    fig.suptitle('Modulacja ASK')
    gs = plt.GridSpec(nrows=2, ncols=2)
    ax0 = fig.add_subplot(gs[0,0])
    ax0.plot(data1,color='indigo', alpha=0.90)
    ax0.set_xlabel('Wiadomość')
    ax1 = fig.add_subplot(gs[0,1])
    ax1.plot(data3,color='mediumorchid', alpha=0.90)
    ax1.set_xlabel('Czas [s]')
    ax1.set_ylabel('Sygnał s(t)')
    ax2 = fig.add_subplot(gs[1,0])
    ax2.plot(data2,color='deeppink', alpha=0.90)
    ax2.set_xlabel('Czas [s]')
    ax2.set_ylabel('Sygnał s(t)+n(t)')
    ax3 = fig.add_subplot(gs[1,1])
    ax3.plot(data4,color='tomato', alpha=0.90)
    ax3.set_xlabel('Czas [s]')
    ax3.set_ylabel('Sygnał r(t)')
    plt.tight_layout()
    plt.show()

def plotBPSK():
    '''Function which loads data output from  BPSK model and plot it'''

    data1 = load('data/output/BPSK/message.npy')
    data2 = load('data/output/BPSK/noisy_signal.npy')
    data3 = load('data/output/BPSK/signal.npy')
    data4 = load('data/output/BPSK/received_signal.npy')
    fig = plt.figure(figsize=(16,9))
    fig.suptitle('Modulacja BPSK')
    gs = plt.GridSpec(nrows=2, ncols=2)
    ax0 = fig.add_subplot(gs[0,0])
    ax0.plot(data1,color='indigo', alpha=0.90)
    ax0.set_xlabel('Wiadomość')
    ax1 = fig.add_subplot(gs[0,1])
    ax1.plot(data3,color='mediumorchid', alpha=0.90)
    ax1.set_xlabel('Czas [s]')
    ax1.set_ylabel('Sygnał s(t)')
    ax2 = fig.add_subplot(gs[1,0])
    ax2.plot(data2,color='deeppink', alpha=0.90)
    ax2.set_xlabel('Czas [s]')
    ax2.set_ylabel('Sygnał s(t)+n(t)')
    ax3 = fig.add_subplot(gs[1,1])
    ax3.plot(data4,color='tomato', alpha=0.90)
    ax3.set_xlabel('Czas [s]')
    ax3.set_ylabel('Sygnał r(t)')
    plt.tight_layout()
    plt.show()

def plotQPSK():
    '''Function which loads data output from  QPSK model and plot it'''

    data1 = load('data/output/QPSK/message.npy')
    data2 = load('data/output/QPSK/noisy_signal.npy')
    data3 = load('data/output/QPSK/signal.npy')
    data4 = load('data/output/QPSK/received_signal.npy')
    fig = plt.figure(figsize=(16,9))
    fig.suptitle('Modulacja QPSK')
    gs = plt.GridSpec(nrows=2, ncols=2)
    ax0 = fig.add_subplot(gs[0,0])
    ax0.plot(data1,color='indigo', alpha=0.90)
    ax0.set_xlabel('Wiadomość')
    ax1 = fig.add_subplot(gs[0,1])
    ax1.plot(data3,color='mediumorchid', alpha=0.90)
    ax1.set_xlabel('Czas [s]')
    ax1.set_ylabel('Sygnał s(t)')
    ax2 = fig.add_subplot(gs[1,0])
    ax2.plot(data2,color='deeppink', alpha=0.90)
    ax2.set_xlabel('Czas [s]')
    ax2.set_ylabel('Sygnał s(t)+n(t)')
    ax3 = fig.add_subplot(gs[1,1])
    ax3.plot(data4,color='tomato', alpha=0.90)
    ax3.set_xlabel('Czas [s]')
    ax3.set_ylabel('Sygnał r(t)')
    plt.tight_layout()
    plt.show()

def run():
    sns.set_theme()
    bpsk_model = binary_shift_keying.BPSK(1024, 120, 64, 0.4)
    bpsk_model.simulate()
    plotBPSK()
    qpsk_model = quadrature_shift_keying.QPSK(1024, 120, 64, 0.4)
    qpsk_model.simulate()
    plotQPSK()
    ask_model = amplitude_shift_keying.ASK(1024, 120, 64, 0.4)
    ask_model.simulate()
    plotASK()
    