from wavefile import WaveFile
from tone import Tone


class Tones(object):
    __slots__ = 'tones'

    def __init__(self, tones=[]):
        self.tones = tones

    def generate_to_wavefile(self, a_wavefile):
        for tone in self.tones:
            tone.generate_to_wavefile(a_wavefile)

    def generate_to_wavefile_path(self, path_name, sampling_rate=8000, sample_width=2, number_of_channels=1):
        wavefile = WaveFile(path_name, sampling_rate, sample_width, number_of_channels)
        self.generate_to_wavefile(wavefile)
        wavefile.close()

    @classmethod
    def dtmf_string(cls, a_string):
        return Tones([Tone.dtmf_string(c) for c in a_string])

