### Summary

This is some code I wrote to help find good cluster scales, that is, scales where multiple consecutive notes can ring out at once on a standard guitar. Since harmonics and open strings make this easier, I wanted to see how many notes could be played as an open/harmonic in every scale. Here, we compute that number for every mode of the major, harmonic minor, and melodic minor scales. We do this for every root note from E2 up to A4. This only takes the first three harmonics above the fundamental into account. It also doesn't consider artificial harmonics.

### Instructions

You can run the code in a terminal window with the command `python main.py`, which will write two text files to this folder called 'singleOctave.txt' and 'twoOctaves.txt'. Those text files are also included here for convenience.

### Interpretation

- **singleOctave.txt**: Each row represents a root note and a mode of a scale that starts and ends on that note. The number after all the dashes says how many notes of that single-octave scale can be played as an open string or harmonic. The list at the end tells you which notes are being included in that count. If a note could be played in multiple ways as an open string/harmonic, we just pick one of those at random.

- **twoOctaves.txt**: Same as above, but the scale is two octaves long instead of one.

Here's an example of a line from the above files:

`E2, Lydian     ---------------------- 2  harmonics/open strings: ['E 0  (open)', 'E 12 (harm)']`

This row represents the E Lydian scale starting from E2, the open sixth string on a standard-tuned guitar. This tells us that 2 of the notes of that one-octave scale could be played with open strings or harmonics, namely the open E string itself and the 12th fret-harmonic on the E string. The low E-string is denoted "E", and the high E-string is denoted "e".
