import classes as classes
import math

scales = {
    "Major": [0, 2, 4, 5, 7, 9, 11, 12],
    "Melodic Minor": [0, 2, 3, 5, 7, 8, 11, 12],
    "Harmonic Minor": [0, 2, 3, 5, 7, 9, 11, 12],
}

majModes = {
    1: "Ionian    ",
    2: "Dorian    ",
    3: "Phrygian  ",
    4: "Lydian    ",
    5: "Mixolydian",
    6: "Aeolian   ",
    7: "Locrian   ",
}


def getModes(scale):
    modes = []
    for i in range(len(scale) - 1):
        newRoot = scale[i]
        newScale = [(x - newRoot) % 12 for x in scale[:-1]] + [12]
        newScale.sort()
        modes.append((i + 1, newScale))
    return modes


def addOrdinal(num):
    if num == 1:
        return str(num) + "st "
    elif num == 2:
        return str(num) + "nd "
    elif num == 3:
        return str(num) + "rd "
    else:
        return str(num) + "th "


def analyzeFromRoot(guitar, root, numOctaves=1, fname="singleOctave.txt"):
    numRoot = math.floor(root / 12) + 2
    rootStr = classes.pitchClasses[root % 12] + str(numRoot) + ", "
    for scaleName, scale in scales.items():
        modes = getModes(scale)
        for mode in modes:
            harms = []
            curMode = mode[1]
            for i in range(1, numOctaves):
                curMode = curMode[:-1] + [x + 12 * i for x in mode[1]]
            numHarms = 0
            numOpen = 0
            numHarmOrOpen = 0
            for scaleDeg in [x + root for x in curMode]:
                options = guitar.findNote(scaleDeg)
                hasHarmonic = any(["harm" in option.method for option in options])
                hasOpen = any(["open" in option.method for option in options])
                numOpen += int(hasOpen)
                numHarms += int(hasHarmonic)
                numHarmOrOpen += int(hasOpen or hasHarmonic)
                for option in options:
                    if ("harm" in option.method) or ("open" in option.method):
                        harms.append(option.__repr__())
                        break
            with open(fname, "a") as f:
                if scaleName == "Major":
                    modeStr = (majModes[mode[0]] + " ").ljust(30, "-")
                else:
                    modeStr = " (" + addOrdinal(mode[0]) + "Mode) "
                    modeStr = scaleName.ljust(14, " ") + modeStr

                scaleStr = rootStr
                scaleStr += modeStr
                scaleStr += (
                    "--- " + str(numHarmOrOpen).ljust(3, " ") + "harmonics/open strings"
                )
                scaleStr += ": " + str(harms) + "\n"
                f.write(scaleStr)


if __name__ == "__main__":
    guitar = classes.Guitar(24)
    with open("singleOctave.txt", "w") as f:
        f.write("Single Octave Scales:\n")
    with open("twoOctaves.txt", "w") as f:
        f.write("Two Octave Scales:\n")
    for root in range(30):
        analyzeFromRoot(guitar, root)
        analyzeFromRoot(guitar, root, 2, "twoOctaves.txt")
