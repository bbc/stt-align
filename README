# Speech-to-text aligner

Python module which aligns a known transcript to the output of a speech-to-text
processor. This gives each word in the transcript a timestamp and duration.

## Installation

    sudo python setup.py install

## Usage

    import sttalign
    sttalign.alignJSONText('/path/to/stt-out.json', 'this is the transcript')
    sttalign.alignJSON('/path/to/stt-out.json', '/path/to/transcript.json')

stt-out.json:

    {
      "words": [
        {"word": "this", "start": 0.02, "end": 0.05},
        {"word": "is", "start": 0.06, "end": 0.10},
        {"word": "the", "start": 0.12, "end": 0.18},
        {"word": "transcript", "start": 0.20, "end": 0.32}
      ]
    }

transcript.json:

    { "text": "this is the transcript" }
