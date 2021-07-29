#!/usr/bin/env python3

from tone import Tone
from tones import Tones
from os import makedirs
from os.path import exists


regenerate = False
demo_tone_duration = 10.0

def generate_dtmf(dtmf_string, path, attenuation_db=0, duration=0.25, silence_duration=0.25, sampling_rate=8000, sample_width=2, number_of_channels=1):
    if regenerate or (not exists(path)):
        Tones.dtmf_string(dtmf_string, attenuation_db=attenuation_db, duration=duration, silence_duration=silence_duration).generate_to_wavefile_path(path, sampling_rate=sampling_rate, sample_width=sample_width, number_of_channels=number_of_channels)

def generate_mf(mf_string, path, attenuation_db=0, duration=0.25, silence_duration=0.25, sampling_rate=8000, sample_width=2, number_of_channels=1):
    if regenerate or (not exists(path)):
        Tone.mf_string(mf_string, attenuation_db=attenuation_db, duration=duration, silence_duration=silence_duration).generate_to_wavefile_path(path, sampling_rate=sampling_rate, sample_width=sample_width, number_of_channels=number_of_channels)

def generate_pure_tone(frequency, path, attenuation_db=0, duration=0.25, silence_duration=0.25, sampling_rate=8000, sample_width=2, number_of_channels=1):
    if regenerate or (not exists(path)):
        Tone.pure_tone(frequency, attenuation_db=attenuation_db, duration=duration, silence_duration=silence_duration).generate_to_wavefile_path(path, sampling_rate=sampling_rate, sample_width=sample_width, number_of_channels=number_of_channels)

for sampling_rate in [8000, 16000, 32000, 44100, 48000]:
    makedirs(f'./generated_dtmf/{sampling_rate}', exist_ok=True)
    for dtmf_string in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd']:
        generate_dtmf(dtmf_string, f'./generated_dtmf/{sampling_rate}/dtmf_{dtmf_string}.wav', sampling_rate=sampling_rate)
    generate_dtmf('*', f'./generated_dtmf/{sampling_rate}/dtmf_star.wav', sampling_rate=sampling_rate)
    generate_dtmf('#', f'./generated_dtmf/{sampling_rate}/dtmf_pound.wav', sampling_rate=sampling_rate)
    generate_dtmf('*##', f'./generated_dtmf/{sampling_rate}/dtmf_star_pound_pound.wav', sampling_rate=sampling_rate)
    generate_dtmf('**#', f'./generated_dtmf/{sampling_rate}/dtmf_star_star_pound.wav', sampling_rate=sampling_rate)
    makedirs(f'./generated_mf/{sampling_rate}', exist_ok=True)
    for mf_string in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'kp', 'kp2', 'st']:
        generate_mf(mf_string, f'./generated_mf/{sampling_rate}/mf_{mf_string}.wav', sampling_rate=sampling_rate)
    makedirs(f'./generated_pure_tones/{sampling_rate}', exist_ok=True)
    for frequency in [600]:
        generate_pure_tone(frequency, f'./generated_pure_tones/{sampling_rate}/{frequency}.wav', sampling_rate=sampling_rate)

makedirs(f'./generated_dtmf_for_demo', exist_ok=True)
for dtmf_string in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd']:
    generate_dtmf(dtmf_string, f'./generated_dtmf_for_demo/dtmf_{dtmf_string}.wav', sampling_rate=48000, duration=demo_tone_duration, silence_duration=0.0)
generate_dtmf('*', f'./generated_dtmf_for_demo/dtmf_star.wav', sampling_rate=48000, duration=demo_tone_duration, silence_duration=0.0)
generate_dtmf('#', f'./generated_dtmf_for_demo/dtmf_pound.wav', sampling_rate=48000, duration=demo_tone_duration, silence_duration=0.0)
makedirs(f'./generated_mf_for_demo', exist_ok=True)
for mf_string in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'kp', 'kp2', 'st']:
    generate_mf(mf_string, f'./generated_mf_for_demo/mf_{mf_string}.wav', sampling_rate=48000, duration=demo_tone_duration, silence_duration=0.0)
makedirs(f'./generated_pure_tones_for_demo', exist_ok=True)
for frequency in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000]:
    generate_pure_tone(frequency, f'./generated_pure_tones_for_demo/{frequency}.wav', sampling_rate=48000, duration=demo_tone_duration, silence_duration=0.0)

