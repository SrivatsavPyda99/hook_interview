import pydub
from pydub import AudioSegment
from pydub.playback import play
import sys

testing = True

# Load into PyDub
vocals_stem = AudioSegment.from_wav("input_files/vocals_[ezstems.com].wav")
accompaniment_stem = AudioSegment.from_wav("input_files/accompaniment_[ezstems.com].wav")

### Testing Effects ###

sound = vocals_stem

print(sound.frame_rate)

# shift the pitch down by half an octave (speed will decrease proportionally)
octaves = -0.95

#new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
low_sample_rate = 32 * 1000
high_sample_rate = 48 * 1000

lowpitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': low_sample_rate})
highpitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': high_sample_rate})

mixed_vocals = lowpitch_sound[:10000].overlay(sound[:10000])

#Play pitch changed sound
play(mixed_vocals)

if testing:
    sys.exit(0)


# Mix with our original loop
mixed = vocals_stem.overlay(accompaniment_stem)

mixed.export("output_files/final.wav", format="wav")

play(mixed)
