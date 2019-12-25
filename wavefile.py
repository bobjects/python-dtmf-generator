import wave


class WaveFile(object):
    __slots__ = 'path_name', 'sampling_rate', 'sample_width', 'number_of_channels', '_wave'

    def __init__(self, path_name, sampling_rate=8000, sample_width=2, number_of_channels=1):
        self.path_name = path_name
        self.sampling_rate = sampling_rate
        self.sample_width = sample_width
        self.number_of_channels = number_of_channels
        self._wave = wave.open(self.path_name, 'w')
        self._wave.setnchannels(self.number_of_channels)
        self._wave.setsampwidth(self.sample_width)
        self._wave.setframerate(self.sampling_rate)

    def append_sample(self, a_float):
        sample_integer = int(a_float * (2 ** (8 * self.sample_width - 1) - 1))
        # print(sample_integer)
        self._wave.writeframes(sample_integer.to_bytes(self.sample_width, byteorder='little', signed=True))

    def append_silent_sample(self):
        self.append_sample(0.0)

    def close(self):
        self._wave.close()
