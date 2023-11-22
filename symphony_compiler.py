'''
Le compilateur va transformer le code Symphony en un fichier midi compilé.
Des fonctions pythons sont utilisées grâce à la librairie 'midiutil'.
Si une valeur à un endroit n'est pas bonne, notamment les boucles et fonctions, 
alors on arrête la compilation avec un message d'erreur.
're' est utilisé pour retirer les guillemets lorsqu'on donne le nom d'une fonction dans add_note.
'sys' nous permet de récupérer les arguments, notamments le chemin du fichier à compiler.
'''

from symphony_parser import parse
import AST
from AST import addToClass
import operator
from midiutil import MIDIFile
import re
import sys


# Global values
# MIDI File used to create the final midi file containing the song
midi_file = MIDIFile(128, adjust_origin=False)
# At which time the note is written
time = 0
# In which track
track = 0
# Which is the current instrument
channel = 0
# Current octave
octave = 0

list_instruments = (
    "--- Indices\t---\tFamiliy ---\n"
    + "-> [1 - 8]\t---\tPianos\n"
    + "-> [9 - 16]\t---\tChromatic Percussion\n"
    + "-> [17 - 24]\t---\tOrgan\n"
    + "-> [25 - 32]\t---\tGuitar\n"
    + "-> [33 - 40]\t---\tBass\n"
    + "-> [41 - 48]\t---\tStrings\n"
    + "-> [49 - 56]\t---\tEnsemble\n"
    + "-> [57 - 64]\t---\tBrass\n"
    + "-> [65 - 72]\t---\tReed\n"
    + "-> [73 - 80]\t---\tPipe\n"
    + "-> [81 - 88]\t---\tSynth Lead\n"
    + "-> [89 - 96]\t---\tSynth Pad\n"
    + "-> [97 - 104]\t---\tSynth Effects\n"
    + "-> [105 - 112]\t---\tEthnic\n"
    + "-> [113 - 120]\t---\tPercussive\n"
    + "-> [121 - 128]\t---\tSound Effects\n"
)

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

notes = {
    "C": 0,
    "DO": 0,
    "C#": 1,
    "DO#": 1,
    "D": 2,
    "RE": 2,
    "D#": 3,
    "RE#": 3,
    "E": 4,
    "MI": 4,
    "F": 5,
    "FA": 5,
    "F#": 6,
    "FA#": 6,
    "G": 7,
    "SOL": 7,
    "G#": 8,
    "SOL#": 8,
    "A": 9,
    "LA": 9,
    "A#": 10,
    "LA#": 10,
    "B": 11,
    "SI": 11,
}

vars = {}


@addToClass(AST.ProgramNode)
def compile(self):
    # Get the global value
    global midi_file
    for c in self.children:
        c.compile()
    # Create the final midi file
    with open("symphony_file.mid", "wb") as output_file:
        midi_file.writeFile(output_file)


@addToClass(AST.TokenNode)
def compile(self):
    if type(self.tok) is str and '"' not in self.tok:
        return vars[self.tok]
    return self.tok


@addToClass(AST.OpNode)
def compile(self):
    val = 0
    if len(self.children) == 1:
        val = self.children[0].compile()
        val *= -1
    else:
        val = operations[self.op](
            self.children[0].compile(), self.children[1].compile()
        )
    return val


@addToClass(AST.AssignNode)
def compile(self):
    if self.declared:
        vars[self.children[0].tok] = self.children[1].compile()
    else:
        if self.children[0].tok in vars:
            vars[self.children[0].tok] = self.children[1].compile()
        else:
            print("Error, the variable is not defined")
            exit()


@addToClass(AST.RangeNode)
def compile(self):
    start = self.children[0].compile()
    end = self.children[1].compile()
    step = self.children[2].compile()

    if (start > end and step < 0) or (start < end and step > 0):
        for i in range(
            self.children[0].compile(),
            self.children[1].compile(),
            self.children[2].compile(),
        ):
            self.children[3].compile()
    else:
        print("Error, the range loop isn't correctly defined")
        exit()


@addToClass(AST.FuncNode)
def compile(self):
    # Func with one parameter : change_instrument(12), change_track(1), change_octave(7)
    if self.func_name == "change_instrument":
        if len(self.children) == 1:
            global channel
            channel += 1
            midi_file.addProgramChange(
                0, channel, 0, self.children[0].compile())
        else:
            print(
                "Error, the number of parameters is not respected for the function change_instrument : required 1 found "
                + len(self.children)
            )
            exit()
    elif self.func_name == "change_octave":
        if len(self.children) == 1:
            global octave
            temp_octave = self.children[0].compile()
            if temp_octave >= -1 and temp_octave <= 9:
                octave = temp_octave
            else:
                print(
                    "Error, the number used for octave is not valid, use between -1 and 9 "
                )
                exit()
        else:
            print(
                "Error, the number of parameters is not respected for the function change_octave : required 1 found "
                + len(self.children)
            )
            exit()
    elif self.func_name == "change_track":
        if len(self.children) == 1:
            global track
            temp_track = self.children[0].compile()
            if temp_track >= 0 and temp_track <= 128:
                track = temp_track
            else:
                print(
                    "Error, the number used for track is not valid, use between 0 and 128 "
                )
                exit()
        else:
            print(
                "Error, the number of parameters is not respected for the function change_track : required 1 found "
                + len(self.children)
            )
            exit()
    elif self.func_name == "add_tempo":
        if len(self.children) == 3:
            # Func with three parameters : add_tempo(track, time, tempo)
            midi_file.addTempo(
                self.children[0].compile(),
                self.children[1].compile(),
                self.children[2].compile(),
            )
        else:
            print(
                "Error, the number of parameters is not respected for the function add_tempo : required 3 found "
                + len(self.children)
            )
            exit()
    elif self.func_name == "add_note":
        if len(self.children) == 4:
            # Func with four parameters : add_note(65, time, duration, volume)
            val = self.children[0].compile()
            if type(val) is str:
                val = re.findall('"([^"]*)"', val)[0]
                if val in notes:
                    val = notes[val]
                    val = val + 12 * (octave + 1)
                else:
                    print(
                        "Error, the string used for the note is note valid, refer to the documentation "
                    )
                    exit()
            if val < 0 or val > 127:
                print(
                    "Error, the number used for note is not correct, use between 0 and 11 "
                )
                exit()
            midi_file.addNote(
                track,
                channel,
                val,
                self.children[1].compile(),
                self.children[2].compile(),
                self.children[3].compile(),
            )
        else:
            print(
                "Error, the number of parameters is not respected for the function add_note : required 4 found "
                + len(self.children)
            )
            exit()
    elif self.func_name == "list_instrument":
        if len(self.children) == 0:
            print(list_instruments)
        else:
            print(
                "Error, the number of parameters is not respected for the function list_instruments : required 0 found "
                + len(self.children)
            )
            exit()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            prog = open(sys.argv[1]).read()
            ast = parse(prog)
            compiled = ast.compile()
        except IOError:
            print("Erreur : Le fichier", sys.argv[1], "n'existe pas")
        except:
            print("Une erreur inconnue est survenue, veuillez réessayer")
    else:
        print(
            "Erreur : Pas le bon nombre d'arguments, argument requis : chemin du fichier à compiler")
