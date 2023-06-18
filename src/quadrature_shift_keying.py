# -*- coding: utf-8 -*-
"""
    This file contains QPSK modulation model
"""
__version__ = '0.1.2'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import numpy as np
import csv

class QPSK:
    ''' Class for Quadrature Phase Shift Keying model

    Parameters
    ----------
    sampling_frec [int]: A sampling frequency of signal
    carry_frec [int]: A frequency of carry wave
    bits_num [int]: Number of bits
    noise [float64]: A standard deviation of random noise. Must be non-negative

    Attributes
    ----------
    time [ndarray]: Simulation time domain
    samp_per_symbol [int]: How many samples are for one symbol (for QPSK one symbol contains two bits)
    '''

    def __init__(self, sampling_frec, carry_frec, bits_num, noise):
        self.sampling_frec = sampling_frec
        self.carry_frec = carry_frec
        self.bits_num = bits_num
        self.noise = noise
        self.time = np.linspace(0, 1, sampling_frec)
        self.samp_per_symbol = int(sampling_frec / (bits_num/2))

    def generateCarryWave(self):
        '''Function to generate carry waves
        Returns
        -------
        carry_waves [list]: A list of ndarrays of carry waves'''
        carry_i = np.cos(2 * np.pi * self.carry_frec * self.time)
        carry_q = np.sin(2 * np.pi * self.carry_frec * self.time)
        carry_i = np.split(carry_i, self.bits_num/2)
        carry_q = np.split(carry_q, self.bits_num/2)
        carry_waves = [carry_i, carry_q]
        return carry_waves
    
    def generateSignal(self):
        '''Function to generate binary signal
        Returns
        -------
        message [ndarray]: Binary message of bit_num bits'''
        message = np.random.randint(2, size=self.bits_num)
        return message

    def modulation(self, message, carry_i, carry_q):
        '''Function for signal modulation
        Returns
        -------
        transmitted_signal [ndarray]: Signal from transmitter'''
        trans_i = np.copy(carry_i)
        trans_q = np.copy(carry_q)
        for i in range(len(carry_i)):
            if (message[2*i] == 0):
                q_sing = 1
            else:
                q_sing = -1
            if (message[2*i+1] == 0):
                i_sing = 1
            else:
                i_sing = -1
            trans_i[i] = i_sing * trans_i[i]
            trans_q[i] = q_sing * trans_q[i]
        trans_i = np.ravel(trans_i)
        trans_q = np.ravel(trans_q)
        transmitted_signal = trans_i + trans_q
        return transmitted_signal
        
    def addNoise(self, signal):
        '''Function which add noise to the transmitted signal
        Returns
        -------
        noisy_signal [ndarray]: Signal with noise'''
        noise = np.random.normal(0, self.noise, len(signal))
        noisy_signal = signal + noise
        return noisy_signal

    def demodulation(self, signal, carry_i, carry_q):
        '''Function for signal demodulation
        Returns
        -------
        received_message [ndarray]: Message from receiver'''
        received_signal = np.arange(self.bits_num)
        signal = np.split(signal, self.bits_num/2)
        for i in range(len(signal)):
            in_phase = np.sum(signal[i] * carry_i[i])
            quadrature = np.sum(signal[i] * carry_q[i])
            if(in_phase > 0):
                q_bit = 0
            else:
                q_bit = 1
            if(quadrature > 0):
                i_bit = 0
            else:
                i_bit = 1
            received_signal[2*i] = i_bit
            received_signal[2*i+1] = q_bit
        received_signal = np.asarray(received_signal)
        return received_signal
    
    def calculateBER(self, original_message, received_message):
        '''Function to calculate Bit Error Rate (BER)
        Returns
        -------
        ber [float]: Bit Error Rate'''
        errors = np.sum(original_message != received_message)
        ber = errors / self.bits_num
        return ber
    
    def save_to_csv(self, float_data, EbNodB):
        '''Function which save statistics from simulation to bers.csv file'''
        with open('data/output/bers.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['QPSK', self.sampling_frec, self.carry_frec, self.bits_num, np.round(self.noise, 1), float_data, EbNodB])

    def one_run(self, EbNodB):
        '''Function which simulates one QPSK modulation'''
        carry_waves = self.generateCarryWave()
        message = self.generateSignal()
        signal = self.modulation(message, carry_waves[0], carry_waves[1])
        noisy_signal = self.addNoise(signal)
        received_signal = self.demodulation(noisy_signal, carry_waves[0], carry_waves[1])
        ber = self.calculateBER(message,received_signal)
        self.save_to_csv(ber, EbNodB)

    def demo_run(self):
        '''Function which demonstrate QPSK modulation'''
        carry_waves = self.generateCarryWave()
        message = self.generateSignal()
        np.save('data/output/QPSK/message.npy', message)
        signal = self.modulation(message, carry_waves[0], carry_waves[1])
        np.save('data/output/QPSK/signal.npy', signal)
        noisy_signal = self.addNoise(signal)
        np.save('data/output/QPSK/noisy_signal.npy', noisy_signal)
        received_signal = self.demodulation(noisy_signal, carry_waves[0], carry_waves[1])
        np.save('data/output/QPSK/received_signal.npy', received_signal)

    def simulate(self):
        '''Function which simulates many QPSK modulations.'''
        for n in range(12):
            EbNo = 10.0**(n/10.0)
            self.noise = 1/np.sqrt(2*EbNo)*4
            self.one_run(n)
        print("Koniec symulacji modulacji QPSK") 