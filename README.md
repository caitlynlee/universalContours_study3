# universal contours
Generating and presenting stimuli for universal contours study. Code is for generating, sorting, and picking random stimuli.

### Stimuli
Currently using stimuli v1. Tested for variance with regards to size of bounding box, duration of sound, onset number, etc.

#### Images

Images were created using Processing. Two methods were used to create images. Number of corners range from 1-13.

One method used to create the images include combination of lines and curves, with a given number of vertices. Proportion of curves ranges from 0 to 1. The other method used to create the images was distorting a circle; takes as a parameter a specified number of points around which the circle will be distorted.

#### Sounds

Sounds were created using the pyo library. Three methods were used to create sounds. Spectral centroid ranges from 0 to 1950

Methods used to generate the sounds: LFO, SAW table, and ROS. LFO also uses sine loop, with random parameters. SAW generator also takes random parameters, and chaotic attractor for the Rossler system. Takes Rossler system, or sine wave, as one of the paramaters. The duration of the sounds ranges from 0.5 seconds to 3.5 seconds.

### GUI

3 different conditions - negative arousal, positive arousal, and matching. All created using `psychopy` library. Conditions are assigned randomly vi `getSubjectIDs`. Generates IDs in range 0-n for $n$ participants, and then assigned randomly to one of three conditions. Conditions for each subjectID can be found in `conditionMapping.json`.

All conditions are run from `run.py` in *GUI* directory. ID and subject demographics must be entered into the code manually before beginning task. `run.py` will then run the appropriate arousal or matching task, based on the condition mapping (so as to be blind to experimenter).
