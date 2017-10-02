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

order_data_path = os.path.join(subject_dir, 'PA_presentation_order_data.json')
order_data = open(order_data_path, 'w')
stim_dict = {}

stim_response_path = os.path.join(subject_dir, 'PA_stim_response_data.json')
stim_response = open(stim_response_path, 'w')
response_dict = {}


###
### Do all the setting up
###

#create a window
mywin = visual.Window([1000,750], color=(255,255,255), monitor="testMonitor")

#keep track of the mouse
mouse = event.Mouse(visible=True)
buttons = mouse.getPressed()

#the 'a' or 'b' buttons
positive = ["Peaceful", "Excited"]
negative = ["Sad", "Angry"]

placement = random.randint(0,1)
a_button = visual.Rect(mywin, width=150, height=50, units='pix',
                              lineColor=(0,0,0), lineColorSpace='rgb255',
                              pos=(-250,-220), fillColor = (255,255,255),
                              fillColorSpace = 'rgb255')
a_button_text = visual.TextStim(mywin, text=positive[placement], color=(0,0,0),
                                       colorSpace='rgb255', pos=(-0.5,-0.586),
                                       height=0.075)

b_button = visual.Rect(mywin, width=150, height=50, units='pix',
                             lineColor=(0,0,0), lineColorSpace='rgb255',
                             pos=(250,-220), fillColor = (255,255,255),
                             fillColorSpace = 'rgb255')
b_button_text = visual.TextStim(mywin, text=positive[abs(placement-1)], color=(0,0,0),
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

# getting some random order to present stimuli (z-score bins)
order = random.sample(range(13), 13)
#print order

# Set the stimulus directory
stimulus_dir = os.path.join(os.path.expanduser("~"),"Documents", "Dartmouth",
                            "wheatlab","universal_contours", "STIMULI")

# generating random positions that will be sound/image
# there will be 6 of one and 7 of the other, pick that randomly too
# and then make sure that there are equal generators of each
indices = random.sample(range(13),13)

if random.randint(0,2) == 0:
    for i in range(13):
        if i < 4:
            stim_dict[indices[i]] = "LC"
        if i >= 4 and i < 7:
            stim_dict[indices[i]] = "PS"
        if i >= 7 and i < 9:
            stim_dict[indices[i]] = "LFO"
        if i>=9 and i < 11:
            stim_dict[indices[i]] = "SAW"
        if i >= 11:
            stim_dict[indices[i]] = "ROS"

else:
    for i in range(13):
        if i < 3:
            stim_dict[indices[i]] = "LFO"
        if i >= 3 and i < 5:
            stim_dict[indices[i]] = "SAW"
        if i >= 5 and i < 7:
            stim_dict[indices[i]] = "ROS"
        if i>= 7 and i < 10:
            stim_dict[indices[i]] = "LC"
        if i >= 10:
            stim_dict[indices[i]] = "PS"

#print stim_dict


###
### Now present the stimuli
###

for trial in range(13):
    choice = False
    zscore = order[trial]
    #print zscore

    method = stim_dict[trial]
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

    #draw the stimuli and update the window
    while (choice == False): #this creates a never-ending loop
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


        a_button.setFillColor(color = (255,255,255), colorSpace='rgb255')
        a_button.draw()
        a_button_text.draw()

        b_button.setFillColor(color = (255,255,255), colorSpace='rgb255')
        b_button.draw()
        b_button_text.draw()

        mywin.flip()

        if mouse.isPressedIn(a_button, buttons=[0]):
            a_button.setFillColor(color = (225,225,225), colorSpace='rgb255')
            if stim_type == "images":
                blob.draw()
            if stim_type == "sounds":
                soundClip.stop()

            a_button.draw()
            a_button_text.draw()

            b_button.draw()
            b_button_text.draw()

            mywin.flip()

            mouse.clickReset()
            core.wait(.2)

            response_dict[file] = positive[placement]
            choice = True

        if mouse.isPressedIn(b_button, buttons=[0]):
            b_button.setFillColor(color = (225,225,225), colorSpace='rgb255')
            if stim_type == "images":
                blob.draw()
            if stim_type == "sounds":
                soundClip.stop()

            b_button.draw()
            b_button_text.draw()

            a_button.draw()
            a_button_text.draw()

            mywin.flip()

            mouse.clickReset()
            core.wait(.2)

            response_dict[file] = positive[abs(placement-1)]
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

            b_button.draw()
            b_button_text.draw()

            a_button.draw()
            a_button_text.draw()

            noSound_button.draw()
            noSound_button_text.draw()

            mywin.flip()

            mouse.clickReset()
            core.wait(0.2)
            soundClip.play()

        if mouse.isPressedIn(noSound_button, buttons = [0]):
            soundClip.stop()
            play_button.draw()
            play_button_text.draw()

            b_button.draw()
            b_button_text.draw()

            a_button.draw()
            a_button_text.draw()

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


#cleanup
mywin.close()
order_data.close()
stim_response.close()
core.quit()
