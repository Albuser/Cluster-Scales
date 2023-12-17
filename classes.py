import math

pitchClasses = {
    0: "E",
    1: "F",
    2: "F#",
    3: "G",
    4: "G#",
    5: "A",
    6: "A#",
    7: "B",
    8: "C",
    9: "C#",
    10: "D",
    11: "D#",
}


class Guitar:
    def __init__(self, numFrets):
        self.numFrets = numFrets
        self.strings = self.addStrings()

    def addStrings(self):
        baseNotes = [0, 5, 10, 15, 19, 24]
        strings = [String(baseNote, 24) for baseNote in baseNotes]
        return strings

    def findNote(self, noteNum, strings=None):
        options = []
        if strings == None:
            for string in self.strings:
                options += [note for note in string.notes if note.noteNum == noteNum]
        return options


class String:
    def __init__(self, baseNote, numFrets):
        self.baseNote = baseNote
        notes = []
        notes.append(Note(self.baseNote, "0".ljust(2, " ") + " (open)", self))
        for fret in range(1, numFrets):
            note = Note(self.baseNote + fret, str(fret).ljust(2, " ") + " (fret)", self)
            notes.append(note)
        notes.append(Note(self.baseNote + 12, "12 (harm)", self))
        notes.append(Note(self.baseNote + 24, "5  (harm)", self))
        notes.append(Note(self.baseNote + 19, "7  (harm)", self))
        notes.append(Note(self.baseNote + 24, "17 (harm)", self))
        notes.append(Note(self.baseNote + 19, "19 (harm)", self))
        self.notes = notes

    def __repr__(self):
        if self.baseNote == 0:
            return "E "
        if self.baseNote == 24:
            return "e "
        return pitchClasses[self.baseNote % 12].ljust(2, " ")


class Note:
    def __init__(self, noteNum, method, string):
        # low E: noteNum = 0
        self.pitchClass = noteNum % 12
        self.octave = math.floor(noteNum / 12)
        self.noteNum = noteNum
        self.method = method
        self.string = string

    def __repr__(self):
        return self.string.__repr__() + self.method
