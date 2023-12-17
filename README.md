### Summary

This is some code I wrote to help identify good candidates for cluster scales, that is, scales where multiple consecutive notes can ring out at once on a standard guitar. Since harmonics and open strings make this easier, I wanted to see how many notes could be played as an open/harmonic in every scale. Here, we are showing that number for every mode of the major scale, harmonic minor, and melodic minor.

### Instructions

You can run the code yourself in a terminal window with the command `python main.py`, which will write two text files to this folder called 'singleOctave.txt' and 'twoOctaves.txt'.

- **singleOctave.txt**: Each row represents a root note and a mode of a scale that starts and ends on that note. The number indicates how many notes of that single-octave scale can be played as an open string or harmonic. The list at the end tells you which notes are being included in that count. If a note could be played in multiple ways as an open string/harmonic, we just pick one of those at random.

- **twoOctaves.txt**: Same as above, but the scale is two octaves instead of one.
