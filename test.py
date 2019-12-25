#!/usr/bin/env python3

from tone import Tone
from tones import Tones


Tone.dtmf_1().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_1.wav')
Tone.dtmf_2().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_2.wav')
Tone.dtmf_3().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_3.wav')
Tone.dtmf_4().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_4.wav')
Tone.dtmf_5().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_5.wav')
Tone.dtmf_6().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_6.wav')
Tone.dtmf_7().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_7.wav')
Tone.dtmf_8().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_8.wav')
Tone.dtmf_9().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_9.wav')
Tone.dtmf_0().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_0.wav')
Tone.dtmf_star().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_star.wav')
Tone.dtmf_pound().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_pound.wav')
Tone.dtmf_a().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_a.wav')
Tone.dtmf_b().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_b.wav')
Tone.dtmf_c().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_c.wav')
Tone.dtmf_d().generate_to_wavefile_path('./generated_dtmf/8000/dtmf_d.wav')
Tone.pure_1000().generate_to_wavefile_path('./generated_pure_tones/8000/1000.wav')
Tone.dtmf_string('1').generate_to_wavefile_path('./generated_dtmf/8000/dtmf_1.wav')
Tones.dtmf_string('*##').generate_to_wavefile_path('./generated_dtmf/8000/dtmf_star_pound_pound.wav')

for sampling_rate in [16000, 32000, 44100, 48000]:
    Tone.dtmf_1().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_1.wav', sampling_rate=sampling_rate)
    Tone.dtmf_2().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_2.wav', sampling_rate=sampling_rate)
    Tone.dtmf_3().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_3.wav', sampling_rate=sampling_rate)
    Tone.dtmf_4().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_4.wav', sampling_rate=sampling_rate)
    Tone.dtmf_5().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_5.wav', sampling_rate=sampling_rate)
    Tone.dtmf_6().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_6.wav', sampling_rate=sampling_rate)
    Tone.dtmf_7().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_7.wav', sampling_rate=sampling_rate)
    Tone.dtmf_8().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_8.wav', sampling_rate=sampling_rate)
    Tone.dtmf_9().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_9.wav', sampling_rate=sampling_rate)
    Tone.dtmf_0().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_0.wav', sampling_rate=sampling_rate)
    Tone.dtmf_star().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_star.wav', sampling_rate=sampling_rate)
    Tone.dtmf_pound().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_pound.wav', sampling_rate=sampling_rate)
    Tone.dtmf_a().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_a.wav', sampling_rate=sampling_rate)
    Tone.dtmf_b().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_b.wav', sampling_rate=sampling_rate)
    Tone.dtmf_c().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_c.wav', sampling_rate=sampling_rate)
    Tone.dtmf_d().generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_d.wav', sampling_rate=sampling_rate)
    Tone.pure_1000().generate_to_wavefile_path(f'./generated_pure_tones/{sampling_rate}/1000.wav', sampling_rate=sampling_rate)
    Tone.dtmf_string('1').generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_1.wav', sampling_rate=sampling_rate)
    Tones.dtmf_string('*##').generate_to_wavefile_path(f'./generated_dtmf/{sampling_rate}/dtmf_star_pound_pound.wav', sampling_rate=sampling_rate)

