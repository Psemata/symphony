# Symphony
*Symphony* is a compiled language designed for the creation of music and MIDI sounds.

Users can employ language functions to generate notes for different instruments across multiple tracks, ultimately creating a final file that encapsulates their musical composition.

The work accomplished includes:
- Creation of a lexical analyzer
- Creation of a syntax analyzer
- Development of a compiler that transforms our language into Python and subsequently generates sound
- Error handling

## Requirements
To ensure the Symphony language functions properly, several important Python packages need to be installed:
- pydot --> Installation: `pip install pydot`
- ply --> Installation: `pip install ply`
- os --> Already installed by default
- operator --> Already installed by default (install with `pip install pyoperators` if needed)
- re --> Already installed by default (install with `pip install regex` if needed)
- midiutil --> Installation: `pip install MIDIUtil` & Usage: `from midiutil import MIDIFile`
- graphviz --> Installation: `pip install graphviz` (If not installed as an executable)

## Installation
To install Symphony, retrieve the various language-related files:
- AST.py
- symphony_ley.py
- symphony_parser.py
- symphony_compiler.py

To run the language, generate a Symphony language file (in .txt or another format) and pass it to the compiler.
When the compiler is executed, a .midi file will be generated and can be played using any media player.

### VLC
For VLC, you need to install a plugin to play MIDI files:
- Plugin Installation Guide: [How to play MIDI files on the VLC Media Player 3.0.8](https://ourcodeworld.com/articles/read/1170/how-to-play-midi-files-on-the-vlc-media-player-3-0-8)
- Additional Information: [VLC Midi Plugin Wiki](https://wiki.videolan.org/Midi/)

## Team Members
* Bruno Costa, [@Psemata](https://github.com/Psemata).
* Diogo Lopes Da Silva, [@Ultrasic](https://github.com/Ultrasic).
