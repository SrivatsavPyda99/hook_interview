import pydub
from pydub import AudioSegment
from pydub.playback import play
import sys
import os
import matchering as mg

testing = True

### TESTING PITCH SHIFTING WITH PYDUB ###

'''
# Load into PyDub


### Testing Effects ###

vocals_stem = AudioSegment.from_wav("input_files/vocals_[ezstems.com].wav")

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
'''

### LOAD SOUNDS ###

vocals_stem = AudioSegment.from_wav("input_files/vocals_[ezstems.com].wav")
lowpitch_vocals_stem = AudioSegment.from_wav("manipulated_vocal_files/vocals_pitched_down.wav")
highpitch_vocals_stem = AudioSegment.from_wav("manipulated_vocal_files/vocals_pitched_up.wav")

drums_stem = AudioSegment.from_wav("input_files/drums_[ezstems.com].wav")
bass_stem = AudioSegment.from_wav("input_files/bass_[ezstems.com].wav")
other_stem = AudioSegment.from_wav("input_files/other_[ezstems.com].wav")

remixed = vocals_stem.overlay(drums_stem).overlay(bass_stem).overlay(other_stem)
remixed_without_vocals = drums_stem.overlay(bass_stem).overlay(other_stem)

#play(remixed)

### INTRO ###

#os.system('pitchshifter -s ./input_files/vocals_2_split[ezstems.com].wav -o ./manipulated_vocal_files/vocals_pitched_up.wav -p 7 -b 1')
#os.system('pitchshifter -s ./input_files/vocals_2_split[ezstems.com].wav -o ./manipulated_vocal_files/vocals_pitched_down.wav -p -7 -b 1')

intro_length = 2525
intro_length_longer = 3500


mixed_vocals_beginning = lowpitch_vocals_stem[:1300]+ vocals_stem[1300:1900] + highpitch_vocals_stem[1900:intro_length]
mixed_beginning = mixed_vocals_beginning.overlay(drums_stem[:intro_length])
mixed_beginning = mixed_beginning.overlay(bass_stem[:intro_length])
mixed_beginning = mixed_beginning.overlay(other_stem[:intro_length])

mixed_vocals_beginning_2 = AudioSegment.silent(duration=1300)+ \
            highpitch_vocals_stem[1300:1900] + \
            vocals_stem[1900:intro_length]
mixed_beginning_2 = mixed_vocals_beginning_2.overlay(drums_stem[:intro_length])
mixed_beginning_2 = mixed_beginning_2.overlay(bass_stem[:intro_length])
mixed_beginning_2 = mixed_beginning_2.overlay(other_stem[:intro_length])

#lowpitch_vocals_softer_stem = lowpitch_vocals_stem - 3
#highpitch_vocals_softer_stem = highpitch_vocals_stem - 3

#mixed_vocals_temp = lowpitch_sound_softer_stem[:intro_length_longer].overlay(highpitch_sound_softer_stem[:intro_length_longer])
#mixed_vocals_beginning = mixed_vocals_temp.overlay(vocals_stem[:intro_length_longer])
#mixed_vocals = mixed_vocals_beginning + vocals_stem[intro_length_longer:]

#mix = mixed_vocals_beginning + sound[intro_length:].overlay(accompaniment_stem[intro_length:])

### FIRST LINE ###

line_1_start = intro_length

line_1_midbeg_start = 4000
line_1_midbeg_end = 4500

line_1_midend_start = 6000
line_1_midend_end =6500

line_1_start_effects = 7800
line_1_first_word = 8500
line_1_second_word = 9200
line_1_third_word = 10000
line_1_end = 11500 

#os.system('pitchshifter -s ./input_files/vocals_[ezstems.com].wav -o ./manipulated_vocal_files/vocals_pitched_up_3_4_split.wav -p 3 -b 1')
#os.system('pitchshifter -s ./input_files/vocals_[ezstems.com].wav -o ./manipulated_vocal_files/vocals_pitched_up_5_4_split.wav -p 5 -b 1')
#os.system('pitchshifter -s ./input_files/vocals_[ezstems.com].wav -o ./manipulated_vocal_files/vocals_pitched_down_3_4_split.wav -p -3 -b 1')
#os.system('pitchshifter -s ./input_files/vocals_[ezstems.com].wav -o ./manipulated_vocal_files/vocals_pitched_down_5_4_split.wav -p -5 -b 1')

vocals_pitched_up_3_4_split = AudioSegment.from_wav("./manipulated_vocal_files/vocals_pitched_up_3_4_split.wav")
vocals_pitched_up_5_4_split = AudioSegment.from_wav("./manipulated_vocal_files/vocals_pitched_up_5_4_split.wav")
vocals_pitched_down_3_4_split = AudioSegment.from_wav("./manipulated_vocal_files/vocals_pitched_down_3_4_split.wav")
vocals_pitched_down_5_4_split = AudioSegment.from_wav("./manipulated_vocal_files/vocals_pitched_down_5_4_split.wav")


'''
mixed_vocals_line_1 = vocals_stem[line_1_start:line_1_midbeg_start] + \
                    lowpitch_vocals_stem[line_1_midbeg_start:line_1_midbeg_end].low_pass_filter(3000) + \
                    vocals_stem[line_1_midbeg_end:line_1_midend_start] + \
                    highpitch_vocals_stem[line_1_midend_start:line_1_midend_end] + \
                    vocals_stem[line_1_midend_end:line_1_start_effects] + \
                    lowpitch_vocals_stem[line_1_start_effects:line_1_first_word].low_pass_filter(1000) + \
                    vocals_stem[line_1_first_word:line_1_second_word] + \
                    highpitch_vocals_stem[line_1_second_word:line_1_third_word] +\
                    vocals_stem[line_1_third_word:line_1_end]
'''

mixed_vocals_line_1 = vocals_stem[line_1_start:line_1_midbeg_start] + \
                    lowpitch_vocals_stem[line_1_midbeg_start:line_1_midbeg_end].high_pass_filter(200) + \
                    vocals_stem[line_1_midbeg_end:line_1_midend_start] + \
                    highpitch_vocals_stem[line_1_midend_start:line_1_midend_end] + \
                    vocals_stem[line_1_midend_end:line_1_start_effects] + \
                    vocals_stem[line_1_start_effects:line_1_first_word] + \
                    vocals_pitched_up_3_4_split[line_1_first_word:line_1_second_word].low_pass_filter(16000) + \
                    vocals_pitched_up_5_4_split[line_1_second_word:line_1_third_word].low_pass_filter(19000) +\
                    vocals_stem[line_1_third_word:line_1_end]

'''
mixed_vocals_line_1 = vocals_stem[line_1_start:line_1_start_effects] + \
                    vocals_stem[line_1_start_effects:line_1_first_word] + \
                    lowpitch_vocals_stem[line_1_first_word:line_1_second_word].low_pass_filter(1000)  + \
                    highpitch_vocals_stem[line_1_second_word:line_1_third_word] +\
                    vocals_stem[line_1_third_word:line_1_end]
'''

drums_stem_line_1 = drums_stem[line_1_start:line_1_first_word] + \
                    AudioSegment.silent(duration=line_1_third_word-line_1_first_word) + \
                    drums_stem[line_1_third_word:line_1_end]


mixed_line_1 = mixed_vocals_line_1.overlay(drums_stem_line_1)
mixed_line_1 = mixed_line_1.overlay(bass_stem[line_1_start:line_1_end])
mixed_line_1 = mixed_line_1.overlay(other_stem[line_1_start:line_1_end])


### SECOND LINE ###

#11500
line_2_start = line_1_end

line_2_midbeg_start = 14000
line_2_midbeg_end = 14600

line_2_midend_start = 16000
line_2_midend_end =16500

line_2_start_effects = 17800
line_2_first_word = 18500
line_2_second_word = 19200
line_2_third_word = 20000
line_2_end = 21500 


mixed_vocals_line_2 = vocals_stem[line_2_start:line_2_midbeg_start] + \
                    lowpitch_vocals_stem[line_2_midbeg_start:line_2_midbeg_end].high_pass_filter(200) + \
                    vocals_stem[line_2_midbeg_end:line_2_midend_start] + \
                    highpitch_vocals_stem[line_2_midend_start:line_2_midend_end] + \
                    vocals_stem[line_2_midend_end:line_2_start_effects] + \
                    vocals_stem[line_2_start_effects:line_2_first_word] + \
                    vocals_pitched_up_3_4_split[line_2_first_word:line_2_second_word].low_pass_filter(16000) + \
                    vocals_pitched_up_5_4_split[line_2_second_word:line_2_third_word].low_pass_filter(18000) +\
                    vocals_stem[line_2_third_word:line_2_end]

'''
mixed_vocals_line_2 = vocals_stem[line_2_start:line_2_midbeg_start] + \
                    vocals_pitched_down_3_4_split[line_2_midbeg_start:line_2_midbeg_end] + \
                    vocals_stem[line_2_midbeg_end:line_2_midend_start] + \
                    vocals_pitched_up_3_4_split[line_2_midend_start:line_2_midend_end] + \
                    vocals_stem[line_2_midend_end:line_2_start_effects] + \
                    vocals_pitched_up_5_4_split[line_2_start_effects:line_2_first_word] + \
                    vocals_pitched_up_3_4_split[line_2_first_word:line_2_second_word] + \
                    vocals_stem[line_2_second_word:line_2_third_word] +\
                    vocals_stem[line_2_third_word:line_2_end]
'''

drums_stem_line_2 = drums_stem[line_2_start:line_2_first_word] + \
                    AudioSegment.silent(duration=line_2_third_word-line_2_first_word) + \
                    drums_stem[line_2_third_word:line_2_end]


mixed_line_2 = mixed_vocals_line_2.overlay(drums_stem_line_2)
mixed_line_2 = mixed_line_2.overlay(bass_stem[line_2_start:line_2_end])
mixed_line_2 = mixed_line_2.overlay(other_stem[line_2_start:line_2_end])







### MIXING ###


#mix = mixed_line_2

mix = mixed_beginning + remixed[400:intro_length] + mixed_line_1 + mixed_line_2
#mix = remixed[:line_1_start] + mixed_beginning[400:] + mixed_line_1
#mix = mixed_vocals_beginning + mixed_vocals_line_1 + mixed_vocals_line_2

play(mix)

mix.export("output_files/mix.wav", format="wav")

# Sending all log messages to the default print function
# Just delete the following line to work silently
mg.log(print)

mg.process(
    # The track you want to master
    target="output_files/mix.wav",
    # Some "wet" reference track
    reference="input_files/Kanye-West-I-Wonder-_Snippet_.wav",
    # Where and how to save your results
    results=[
        mg.pcm16("output_files/master_16bit.wav"),
        mg.pcm24("output_files/master_24bit.wav"),
    ],
)

print("playing mix")

#play(AudioSegment.from_wav("output_files/master_24bit.wav"))