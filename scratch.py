#!/usr/bin/env python3

from math import sin
from math import pi
import wave

sampling_rate = 8000
time = 0.25
post_tone_silence_time = 0.25
alternations = 1
attenuation_db = 0.0
attenuation_multiplier = 10**((-1*attenuation_db)/20)

# PURE TONE
frequency = 1000

wavefile = wave.open('foo.wav', 'w')
wavefile.setnchannels(1)
wavefile.setsampwidth(2)
wavefile.setframerate(sampling_rate)

sample_index_multiplier = frequency / sampling_rate * pi * 2
for _ in range(0, alternations):
    for sample_index in range(0,int(sampling_rate * time)):
        sample = sin(sample_index_multiplier * sample_index) * attenuation_multiplier
        sample_integer = int(sample * (2**15-1))
        print(f"{sample_index} - {sample} - {sample_integer}")
        wavefile.writeframes(sample_integer.to_bytes(2, byteorder='little', signed=True))
    for sample_index in range(0,int(sampling_rate * post_tone_silence_time)):
        wavefile.writeframes(b'\0\0')
wavefile.close()

# DTMF 1
frequency1 = 1209
frequency2 = 697

wavefile = wave.open('bar.wav', 'w')
wavefile.setnchannels(1)
wavefile.setsampwidth(2)
wavefile.setframerate(sampling_rate)

sample_index_multiplier1 = frequency1 / sampling_rate * pi * 2
sample_index_multiplier2 = frequency2 / sampling_rate * pi * 2
for _ in range(0, alternations):
    for sample_index in range(0,int(sampling_rate * time)):
        sample = (sin(sample_index_multiplier1 * sample_index) * 0.5 + sin(sample_index_multiplier2 * sample_index) * 0.5) * attenuation_multiplier
        sample_integer = int(sample * (2**15-1))
        print(f"{sample_index} - {sample} - {sample_integer}")
        wavefile.writeframes(sample_integer.to_bytes(2, byteorder='little', signed=True))
    for sample_index in range(0,int(sampling_rate * post_tone_silence_time)):
        wavefile.writeframes(b'\0\0')
wavefile.close()
