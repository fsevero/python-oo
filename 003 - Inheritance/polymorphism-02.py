class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Formato inválido')

        self.filename = filename

class Mp3File(AudioFile):
    ext = '.mp3'

    def play(self):
        print('Playing mp3...')

class WavFile(AudioFile):
    ext = '.wav'

    def play(self):
        print('Playing wav...')

class OggFile(AudioFile):
    ext = '.ogg'

    def play(self):
        print('Playing ogg...')

mp3 = Mp3File('file.mp3')
mp3.play()

wav = WavFile('file.wav')
wav.play()

ogg = OggFile('file.ogg')
ogg.play()

mp4 = Mp3File('file.mp4')
mp4.play()