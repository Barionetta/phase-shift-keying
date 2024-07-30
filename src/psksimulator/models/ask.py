# -*- coding: utf-8 -*-
"""
    This file contains ASK modulation model
"""

import numpy as np

from psksimulator.models.base import _BaseModulationModel


class ASKModel(_BaseModulationModel):
    ''' Class for Amplitude Shift Keying model

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
        return "ASK"


    def _generate_carry_waves(self):
        '''Function to generate sine carry wave

        Returns
        -------
        carry_waves [list]: Carry waves signals
        '''

        carry_waves = []
        carry_waves.append(np.sin(2 * np.pi * self.carry_frec * self.time))
        return carry_waves
    
    def _modulation(self, message, carry_waves):
        '''Function for signal modulation

        Returns
        -------
        transmitted_signal [ndarray]: Signal from transmitter
        '''

        cont_msg = np.repeat(message, self.samp_per_bit)
        transmited_signal = carry_waves[0] * cont_msg
        return transmited_signal

    def _demodulation(self, signal, carry_waves):
        '''Function for signal demodulation

        Returns
        -------
        received_message [ndarray]: Message from receiver
        '''

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