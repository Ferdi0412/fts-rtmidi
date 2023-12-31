# fts-rtmidi
My name is Ferdinand Tonby-Strandborg, and I am creating this library as I want an easy, quick class for sending midi messages.

## Installation
Available on [PyPi](https://pypi.org/project/fts-rtmidi/)
```bash
pip install fts-rtmidi
```


## Usage
To check what MIDI ports are available, use the ***rtmidi*** library. To send messages, use the ***ftsmidi*** library.
```python
from rtmidi  import MidiOut
from ftsmidi import MidiSender
from time    import sleep

## Print available MIDI channels using rtmidi class
print(MidiOut().get_ports())


## Connect to MIDI channel "Microsoft GS Wavetable Synth 0"
midi = MidiSender("Microsoft GS Wavetable Synth 0")


## Trigger note middle-C with velocity 120 for 1 second
midi.note_on(60, 120)
sleep(1)
midi.note_off(60)

```

## MIDI protocol
For an in-depth explanation of the MIDI format, please see: https://www.cs.cmu.edu/~music/cmsip/readings/davids-midi-spec.htm

## Note on implementation
A lot of the functions are implemented in a way that is unnecessarily hard to read. This is simply as I wanted to test features of Python I haven't used before.

# rtmidi
This uses the **python-rtmidi** library, which is currently available through pypi. All classes here simply wrap the rtmidi classes, and handle formatting the messages.
<br>To learn more about RtMidi, visit their [PyPi](https://pypi.org/project/python-rtmidi/) page or their [GitHub repository](https://github.com/SpotlightKid/python-rtmidi).
