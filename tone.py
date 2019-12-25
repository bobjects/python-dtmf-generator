from wavefile import WaveFile
from math import pi
from math import sin

class Tone(object):
    __slots__ = 'frequencies', 'attenuation_db', 'duration', 'silence_duration'

    def __init__(self, frequencies, attenuation_db=0, duration=0.25, silence_duration=0.25):
        self.frequencies = frequencies
        self.attenuation_db = attenuation_db
        self.duration = duration
        self.silence_duration = silence_duration

    @property
    def number_of_frequecies(self):
        return len(self.frequencies)

    def generate_to_wavefile(self, a_wavefile):
        sample_index_multipliers = [frequency / a_wavefile.sampling_rate * pi * 2 for frequency in self.frequencies]
        for sample_index in range(0, int(a_wavefile.sampling_rate * self.duration)):
            sample = sum([sin(sample_index_multiplier * sample_index) * (1 / self.number_of_frequecies) for sample_index_multiplier in sample_index_multipliers])
            a_wavefile.append_sample(sample)
        for sample_index in range(0, int(a_wavefile.sampling_rate * self.silence_duration)):
            a_wavefile.append_silent_sample()

    def generate_to_wavefile_path(self, path_name, sampling_rate=8000, sample_width=2, number_of_channels=1):
        wavefile = WaveFile(path_name, sampling_rate, sample_width, number_of_channels)
        self.generate_to_wavefile(wavefile)
        wavefile.close()

    @classmethod
    def dtmf_string(cls, a_string):
        frequencies = {
            '1': [1209,697],
            '2': [1336, 697],
            '3': [1477, 697],
            '4': [1209, 770],
            '5': [1336, 770],
            '6': [1477, 770],
            '7': [1209, 852],
            '8': [1336, 852],
            '9': [1477, 852],
            '0': [1336, 941],
            '*': [1209, 941],
            '#': [1477, 941],
            'a': [1633, 697],
            'b': [1633, 770],
            'c': [1633, 852],
            'd': [1633, 941],
            'A': [1633, 697],
            'B': [1633, 770],
            'C': [1633, 852],
            'D': [1633, 941],
        }.get(a_string, [1209,697])
        return Tone(frequencies)

    @classmethod
    def dtmf_1(cls):
        return Tone([1209, 697])

    @classmethod
    def dtmf_2(cls):
        return Tone([1336, 697])

    @classmethod
    def dtmf_3(cls):
        return Tone([1477, 697])

    @classmethod
    def dtmf_4(cls):
        return Tone([1209, 770])

    @classmethod
    def dtmf_5(cls):
        return Tone([1336, 770])

    @classmethod
    def dtmf_6(cls):
        return Tone([1477, 770])

    @classmethod
    def dtmf_7(cls):
        return Tone([1209, 852])

    @classmethod
    def dtmf_8(cls):
        return Tone([1336, 852])

    @classmethod
    def dtmf_9(cls):
        return Tone([1477, 852])

    @classmethod
    def dtmf_0(cls):
        return Tone([1336, 941])

    @classmethod
    def dtmf_star(cls):
        return Tone([1209, 941])

    @classmethod
    def dtmf_pound(cls):
        return Tone([1477, 941])

    @classmethod
    def dtmf_a(cls):
        return Tone([1633, 697])

    @classmethod
    def dtmf_b(cls):
        return Tone([1633, 770])

    @classmethod
    def dtmf_c(cls):
        return Tone([1633, 852])

    @classmethod
    def dtmf_d(cls):
        return Tone([1633, 941])

    @classmethod
    def pure_1000(cls):
        return Tone([1000])

