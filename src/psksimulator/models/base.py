# -*- coding: utf-8 -*-
"""
    This file contains code for base simulation model
"""

from abc import ABC, abstractmethod
import numpy as np


class _BaseModulationModel(ABC):
    ''' Class for Base Modulation Model

    Parameters
    ----------
    sampling_frec [int]: A sampling frequency of signal
    carry_frec [int]: A frequency of carry wave
    bits_num [int]: Number of bits
    noise [float64]: A standard deviation of random noise. Must be non-negative

    Attributes
    ----------
    time [ndarray]: Simulation time domain
    '''

    def __init__(self, sampling_frec, carry_frec, bits_num, noise):
        self.sampling_frec = sampling_frec
        self.carry_frec = carry_frec
        self.bits_num = bits_num
        self.noise = noise
        self.time = np.linspace(0, 1, sampling_frec)

    def set_noise(self, value):
        self.noise = value

    @abstractmethod
    def get_modulation_name():
        '''Function which returns modulation name'''


    def _generate_signal(self):
        ''' Function to generate binary signal

        Returns
        -------
        message [ndarray]: Binary message of bit_num bit
        '''

        message = np.random.randint(2, size=self.bits_num)
        return message


    def _add_noise(self, signal):
        '''Function which add noise to the transmitted signal

        
        Returns
        -------
        noisy_signal [ndarray]: Signal with noise
        '''

        noises = np.random.normal(0, self.noise, len(signal))
        noisy_signal = signal + noises
        return noisy_signal


    @abstractmethod
    def _generate_carry_waves(self):
        '''Function to generate sine carry wave

        Returns
        -------
        carry_wave [ndarray]: Carry wave signal
        '''
        pass


    @abstractmethod
    def _modulation(self, message, carry_waves):
        '''Function for signal modulation

        Returns
        -------
        transmitted_signal [ndarray]: Signal from transmitter
        '''
        pass


    @abstractmethod
    def _demodulation(self, signal, carry_waves):
        '''Function for signal demodulation

        Returns
        -------
        received_message [ndarray]: Message from receiver
        '''
        pass


    def run(self):
        '''Function which runs simulation model
        
        Returns
        -------
        signals [dict]: Dictionary of simulation signals
        '''

        carry_waves = self._generate_carry_waves()
        message = self._generate_signal()
        signal = self._modulation(message, carry_waves)
        noisy_signal = self._add_noise(signal)
        received_signal = self._demodulation(noisy_signal, carry_waves)

        return { 'message'  : message,
                 'signal'   : signal,
                 'noises'   : noisy_signal,
                 'received' : received_signal }
