# -*- coding: utf-8 -*-
"""
    This file contains QPSK modulation model
"""

import numpy as np

from psksimulator.models.base import _BaseModulationModel


class QPSKModel(_BaseModulationModel):
    ''' Class for Quadrature Phase Shift Keying model

    Attributes
    ----------
    samp_per_symbol [int]: How many samples are for one symbol (for QPSK one symbol contains two bits)
    '''

    def __init__(self, sampling_frec, carry_frec, bits_num, noise):
        super().__init__(
            sampling_frec=sampling_frec,
            carry_frec=carry_frec,
            bits_num=bits_num,
            noise=noise
        )
        self.samp_per_symbol = int(sampling_frec / (bits_num/2))


    def get_modulation_name():
        '''Function which returns modulation name'''
        return "QPSK"


    def _generate_carry_waves(self):
        '''Function to generate carry waves

        Returns
        -------
        carry_waves [list]: A list of ndarrays of carry waves
        '''

        carry_i = np.cos(2 * np.pi * self.carry_frec * self.time)
        carry_q = np.sin(2 * np.pi * self.carry_frec * self.time)
        carry_i = np.split(carry_i, self.bits_num/2)
        carry_q = np.split(carry_q, self.bits_num/2)
        carry_waves = [carry_i, carry_q]
        return carry_waves


    def _modulation(self, message, carry_waves):
        '''Function for signal modulation

        Returns
        -------
        transmitted_signal [ndarray]: Signal from transmitter
        '''

        trans_i = np.copy(carry_waves[0])
        trans_q = np.copy(carry_waves[1])

        for i in range(len(carry_waves[0])):
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


    def _demodulation(self, signal, carry_waves):
        '''Function for signal demodulation

        Returns
        -------
        received_message [ndarray]: Message from receiver
        '''

        carry_i = carry_waves[0]
        carry_q = carry_waves[1]

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