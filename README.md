# hook_interview

## Setup Environment Commands:

###### pydub
brew install ffmpeg
pip install pydub
pip install simpleaudio

###### pitch shifter
git clone https://github.com/cwoodall/pitch-shifter-py.git
cd pitch-shifter-py
pip install .


## Themes
1. Pitch shifting to accentuate vocals, both in sample and in rapping

## Ideas
1. Intro - manipulate intro vocal sample so that each word increases in pitch
2. Rapping - manipulate last word with reverb tail so that each reverbed voice
3. Drums - Take out drums after the last word of each line, so for the course of the reverb there's no drums. OPTIONAL: Add reverb to the last drum sound of a line.
4. (OPTIONAL) Bass - try using bass boost in https://github.com/belangeo/pyo-tools

## Next Steps
1. Test out more advanced technical libraries. 
    a. Test out the oscillators to see if we can create matching synth sounds by say, taking a sine wave and then applying the mastering library to match the sound of the song so far
2. Add reverb to the accompaniment at certain parts, maybe the same times as reverb in vocal, maybe different times to create more accentuation
3. Totally remix the drums - given this is a short snippet and not the whole song, the drums could be more complex
4. Play with eq on the vocal to pair with pitch shifting - maybe do low pass on low pitch/high pass on high pitch

## Workflow

1. Split audio files using online tool that applies spleeter (was having dependencies issues on my laptop) https://ezstems.com/ 

2. Shift vocal pitch up and down 

pitchshifter -s ./hook_interview/input_files/vocals_[ezstems.com].wav -o ./hook_interview/manipulated_vocal_files/vocals_pitched_up.wav -p 7 -b 1

pitchshifter -s ./hook_interview/input_files/vocals_[ezstems.com].wav -o ./hook_interview/manipulated_vocal_files/vocals_pitched_down.wav -p -7 -b 1

## Challenges

1. Setting up environment for all libraries
2. Figuring out timings for effects
3. Maintaining creative flow while taking periods of time to code
