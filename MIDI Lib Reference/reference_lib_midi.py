from midiutil import MIDIFile

# One track, defaults to format 1 (tempo track automatically created)
MyMIDI = MIDIFile(128, adjust_origin=False)

MyMIDI.addProgramChange(0, 0, 0, 0)
MyMIDI.addProgramChange(0, 1, 0, 123)

# MIDI note number [between 0 - 127]
degrees = [60, 62, 64, 65, 67, 69, 71, 72]
track = 1  # piste
channel = 1  # instrument
time = 0  # In beats
duration = 1  # In beats
tempo = 60  # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI.addTempo(track, time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1


with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
