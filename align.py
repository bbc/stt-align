import json, difflib, sys

if len(sys.argv) != 3:
    sys.exit('Usage: python align.py stt.json transcript.json')

with open(sys.argv[1]) as sttFile:
    sttData=json.load(sttFile)['words']

with open(sys.argv[2]) as transcriptFile:
    transcriptText=json.load(transcriptFile)['text']

sttWords=[words.get('word') for words in sttData]
transcriptWords=transcriptText.split()
transcriptData=[{} for _ in range(len(transcriptWords))]

matcher = difflib.SequenceMatcher(None, sttWords, transcriptWords)
for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    if tag == 'equal':
        transcriptData[j1:j2] = sttData[i1:i2]
