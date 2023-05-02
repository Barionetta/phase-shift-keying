# -*- coding: utf-8 -*-
"""
    This module contains simulation methods
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

import pandas as pd
import seaborn as sns
from src import amplitude_shift_keying
#import binary_shift_keying
#import quadrature_shift_keying


def run():
    ask_model = amplitude_shift_keying.ASK(44100, 1800, 10, 300)
    ask_model.simulate()

