### Summary

This is some code I wrote to help identify good candidates for cluster scales, that is, scales where multiple consecutive notes can ring out at once on a standard guitar. Since harmonics and open strings make this easier, I wanted to see how many notes could be played as an open/harmonic in every scale. Here, we are calculating that number for every mode of the major, harmonic minor, and melodic minor scales. We do this for every root note from E2 up to A4.

### Instructions

You can run the code in a terminal window with the command `python main.py`, which will write two text files to this folder called 'singleOctave.txt' and 'twoOctaves.txt'. Those text files are also included here for convenience.

### Interpretation

- **singleOctave.txt**: Each row represents a root note and a mode of a scale that starts and ends on that note. The number indicates how many notes of that single-octave scale can be played as an open string or harmonic. The list at the end tells you which notes are being included in that count. If a note could be played in multiple ways as an open string/harmonic, we just pick one of those at random.

- **twoOctaves.txt**: Same as above, but the scale is two octaves instead of one.

Here's an example of a line from the above files:

`1st E,  Lydian     ------------------ 2  harmonics/open strings: ['E 0  (open)', 'E 12 (harm)']`

This row represents the E Lydian scale starting from the 1st E on a standard-tuned guitar (the open sixth string). This indicates that 2 of the notes of that one-octave scale could be played with open strings or harmonics, namely the open E string itself and the 12th fret-harmonic on the E string. Here, the low E-string is denoted "E", and the high E-string is denoted "e".
