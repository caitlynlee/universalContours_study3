#import some libraries from PsychoPy
from psychopy import visual, core, event, data, sound
import os
import itertools
import random
import json

###
### Experiment data
###
output_dir = os.path.join(os.path.expanduser("~"),"Documents", "Dartmouth", "wheatlab",
                          "universal_contours", "output")
sub_id = raw_input("Enter subject_id: ")
subject_dir = os.path.join(output_dir,str(sub_id))

if not os.path.exists(subject_dir):
    sub_dict = {}
    os.mkdir(subject_dir)
    age = raw_input("age: ")
    sub_dict["Age"] = age
    gender = raw_input("gender: ")
    sub_dict["Gender"] = gender
    date = raw_input("date: ")
    sub_dict["Date"] = date

    sub_dict_path = os.path.join(subject_dir, 'subject_info.json')
    with open(sub_dict_path, 'w') as f:
        json.dump(sub_dict, f, sort_keys=True, indent=4)

# get number of runs:
num_runs = input("Number of runs: ")


###
### Do all the setting up
###

#create a window
mywin = visual.Window([1000,750], color=(255,255,255), monitor="testMonitor")

#keep track of the mouse
mouse = event.Mouse(visible=True)
buttons = mouse.getPressed()

#the 'sad' or 'angry' buttons
sad_button = visual.Rect(mywin, width=150, height=50, units='pix',
                              lineColor=(0,0,0), lineColorSpace='rgb255',
                              pos=(-250,-220), fillColor = (255,255,255),
                              fillColorSpace = 'rgb255')
sad_button_text = visual.TextStim(mywin, text="Sad", color=(0,0,0),
                                       colorSpace='rgb255', pos=(-0.5,-0.586),
                                       height=0.075)

angry_button = visual.Rect(mywin, width=150, height=50, units='pix',
                             lineColor=(0,0,0), lineColorSpace='rgb255',
                             pos=(250,-220), fillColor = (255,255,255),
                             fillColorSpace = 'rgb255')
angry_button_text = visual.TextStim(mywin, text="Angry", color=(0,0,0),
                                      colorSpace='rgb255', pos=(0.5,-0.586),
                                      height=0.075)

# the play button for sounds
play_button_text = visual.TextStim(mywin,text="Click play button to play sound",
                                   color=(0,0,0), colorSpace='rgb255',
                                   pos=(0,0.2), height=0.05)
button_vertices = [[-20,33],[-20,-13],[20,10]]
play_button = visual.ShapeStim(mywin, units = 'pix', vertices = button_vertices,
                               lineColor=(0,0,0),lineColorSpace = 'rgb255',
                               pos = (0,0), fillColor = (255,255,255),
                               fillColorSpace = 'rgb255')

# another sound related button - for testing mostly
noSound_button_text = visual.TextStim(mywin,text="Could not hear sound",
                                   color=(0,0,0), colorSpace='rgb255',
                                   pos=(0,-300), height=20, units = 'pix')
noSound_button = visual.Rect(mywin, width=200, height=30, units='pix',
                             lineColor=(0,0,0), lineColorSpace='rgb255',
                             pos=(0,-300), fillColor = (255,255,255),
                             fillColorSpace = 'rgb255')

# Set the stimulus directory
stimulus_dir = os.path.join(os.path.expanduser("~"),"Documents", "Dartmouth",
                            "wheatlab","universal_contours", "STIMULI")

###
### Show instruction screen
###
instructions = ("In the following task, you will be presented with either visual"
                + " or auditory stimuli. For each, click the button at the"
                + " bottom of the screen that best fits. Sounds may be played"
                + " more than once.\n\n\n Click the button to start")
instruction_text = visual.TextStim(mywin,text=instructions,
                                   color=(0,0,0), colorSpace='rgb255',
                                   pos=(0,100), height=20, units = 'pix',
                                   wrapWidth = 500)
continue_text = visual.TextStim(mywin,text="Start",
                                   color=(0,0,0), colorSpace='rgb255',
                                   pos=(0,-50), height=20, units = 'pix')
continue_button = visual.Rect(mywin, width=150, height=50, units='pix',
                             lineColor=(0,0,0), lineColorSpace='rgb255',
                             pos=(0,-50), fillColor = (255,255,255),
                             fillColorSpace = 'rgb255')
ready = False
while not ready:
    instruction_text.draw()

    continue_button.draw()
    continue_text.draw()

    mywin.flip()
    if mouse.isPressedIn(continue_button, buttons=[0]):
        continue_button.setFillColor(color = (225,225,225), colorSpace='rgb255')
        instruction_text.draw()

        continue_button.draw()
        continue_text.draw()
        mywin.flip()

        core.wait(0.2)
        ready = True

###
### Now present the stimuli
###

for run in range(num_runs):

    order_data_path = os.path.join(subject_dir, 'NA_presentation_order_data_run'
                                                + str(run) + '.json')
    order_data = open(order_data_path, 'w')
    stim_dict = {}

    stim_response_path = os.path.join(subject_dir, 'NA_stim_response_data_run'
                                                   + str(run)+ '.json')
    stim_response = open(stim_response_path, 'w')
    response_dict = {}

    # getting some random order of bins
    image_zscore = random.sample(range(13), 13)
    sound_zscore = random.sample(range(13), 13)

    # getting random order of stimuli
    indices = random.sample(range(26),26)
    image_types = ["LC", "PS"]
    sound_types = ["LFO", "SAW", "ROS"]

    # pick the generator method for stimuli
    for index in range(26):
        if (index < 12):
            stim_dict[indices[index]] = (image_types[index%2],
                                         image_zscore[index])
        if (index == 12):
            stim_dict[indices[index]] = (image_types[random.randint(0,1)],
                                         image_zscore[index])
        if (index > 12) and (index < 25):
            stim_dict[indices[index]] = (sound_types[index%3],
                                         sound_zscore[index%13])
        if (index == 25):
            stim_dict[indices[index]] = (sound_types[random.randint(0,2)],
                                         sound_zscore[index%13])

    # run through trials (one image/sound)
    for trial in range(26):
        choice = False

        # get info about stimuli for this trial
        method = stim_dict[trial][0]
        zscore = stim_dict[trial][1]
        if method == "LFO" or method == "SAW" or method == "ROS":
            stim_type = "sounds"
        else: stim_type = "images"

        # get some random file of specified type
        method_dir = os.path.join(stimulus_dir, stim_type, str(zscore), method)
        file = os.path.join(method_dir,random.choice(os.listdir(method_dir)))

        #update the dictionary with the specific file
        stim_dict[trial] = file

        if stim_type == "sounds":
            soundClip = sound.Sound(file, secs = 2)

        if stim_type == "images":
            blob = visual.ImageStim(mywin, image=file, pos=(0,.25))

        #draw the stimuli and wait for choice
        while (choice == False):
            if stim_type == "images":
                blob.draw()

            if stim_type == "sounds":
                play_button = visual.ShapeStim(mywin, units = 'pix',
                                               vertices = button_vertices,
                                               lineColor=(0,0,0),
                                               lineColorSpace = 'rgb255',
                                               pos = (0,0),
                                               fillColor = (255,255,255),
                                               fillColorSpace = 'rgb255')
                play_button_text.draw()
                play_button.draw()

                noSound_button.setFillColor(color = (255,255,255),
                                            colorSpace='rgb255')
                noSound_button.draw()
                noSound_button_text.draw()

            sad_button.setFillColor(color = (255,255,255), colorSpace='rgb255')
            sad_button.draw()
            sad_button_text.draw()

            angry_button.setFillColor(color = (255,255,255), colorSpace='rgb255')
            angry_button.draw()
            angry_button_text.draw()

            mywin.flip()

            if mouse.isPressedIn(sad_button, buttons=[0]):
                sad_button.setFillColor(color = (225,225,225),
                                             colorSpace='rgb255')
                if stim_type == "images":
                    blob.draw()
                if stim_type == "sounds":
                    soundClip.stop()

                sad_button.draw()
                sad_button_text.draw()

                angry_button.draw()
                angry_button_text.draw()

                mywin.flip()

                mouse.clickReset()
                core.wait(.2)

                response_dict[file] = "Sad"
                choice = True

            if mouse.isPressedIn(angry_button, buttons=[0]):
                angry_button.setFillColor(color = (225,225,225),
                                            colorSpace='rgb255')
                if stim_type == "images":
                    blob.draw()
                if stim_type == "sounds":
                    soundClip.stop()

                angry_button.draw()
                angry_button_text.draw()

                sad_button.draw()
                sad_button_text.draw()

                mywin.flip()

                mouse.clickReset()
                core.wait(.2)

                response_dict[file] = "Angry"
                choice = True

            if mouse.isPressedIn(play_button, buttons=[0]):
                play_button = visual.ShapeStim(mywin, units = 'pix',
                                               vertices = button_vertices,
                                               lineColor=(0,0,0),
                                               lineColorSpace = 'rgb255',
                                               pos = (0,0),
                                               fillColor = (225,225,225),
                                               fillColorSpace = 'rgb255')
                play_button.draw()
                play_button_text.draw()

                noSound_button.draw()
                noSound_button_text.draw()

                angry_button.draw()
                angry_button_text.draw()

                sad_button.draw()
                sad_button_text.draw()

                mywin.flip()

                mouse.clickReset()
                core.wait(0.2)
                soundClip.play()

            if mouse.isPressedIn(noSound_button, buttons = [0]):
                soundClip.stop()
                play_button.draw()
                play_button_text.draw()

                sad_button.draw()
                sad_button_text.draw()

                angry_button.draw()
                angry_button_text.draw()

                noSound_button.setFillColor(color = (225,225,225), colorSpace='rgb255')
                noSound_button.draw()
                noSound_button_text.draw()

                mywin.flip()

                mouse.clickReset()
                core.wait(0.2)

                response_dict[file] = "NONE"
                choice = True


    ###
    ### write data to files
    ###
    json.dump(stim_dict, order_data, sort_keys=True, indent=4)
    json.dump(response_dict, stim_response, sort_keys=True, indent=4)

    # close files
    order_data.close()
    stim_response.close()


#cleanup
mywin.close()
core.quit()
