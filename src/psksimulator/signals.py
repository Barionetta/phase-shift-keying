# -*- coding: utf-8 -*-
"""
    This file contains functions for generating signals
"""
import numpy as np


def generate_signal(bits_num : int) -> np.ndarray:
    ''' Function to generate binary signal

    Returns
    -------
    message [ndarray] : Binary message of bit_num bit
    '''

    message = np.random.randint(2, size=bits_num)
    return message


def add_noise(noise : float, signal : np.ndarray) -> np.ndarray:
    '''Function which add noise to the transmitted signal

    Returns
    -------
    noisy_signal [ndarray] : Signal with noise
    '''

    noises = np.random.normal(0, noise, len(signal))
    noisy_signal = signal + noises
    return noisy_signal


def ASK_generate_carry_waves(carry_frec : int, time : np.ndarray) -> np.ndarray:
    '''Function to generate sine carry wave for ASK modulation

    Returns
    -------
    carry_waves [ndarray] : Carry waves signal
    '''

    carry_wave = np.sin(2 * np.pi * carry_frec * time)
    return carry_wave


def BPSK_generate_carry_waves(carry_frec : int, time : np.ndarray, bits_num : int) -> np.ndarray:
    '''Function to generate sine carry wave for BPSK modulation

    Returns
    -------
    carry_wave [ndarray] : Carry waves signal
    '''

    carry_wave = np.sin(2 * np.pi * carry_frec * time)
    carry_wave = np.split(carry_wave, bits_num)
    return carry_wave


def QPSK_generate_carry_waves(carry_frec : int, time : np.ndarray, bits_num : int) -> list:
    '''Function to generate carry waves

    Returns
    -------
    carry_waves [list] : A list of ndarrays of carry waves
    '''

    carry_i = np.cos(2 * np.pi * carry_frec * time)
    carry_q = np.sin(2 * np.pi * carry_frec * time)
    carry_i = np.split(carry_i, bits_num/2)
    carry_q = np.split(carry_q, bits_num/2)
    carry_waves = [carry_i, carry_q]
    return carry_waves