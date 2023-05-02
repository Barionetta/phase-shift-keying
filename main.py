# -*- coding: utf-8 -*-
"""
    This is the main file of the project
"""
__version__ = '0.1.0'
__author__ = 'Katarzyna Matuszek, Miłosz Siemiński'

from src import simulation

def main():
    print("Phase Shift Keying Project")
    simulation.run()
    

if __name__ == "__main__":
    main()
    