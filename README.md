# hook_interview

## Usage

python3 manipulate_audio.py

## Setup Environment Commands:

###### pydub
brew install ffmpeg
pip install pydub
pip install simpleaudio

###### pitch shifter
git clone https://github.com/cwoodall/pitch-shifter-py.git
cd pitch-shifter-py
pip install .


## Creative Goal

I'd like to use EQ and pitch shifting for two main goals. First, an overally strength of this snippet and Kanye's rapping in general is a rhythm created by accentuating important words with his voice. In this remix, I want to highlight and further this accentuation by pitch shifting these words. I'd also like to use pitch shifting to add a new dimension to the vocals, making them more dynamic in the same way that playing playing in multiple keys can be more dynamic. In an overall song, this would definitely be too much to have for every line/bar, but given this is just a two line snippet, I think it could work.

From a practical, technical perspective, I had a lot of trouble installing pyo and pyo tools, and chose to stick with effects in pydub and pitchsfiter, both of which worked immediately with my system. Because of this, I did not use the more complicated effects (reverb, compression, synthesizers) only available with pyo, which I am very interested in learning and applying in the future. I will list some ways I could use these effects to further the creative vision in the next steps section.

## Ideas
1. Intro - manipulate intro vocal sample so that each word increases in pitch. 
2. Repeat Intro normally as well to add more space before rapping
3. Rapping
    a. manipulate last word with reverb tail so that each reverbed voice has a different pitch.
    b. manipulate middle words in line with pitch accents (Low->High to match reverb?).
3. Drums - Take out drums after the last word of each line, so for the course of the reverb there's no drums. OPTIONAL: Add reverb to the last drum sound of a line.
4. (OPTIONAL) Bass - try using bass boost in https://github.com/belangeo/pyo-tools

## Next Steps
1. Test out more advanced technical libraries. 
    a. Test out the oscillators to see if we can create matching synth sounds by say, taking b. sine wave and then applying the mastering library to match the sound of the song so far
2. Add reverb to the accompaniment at certain parts, maybe the same times as reverb in vocal, maybe different times to create more accentuation
3. Totally remix the drums - given this is a short snippet and not the whole song, the drums could be more complex
4. Play with eq on the vocal to pair with pitch shifting - maybe do low pass on low pitch/high pass on high pitch

## Workflow

1. Split audio files using online tool that applies spleeter (was having dependencies issues on my laptop) https://ezstems.com/ 

2. Shift vocal pitch up and down using pitch shifter. Other pitch shifting methods such as pydub change the speed of the file, but pitchshifter doesn't.

3. Change drums around ends of lines. Should accentuate the effect we are adding on the echoes on the last words of lines.

4. Mix audio files using pydub

5. Master using matchering - will use original track as reference file to hopefully fix up changes in track balance and fix clicks/pops.

## Challenges

1. Setting up environment for all libraries
2. Figuring out timings for effects
3. Maintaining creative flow while taking periods of time to code
4. Mixing altered audio stems seamlessly back in
5. Recognizing frequencies that create cracks/pops in any given sound
