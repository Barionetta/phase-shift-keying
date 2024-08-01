# -*- coding: utf-8 -*-
"""
    This module contains simulation methods
"""
import numpy as np
from dataclasses import dataclass
import csv


@dataclass
class Simulation:
    sampling_frec: int
    carry_frec: int
    bits_num: int
    noise: float


def calculateBER(bits_num : int, original_message : np.ndarray, received_message : np.ndarray) -> float:
    '''Function to calculate Bit Error Rate (BER)

    Returns
    -------
    ber [float] : Bit Error Rate
    '''

    errors = np.sum(original_message != received_message)
    ber = errors / bits_num
    return ber


def save_to_csv(model : str, simulation : Simulation, float_data : float, EbNodB : int):
    '''Function which save statistics from simulation to bers.csv file'''
    with open('data/output/bers.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([model, simulation.sampling_frec, simulation.carry_frec, simulation.bits_num,
                        np.round(simulation.noise, 1), float_data, EbNodB])