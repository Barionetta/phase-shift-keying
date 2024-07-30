# -*- coding: utf-8 -*-
"""
    This file contains BPSK modulation model
"""

import numpy as np

from psksimulator.models.base import _BaseModulationModel


class BPSKModel(_BaseModulationModel):
    ''' Class for Binary Phase Shift Keying model

    Attributes
    ----------
    samp_per_bit [int]: How many samples are for one bit
    '''

    def __init__(self, sampling_frec, carry_frec, bits_num, noise):
        super().__init__(
            sampling_frec=sampling_frec,
            carry_frec=carry_frec,
            bits_num=bits_num,
            noise=noise
        )
        self.samp_per_bit = int(sampling_frec / bits_num)


    def get_modulation_name():
        '''Function which returns modulation name'''
        return "BPSK"


    def _generate_carry_waves(self):
        '''Function to generate carry waves

        Returns
        -------
        carry_waves [list]: A list of ndarrays of carry waves
        '''
        
        carry_waves = []
        carry_wave = np.sin(2 * np.pi * self.carry_frec * self.time)
        carry_wave = np.split(carry_wave, self.bits_num)
        carry_waves.append(carry_wave)
        return carry_waves


    def _modulation(self, message, carry_waves):
        '''Function for signal modulation

        Returns
        -------
        transmitted_signal [ndarray]: Signal from transmitter
        '''

        transmitted_signal = np.copy(carry_waves[0])
        for i in range(len(message)):
            if(message[i] == 1):
                transmitted_signal[i] = -1 * transmitted_signal[i]
        transmitted_signal = np.ravel(transmitted_signal)
        return transmitted_signal


    def _demodulation(self, signal, carry_waves):
        '''Function for signal demodulation

        Returns
        -------
        received_message [ndarray]: Message from receiver
        '''
        
        received_signal = np.arange(self.bits_num)
        signal = np.split(signal, self.bits_num)
        for i in range(len(signal)):
            phase = np.sum(signal[i] * carry_waves[0][i])
            if(phase > 0):
                bit = 0
            else:
                bit = 1
            received_signal[i] = bit
        received_signal = np.asarray(received_signal)
        return received_signal
