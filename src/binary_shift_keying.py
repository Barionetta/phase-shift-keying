# -*- coding: utf-8 -*-
"""
    This file contains BPSK modulation model
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import numpy as np

class BPKS:
    ''' Class for Binary Phase Shift Keying model

    Parameters
    ----------
    sampling_frec [int]: A sampling frequency of signal
    carry_frec [int]: A frequency of carry wave
    bits_num [int]: Number of bits
    noise [float64]: A standard deviation of random noise. Must be non-negative

    Attributes
    ----------
    time [ndarray]: Simulation time domain
    samp_per_bit [int]: How many samples are for one bit
    '''

    def __init__(self, sampling_frec, carry_frec, bits_num, noise):
        self.sampling_frec = sampling_frec
        self.carry_frec = carry_frec
        self.bits_num = bits_num
        self.noise = noise
        self.time = np.linspace(0, 1, sampling_frec)
        self.samp_per_bit = int(sampling_frec / bits_num)


    def generateCarryWave(self):
        ''''Function to generate four carry waves
        Returns
        -------
        carry_waves [list]: A list of ndarrays of carry waves'''
        carry_waves = []
        carry_zeros = np.cos(2 * np.pi * self.carry_frec * self.time)
        carry_ones = np.cos(2 * np.pi * self.carry_frec * self.time + np.pi)
        carry_waves.append(carry_zeros)
        carry_waves.append(carry_ones)
        return carry_waves
    
    def generateSignal(self):
        '''Function to generate binary signal
        Returns
        -------
        message [ndarray]: Binary message of bit_num bits'''
        message = np.random.randint(2, size=self.bits_num)
        return message
    
    def modulation(self, message, carry_zeros, carry_ones):
        '''Function for signal modulation
        Returns
        -------
        transmited_signal [ndarray]: Signal from transmitter'''
        cont_msg = np.repeat(message, self.samp_per_bit)
        transmitted_signal = []
        for i in range(0, cont_msg.size, 2):
            if(cont_msg[i] == 0):
                transmitted_signal.append(carry_zeros[i])
            elif(cont_msg[i] == 1):
                transmitted_signal.append(carry_ones[i])      
        transmitted_signal = np.asarray(transmitted_signal)
        return transmitted_signal

    def addNoise(self, signal):
        '''Function which add noise to the transmitted signal
        Returns
        -------
        noisy_signal [ndarray]: Signal with noise'''
        noise = np.random.normal(0, self.noise, len(signal))
        noisy_signal = signal + noise
        return noisy_signal

    def demodulation(self, signal):
        '''Function for signal demodulation
        Returns
        -------
        recieved_message [ndarray]: Message from reciever'''
        recieved_signal = []
        bits_signals = np.split(signal, self.bits_num)
        for bit_signal in bits_signals:
            phase = np.angle(np.ftt.ftt(bit_signal), deg=True)
            if(phase == 0):
                recieved_signal.append(0)
            elif(phase == 180.0):
                recieved_signal.append(1)
        recieved_signal.reverse()
        recieved_signal = np.asarray(recieved_signal)
        return recieved_signal

    def simulate(self):
        '''Function which simulates BPSK modulation'''

        carry_waves = self.generateCarryWave()
        message = self.generateSignal()
        np.save('data/output/BPSK/message.npy', message)
        signal = self.modulation(message, carry_waves[0], carry_waves[1])
        np.save('data/output/BPSK/signal.npy', signal)
        noisy_signal = self.addNoise(signal)
        np.save('data/output/BPSK/noisy_signal.npy', noisy_signal)
        recieved_signal = self.demodulation(noisy_signal)
        np.save('data/output/BPSK/recieved_signal.npy', recieved_signal)