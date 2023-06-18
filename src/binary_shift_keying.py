# -*- coding: utf-8 -*-
"""
    This file contains BPSK modulation model
"""
__version__ = '0.1.2'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import numpy as np
import csv

class BPSK:
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
        '''Function to generate sine carry wave
        Returns
        -------
        carry_wave [ndarray]: Carry wave signal'''
        carry_wave = np.sin(2 * np.pi * self.carry_frec * self.time)
        carry_wave = np.split(carry_wave, self.bits_num)
        return carry_wave
    
    def generateSignal(self):
        '''Function to generate binary signal
        Returns
        -------
        message [ndarray]: Binary message of bit_num bits'''
        message = np.random.randint(2, size=self.bits_num)
        return message
    
    def modulation(self, message, carry_wave):
        '''Function for signal modulation
        Returns
        -------
        transmitted_signal [ndarray]: Signal from transmitter'''
        transmitted_signal = np.copy(carry_wave)
        for i in range(len(message)):
            if(message[i] == 1):
                transmitted_signal[i] = -1 * transmitted_signal[i]
        transmitted_signal = np.ravel(transmitted_signal)
        return transmitted_signal

    def addNoise(self, signal):
        '''Function which adds noise to the transmitted signal
        Returns
        -------
        noisy_signal [ndarray]: Signal with noise'''
        noise = np.random.normal(0, self.noise, len(signal))
        noisy_signal = signal + noise
        return noisy_signal

    def demodulation(self, signal, carry_wave):
        '''Function for signal demodulation
        Returns
        -------
        received_message [ndarray]: Message from receiver'''
        received_signal = np.arange(self.bits_num)
        signal = np.split(signal, self.bits_num)
        for i in range(len(signal)):
            phase = np.sum(signal[i] * carry_wave[i])
            if(phase > 0):
                bit = 0
            else:
                bit = 1
            received_signal[i] = bit
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
            writer.writerow(['BPSK', self.sampling_frec, self.carry_frec, self.bits_num, np.round(self.noise, 1), float_data, EbNodB])

    def one_run(self, EbNodB):
        '''Function which simulates one BPSK modulation'''
        carry_wave = self.generateCarryWave()
        message = self.generateSignal()
        signal = self.modulation(message, carry_wave)
        noisy_signal = self.addNoise(signal)
        received_signal = self.demodulation(noisy_signal, carry_wave)
        ber = self.calculateBER(message,received_signal)
        self.save_to_csv(ber, EbNodB)

    def demo_run(self):
        '''Function which demonstrate BPSK modulation'''
        carry_wave = self.generateCarryWave()
        message = self.generateSignal()
        np.save('data/output/BPSK/message.npy', message)
        signal = self.modulation(message, carry_wave)
        np.save('data/output/BPSK/signal.npy', signal)
        noisy_signal = self.addNoise(signal)
        np.save('data/output/BPSK/noisy_signal.npy', noisy_signal)
        received_signal = self.demodulation(noisy_signal, carry_wave)
        np.save('data/output/BPSK/received_signal.npy', received_signal)

    def simulate(self):
        '''Function which simulates many BPSK modulations.'''
        for n in range(12):
            EbNo = 10.0**(n/10.0)
            self.noise = 1/np.sqrt(2*EbNo)*4
            self.one_run(n)
        print("Koniec symulacji modulacji BPSK") 
        