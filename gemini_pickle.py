#!/home/samhaug/anaconda2/bin/python

'''
==============================================================================

File Name : gemini_pickle.py
Purpose : convert Ascii gemini output to pickle file
Creation Date : 05-07-2017
Last Modified : Wed 05 Jul 2017 08:56:07 PM EDT
Created By : Samuel M. Haugland

==============================================================================
'''

import numpy as np
from matplotlib import pyplot as plt
from subprocess import call
from os import listdir
import h5py
import obspy
import seispy

def main():

def read_station_list(statfile):
    '''Needs list of stations AKA gemini station input file'''
    f = open(statfile,'r').read().strip().split('\n')
    return f[2::]

def read_cmtfile(momfile):
    '''Needs gemini moment tensor input file'''

def read_ascii_seis(asciiseis):
    '''Needs Ascii seismogram output file'''

main()
