# hook_interview

Setup Environment Commands:

brew install ffmpeg
pip install pydub

Ideas

1. 

Workflow

1. Split audio files using online tool that applies spleeter (was having dependencies issues on my laptop)

2. Shift vocal pitch up and down 

pitchshifter -s ./hook_interview/input_files/vocals_[ezstems.com].wav -o ./hook_interview/manipulated_vocal_files/vocals_pitched_up.wav -p 7 -b 1
pitchshifter -s ./hook_interview/input_files/vocals_[ezstems.com].wav -o ./hook_interview/manipulated_vocal_files/vocals_pitched_down.wav -p -7 -b 1

