# -*- coding: utf-8 -*-
"""
    This file contains functions for signal modulations
"""
import numpy as np


def ASK_modulation(samp_per_bit : int, message : np.ndarray, carry_wave : np.ndarray) -> np.ndarray:
    '''Function for signal ASK modulation

    Returns
    -------
    transmitted_signal [ndarray]: Signal from transmitter
    '''

    cont_msg = np.repeat(message, samp_per_bit)
    transmited_signal = carry_wave * cont_msg
    return transmited_signal


def ASK_demodulation(sampling_frec : int, bits_num : int, samp_per_bit: int, signal : np.ndarray) -> np.ndarray:
    '''Function for signal ASK demodulation

    Returns
    -------
    received_message [ndarray]: Message from receiver
    '''

    recieved_signal = np.zeros(sampling_frec)
    signal = np.absolute(signal)
    for i in range(sampling_frec):
        if(signal[i] > 0.4):
            recieved_signal[i] = 1
        else:
            recieved_signal[i] = 0
    splited = np.split(recieved_signal, bits_num)
    recieved_message = []
    for array in splited:
        arr_sum = np.sum(array)
        if(arr_sum > (samp_per_bit/2)):
            recieved_message.append(1)
        else:
            recieved_message.append(0)
    recieved_message = np.asarray(recieved_message)
    return recieved_message


def BPSK_modulation(message : np.ndarray, carry_wave : np.ndarray) -> np.ndarray:
    '''Function for signal BPSK modulation

    Returns
    -------
    transmitted_signal [ndarray]: Signal from transmitter
    '''

    transmitted_signal = np.copy(carry_wave)
    for i in range(len(message)):
        if(message[i] == 1):
            transmitted_signal[i] = -1 * transmitted_signal[i]
    transmitted_signal = np.ravel(transmitted_signal)
    return transmitted_signal


def BPSK_demodulation(bits_num : int, signal : np.ndarray, carry_wave : np.ndarray) -> np.ndarray:
    '''Function for signal BPSK demodulation

    Returns
    -------
    received_message [ndarray]: Message from receiver
    '''

    received_signal = np.arange(bits_num)
    signal = np.split(signal, bits_num)
    for i in range(len(signal)):
        phase = np.sum(signal[i] * carry_wave[i])
        if(phase > 0):
            bit = 0
        else:
            bit = 1
        received_signal[i] = bit
    received_signal = np.asarray(received_signal)
    return received_signal


def QPSK_modulation(message : np.ndarray, carry_waves : list) -> np.ndarray:
    '''Function for signal QPSK modulation

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


def QPSK_demodulation(bits_num : int, signal : np.ndarray, carry_waves : list) -> np.ndarray:
    '''Function for signal QPSK demodulation

    Returns
    -------
    received_message [ndarray]: Message from receiver
    '''

    carry_i = carry_waves[0]
    carry_q = carry_waves[1]

    received_signal = np.arange(bits_num)
    signal = np.split(signal, bits_num/2)
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