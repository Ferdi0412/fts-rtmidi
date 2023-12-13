import ftsmidi # import MidiSender
from   ftsmidi import MidiSender


if __name__ == '__main__':
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
