import scipy.io.wavfile as wavfile
import IPython
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

def sound( x, rate=8000, label=''):
	"""
	display one sound track

	Args:
		x: input sound
		rate: rate of the sound
		label: comment for this audio
	"""
    from IPython.display import display, Audio, HTML
    if label is '':
        display( Audio( x, rate=rate))
    else:
        display( HTML( 
        '<style> table, th, td {border: 0px; }</style> <table><tr><td>' + label + 
        '</td><td>' + Audio( x, rate=rate)._repr_html_()[3:] + '</td></tr></table>'
        ))

def compressor():
	pass

def EQ_effect_box(input_sound,gains,fs):
	"""
	EQ effect box
	It can boost or suppress certain frequency. Here I use 5-element vector for boosting or suppressing 80Hz,240Hz,2500Hz,3750Hz,5000Hz.

	Args:
		input_sound: input audio
		gains: 5-element vector for frequency of (80,240,2500,3750,5000)
		fs: frequency of the sound

	Returns:
		audio after applying EQ_effect_box
	"""

    freq = [0.0, 80/fs, 240/fs, 2500/fs, 3750/fs, 5000/fs, 1.0]
    gain = [1.0] + gains + [1.0]
    filter_ = signal.firwin2(1001, freq, gain, nfreqs=None, window='hamming')
    return signal.convolve(input_sound,filter_)


def overdrive():
	pass

def chrous():
	pass

def reverb():
	pass

def wah_wah_pedal():
	pass

def tremolo():
	pass

def acoustic_simulator():
	pass

def electric_simulator():
	pass

def noise gate():
	pass

