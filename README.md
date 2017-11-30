# Universal Contours
Generating and presenting stimuli for universal contours study. Code is for generating and presenting stimuli.

### STIMULI
Directory containing relevant subdirectories with 390 shapes and 390 sounds. Also containing jupyter notebooks for looking at the variance in the relevant paramters of shapes and sounds.


#### Images

Images were created using Processing. Two methods were used to create images. Number of corners range from 1-13.

One method used to create the images include combination of lines and curves, with a given number of vertices. Proportion of curves ranges from 0 to 1. The other method used to create the images was distorting a circle; takes as a parameter a specified number of points around which the circle will be distorted.

Code for generating images can be found in *generating_images* subdirectory

#### Sounds

Sounds were created using the pyo library. Three methods were used to create sounds. Spectral centroid ranges from 0 to 1950

Methods used to generate the sounds: LFO, SAW table, and ROS. LFO also uses sine loop, with random parameters. SAW generator also takes random parameters, and chaotic attractor for the Rossler system. Takes Rossler system, or sine wave, as one of the paramaters. The duration of the sounds ranges from 0.5 seconds to 3.5 seconds.

Code for generating images can be found in *generating_sounds* subdirectory

### GUI

3 different conditions - negative arousal, positive arousal, and matching. All created using `psychopy` library. Conditions are assigned randomly; conditions for each subjectID can be found in `conditionMapping.json`.

To generate new subjectIDs assigned randomly to conditions and a new conditionMapping JSON, call `getSubjectIDs.py`.

**To run**: call `run.py`. Subject ID and subject demographics must be entered into the code in `run.py` manually before beginning task. `run.py` will then run the appropriate arousal or matching task, referenced from mapping JSON.

Output will be in the form of a directory for the subjectID containing JSON files of presentation order data and response data. Subject data directories are placed in *output* directory from within *GUI* directory. If not already exists, must manually create directory.

### DATA

Converts all relevant subject data (from *GUI/output/* directory) into CSV for each condition.

**To run**: call `getData.py`. Directory must contain stimuli parameter JSONs to build CSVs. Relevant parameter JSONs are created using `getParameters.py` from within the *STIMULI* directory.
