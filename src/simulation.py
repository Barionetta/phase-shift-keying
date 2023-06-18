# -*- coding: utf-8 -*-
"""
    This module contains simulation methods
"""
__version__ = '0.1.2'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import load
import csv
from src import amplitude_shift_keying
from src import binary_shift_keying
from src import quadrature_shift_keying

def plot_demo(model):
    '''Function which loads data output from model data folder and plot it'''
    data1 = load(''.join(('data/output/', model, '/message.npy')))
    data2 = load(''.join(('data/output/', model, '/noisy_signal.npy')))
    data3 = load(''.join(('data/output/', model, '/signal.npy')))
    data4 = load(''.join(('data/output/', model, '/received_signal.npy')))
    fig = plt.figure(figsize=(16,9))
    fig.suptitle(''.join(('Modulacja ', model)))
    gs = plt.GridSpec(nrows=2, ncols=2)
    ax0 = fig.add_subplot(gs[0,0])
    ax0.plot(data1,color='indigo', alpha=0.90)
    ax0.set_xlabel('Wiadomość')
    ax1 = fig.add_subplot(gs[0,1])
    ax1.plot(data3,color='mediumorchid', alpha=0.90)
    ax1.set_xlabel('Czas')
    ax1.set_ylabel('Sygnał s(t)')
    ax2 = fig.add_subplot(gs[1,0])
    ax2.plot(data2,color='deeppink', alpha=0.90)
    ax2.set_xlabel('Czas')
    ax2.set_ylabel('Sygnał s(t)+n(t)')
    ax3 = fig.add_subplot(gs[1,1])
    ax3.plot(data4,color='tomato', alpha=0.90)
    ax3.set_xlabel('Odebrana wiadomość')
    plt.tight_layout()
    plt.show()

def demo():
    '''Function which visualize models work'''
    sns.set_theme()
    bpsk_model = binary_shift_keying.BPSK(512, 16, 8, 0.7)
    bpsk_model.demo_run()
    plot_demo('BPSK')
    qpsk_model = quadrature_shift_keying.QPSK(512, 16, 8, 0.7)
    qpsk_model.demo_run()
    plot_demo('QPSK')
    ask_model = amplitude_shift_keying.ASK(512, 16, 8, 0.5)
    ask_model.demo_run()
    plot_demo('ASK')

def run():
    '''Main simulation loop'''

    with open('data/output/bers.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Model', 'Sampling Frec', 'Carry Frec', 'Bits Num', 'Noise', 'BER', 'EbNo(dB)'])

    bpsk_model = binary_shift_keying.BPSK(16384, 4096, 2048, 4.0)
    bpsk_model.simulate()
    qpsk_model = quadrature_shift_keying.QPSK(16384, 4096, 2048, 4.0)
    qpsk_model.simulate()
    ask_model = amplitude_shift_keying.ASK(16384, 4096, 2048, 2.0)
    ask_model.simulate()
    