import pydub
from pydub import AudioSegment
from pydub.playback import play
import sys



# Load into PyDub
vocals_stem = AudioSegment.from_wav("input_files/vocals_[ezstems.com].wav")
accompaniment_stem = AudioSegment.from_wav("input_files/accompaniment_[ezstems.com].wav")

# Mix with our original loop
mixed = vocals_stem.overlay(accompaniment_stem)

mixed.export("output_files/final.wav", format="wav")

play(mixed)
