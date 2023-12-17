import classes as classes
import math

scales = {
    "Major": [0, 2, 4, 5, 7, 9, 11],
    "Melodic Minor": [0, 2, 3, 5, 7, 8, 11],
    "Harmonic Minor": [0, 2, 3, 5, 7, 9, 11],
}


def getModes(scale):
    modes = []
    for i in range(len(scale)):
        newRoot = scale[i]
        newScale = [(x - newRoot) % 12 for x in scale]
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
    numRoot = math.floor(root / 12) + 1
    rootStr = addOrdinal(numRoot)
    for scaleName, scale in scales.items():
        modes = getModes(scale)
        for mode in modes:
            curMode = mode[1]
            for i in range(1, numOctaves):
                curMode += [x + 12 * i for x in mode[1]]
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
            with open(fname, "a") as f:
                modeStr = addOrdinal(mode[0])
                scaleStr = rootStr
                rootName = (classes.pitchClasses[root % 12] + ",").ljust(3, " ")
                scaleStr += rootName + scaleName.ljust(14, " ")
                scaleStr += " (" + modeStr + "Mode) "
                scaleStr += "--- {} harmonics/open strings".format(numHarmOrOpen) + "\n"
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
