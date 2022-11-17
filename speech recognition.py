import wave
import json
import glob
import numpy
import tgt

from vosk import Model, KaldiRecognizer, SetLogLevel
import Word as custom_Word

model_path = "/PATH/TO/VOSK/MODEL"

#Searches for .wav files using their n## format
audio_filename = glob.glob("/PATH/TO/FOLDER/AUDIO/FILES/*n##*.wav")
audio_filename = audio_filename[0]

model = Model(model_path)
wf = wave.open(audio_filename, "rb")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# get the list of JSON dictionaries
results = []
# recognize speech using vosk model
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        part_result = json.loads(rec.Result())
        results.append(part_result)
part_result = json.loads(rec.FinalResult())
results.append(part_result)

# convert list of JSON dictionaries to list of 'Word' objects
list_of_Words = []
for sentence in results:
    if len(sentence) == 1:
        # sometimes there are bugs in recognition 
        # and it returns an empty dictionary
        # {'text': ''}
        continue
    for obj in sentence['result']:
        w = custom_Word.Word(obj)  # create custom Word object
        list_of_Words.append(w)  # and add it to list

wf.close()  # close audiofile

# output to the screen
for word in list_of_Words:
    print(word.to_string()) 

audio_filename = audio_filename.split("/")[-1]
audio_filename = audio_filename.split(".")[0]
audio_filename = audio_filename + ".txt"

# create textgrid file with audioname and list of words
tg = tgt.core.TextGrid()
tg.name = audio_filename  # type: ignore
tier = tgt.core.IntervalTier(name='words')
for word in list_of_Words:
    tier.add_interval(tgt.core.Interval(word.start, word.end, word.word))
tg.add_tier(tier)
tgt.io.write_to_file(tg, f'{audio_filename}.TextGrid', format='long')