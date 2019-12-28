from wavefile import WaveFile
from tone import Tone


class Tones(object):
    __slots__ = 'tones', 'attenuation_db', 'duration', 'silence_duration'

    def __init__(self, tones=[], attenuation_db=0, duration=0.25, silence_duration=0.25):
        self.tones = tones
        self.attenuation_db = attenuation_db
        self.duration = duration
        self.silence_duration = silence_duration

    def generate_to_wavefile(self, a_wavefile):
        for tone in self.tones:
            tone.generate_to_wavefile(a_wavefile)

    def generate_to_wavefile_path(self, path_name, sampling_rate=8000, sample_width=2, number_of_channels=1):
        print(path_name)
        wavefile = WaveFile(path_name, sampling_rate, sample_width, number_of_channels)
        self.generate_to_wavefile(wavefile)
        wavefile.close()

    @classmethod
    def dtmf_string(cls, a_string, attenuation_db=0, duration=0.25, silence_duration=0.25):
        return Tones([Tone.dtmf_string(c, attenuation_db=attenuation_db, duration=duration, silence_duration=silence_duration) for c in a_string])

    # @classmethod
    # def mf_string(cls, a_string, attenuation_db=0, duration=0.25, silence_duration=0.25):
    #     # TODO:  'kp', 'kp2', and 'st' are atomic.
    #     return Tones([Tone.mf_string(c, attenuation_db=attenuation_db, duration=duration, silence_duration=silence_duration) for c in a_string])

