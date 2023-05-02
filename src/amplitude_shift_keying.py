# -*- coding: utf-8 -*-
"""
    This file contains ASK modulation model
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import numpy as np

class ASK:
    ''' Class for Amplitude Shift Keying model

    Parameters
    ----------
    sampling_frec [int]: A sampling frequency of signal
    carry_frec [int]: A frequency of carry wave
    bits_num [int]: Number of bits
    symbol_rate [int]: Number of symbol changes across the transmission

    Attributes
    ----------
    time [int]: Simulation dziedzina czasu
    samp_per_bit [int]: How many samples are for one bit
    samples_num [int]: Total number of samples
    '''

    def __init__(self, sampling_frec, carry_frec, bits_num, symbol_rate):
        self.sampling_frec = sampling_frec
        self.carry_frec = carry_frec
        self.bits_num = bits_num
        self.symbol_rate = symbol_rate
        self.time = np.arange(0,2, 1/self.sampling_frec)
        self.samp_per_bit = self.sampling_frec / self.symbol_rate
        self.samples_num = self.bits_num * self.samp_per_bit

    def generateCarryWave(self):
        '''Function to generate sine carry wave
        Returns
        -------
        carry_wave [ndarray]: Carry wave signal'''
        carry_wave = np.sin(2 * np.pi * self.carry_frec * self.time)
        return carry_wave
    
    def generateSignal(self):
        '''Function to generate binary signal
        Returns
        -------
        message [ndarray]: Binary message of bit_num bits'''
        message = np.empty(self.bits_num, dtype=int)
        for i in range(self.bits_num):
            np.append(message, np.random.uniform(0, 1))
        return message

    def modulation(self, carry_wave):
        '''Function for signal modulation
        Returns
        -------
        transmited_signal [ndarray]: Signal from transmitter'''
        message = self.generateSignal()
        cont_msg = np.repeat(message, 60 * self.samp_per_bit)
        transmited_signal = carry_wave * cont_msg
        return transmited_signal

    def addNoise(self, signal):
        '''Function which add noise to the transmitted signal
        Returns
        -------
        noisy_signal [ndarray]: Signal with noise'''
        noise = np.random.normal(0, 0.1, len(signal))
        noisy_signal = signal + noise
        return noisy_signal

    def demodulation(self, signal, carry_wave):
        '''Function for signal demodulation
        Returns
        -------
        recieved_signal [ndarray]: Signal from reciever'''
        recieved_signal = np.empty(self.bits_num)
        t1 = 0
        t2 = self.samp_per_bit
        for i in range(self.bits_num):
            x = sum(carry_wave * signal[i])
            if(x > 0):
                recieved_signal[i] = 1
            else:
                recieved_signal[i] = 0
            t1 = t1 + (self.samp_per_bit + 0.01)
            t2 = t2 + (self.samp_per_bit + 0.01)           
        return recieved_signal

    def simulate(self):
        '''Function which simulates ASK modulation'''

        carry_wave = self.generateCarryWave()
        np.save('data/output/carry_wave.npy', carry_wave)
        signal = self.modulation(carry_wave)
        np.save('data/output/signal.npy', signal)
        noisy_signal = self.addNoise(signal)
        np.save('data/output/noisy_signal.npy', noisy_signal)
        recieved_signal = self.demodulation(noisy_signal, carry_wave)
        np.save('data/output/recieved_signal.npy', recieved_signal)
        
        