# -*- coding: utf-8 -*-
"""
    This file contains ASK modulation model
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import numpy as np
import csv

class ASK:
    ''' Class for Amplitude Shift Keying model

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
        transmited_signal [ndarray]: Signal from transmitter'''
        cont_msg = np.repeat(message, self.samp_per_bit)
        transmited_signal = carry_wave * cont_msg
        return transmited_signal

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
        recieved_signal = np.zeros(self.sampling_frec)
        signal = np.absolute(signal)
        for i in range(self.sampling_frec):
            if(signal[i] > 0.4):
                recieved_signal[i] = 1
            else:
                recieved_signal[i] = 0
        splited = np.split(recieved_signal, self.bits_num)
        recieved_message = []
        for array in splited:
            arr_sum = np.sum(array)
            if(arr_sum > (self.samp_per_bit/2)):
                recieved_message.append(1)
            else:
                recieved_message.append(0)
        recieved_message = np.asarray(recieved_message)
        return recieved_message
    
    def calculateBER(self, original_message, received_message):
        '''Function to calculate Bit Error Rate (BER)
        Returns
        -------
        ber [float]: Bit Error Rate'''
        errors = np.sum(original_message != received_message)
        ber = errors / self.bits_num
        return ber
    def save_to_csv(self, file_path, float_data):
        # Open the CSV file in 'write' mode with semicolon delimiter
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
                
            # Write the header row
            writer.writerow(['ASK', 'BER', 'Sampling Frec', 'Carry Frec', 'Bits Num', 'Noise'])
                
            # Write the data row
            writer.writerow(['', float_data, self.sampling_frec, self.carry_frec, self.bits_num, self.noise])
            
    def simulate(self):
        '''Function which simulates ASK modulation'''

        carry_wave = self.generateCarryWave()
        np.save('data/output/ASK/carry_wave.npy', carry_wave)
        message = self.generateSignal()
        np.save('data/output/ASK/message.npy', message)
        signal = self.modulation(message, carry_wave)
        np.save('data/output/ASK/signal.npy', signal)
        noisy_signal = self.addNoise(signal)
        np.save('data/output/ASK/noisy_signal.npy', noisy_signal)
        received_signal = self.demodulation(noisy_signal)
        np.save('data/output/ASK/received_signal.npy', received_signal)
        ber = self.calculateBER(message,received_signal)
        self.save_to_csv('data/output/ASK/ber.csv', ber)
        
        