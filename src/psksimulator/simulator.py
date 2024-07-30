# -*- coding: utf-8 -*-
"""
    This module contains simulation methods
"""

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import load
import csv

from psksimulator.models.ask import ASKModel
from psksimulator.models.bpsk import BPSKModel
from psksimulator.models.qpsk import QPSKModel


def _calculateBER(self, original_message, received_message):
    '''Function to calculate Bit Error Rate (BER)

    Returns
    -------
    ber [float]: Bit Error Rate
    '''
    errors = np.sum(original_message != received_message)
    ber = errors / self.bits_num
    return ber


def _save_to_csv(model, float_data, EbNodB):
    '''Function which save statistics from simulation to bers.csv file'''
    with open('data/output/bers.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([model.get_modulation_name(), model.sampling_frec, model.carry_frec, model.bits_num, np.round(model.noise, 1), float_data, EbNodB])


def _simulate(model):
    '''Function which simulates many modulations.'''
    for n in range(12):
        EbNo = 10.0**(n/10.0)
        noise = 1/np.sqrt(2*EbNo)*4
        model.set_noise(noise)
        signals = model.run()
        ber = _calculateBER(signals['message'], signals['received'])
        _save_to_csv(model, ber, EbNo)
        print("Koniec symulacji")


def plot_signals(model):
    '''Function which loads data output from model data folder and plot it'''
    signals = model.run()
    sns.set_theme()
    fig = plt.figure(figsize=(16,9))
    fig.suptitle(''.join(('Modulacja ', model.get_modulation_name())))
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


def show_result():
    '''Function which visualize models work'''
    bpsk_model = BPSKModel(512, 16, 8, 0.7)
    qpsk_model = QPSKModel(512, 16, 8, 0.7)
    ask_model = ASKModel(512, 16, 8, 0.5)

    plot_signals(bpsk_model)
    plot_signals(qpsk_model)
    plot_signals(ask_model)


def run():
    '''Run simulation'''

    with open('data/output/bers.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Model', 'Sampling Frec', 'Carry Frec', 'Bits Num', 'Noise', 'BER', 'EbNo(dB)'])

    bpsk_model = BPSKModel(16384, 4096, 2048, 4.0)
    qpsk_model = QPSKModel(16384, 4096, 2048, 4.0)
    ask_model = ASKModel(16384, 4096, 2048, 2.0)
    
    _simulate(bpsk_model)
    _simulate(qpsk_model)
    _simulate(ask_model)
