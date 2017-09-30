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

order_data_path = os.path.join(subject_dir, 'Match_presentation_order_data.json')
order_data = open(order_data_path, 'w')
stim_dict = {}

stim_response_path = os.path.join(subject_dir, 'Match_stim_response_data.json')
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

#the rating scale
mark = visual.TextStim(mywin, text='|', color=(0,0,0), colorSpace='rgb255')
ratingScale = visual.RatingScale(mywin, low=1, high=200, marker = mark,
                                 markerColor = 'Black', scale = None,
                                 tickMarks = None, tickHeight = 0,
                                 labels = ('Not at all', 'Perfectly matched'),
                                 showValue = False, lineColor = 'LightGray',
                                 stretch = 2.5, markerExpansion = 0.5,
                                 textColor = 'Black', showAccept = False)

# the play button for sounds
play_button_text = visual.TextStim(mywin,text="Click play button to play sound",
                                   color=(0,0,0), colorSpace='rgb255',
                                   units = 'pix', pos=(-200,150), height=16)
button_vertices = [[-20,33],[-20,-13],[20,10]]

# Set the stimulus directory
stimulus_dir = os.path.join(os.path.expanduser("~"),"Documents", "Dartmouth",
                            "wheatlab","universal_contours", "STIMULI")

# Pick the order of the images and the sounds
image_zscore_order = random.sample(range(13),13)
sound_zscore_order = random.sample(range(13),13)

present_pairs = [("LC", "LFO"), ("LC", "SAW"), ("LC", "ROS"),
                 ("PS", "LFO"), ("PS", "SAW"), ("PS", "ROS")]

present_order = []
rand_order = random.sample(range(12),12)
for i in range(12):
    present_order.append(present_pairs[rand_order[i]%6])
present_order.append(present_pairs[random.randint(0,5)])


###
### Do the drawings
###
for trial in range(13):
    # pick an image file
    image_zscore = image_zscore_order[trial]
    image_type = present_order[trial][0]
    image_dir = os.path.join(stimulus_dir, "images",
                             str(image_zscore), image_type)
    image_file = os.path.join(image_dir, random.choice(os.listdir(image_dir)))

    # pick a sound file
    sound_zscore = sound_zscore_order[trial]
    sound_type = present_order[trial][1]
    sound_dir = os.path.join(stimulus_dir, "sounds",
                             str(sound_zscore), sound_type)
    sound_file = os.path.join(sound_dir, random.choice(os.listdir(sound_dir)))

    # making the stimuli
    blob = visual.ImageStim(mywin, image=image_file, units = 'pix',
                            pos=(150,120))
    soundClip = sound.Sound(sound_file, secs = 2)

    # adding files presented to dictionary
    stim_dict[trial] = (image_file, sound_file)

    # draw and wait for response
    while ratingScale.noResponse:
        blob.draw()
        play_button = visual.ShapeStim(mywin, units = 'pix',
                                       vertices = button_vertices,
                                       lineColor=(0,0,0),
                                       lineColorSpace = 'rgb255',
                                       pos = (-200,100),
                                       fillColor = (255,255,255),
                                       fillColorSpace = 'rgb255')
        play_button_text.draw()
        play_button.draw()

        ratingScale.draw()

        mywin.flip()

        if mouse.isPressedIn(play_button, buttons=[0]):
            blob.draw()
            play_button = visual.ShapeStim(mywin, units = 'pix',
                                           vertices = button_vertices,
                                           lineColor=(0,0,0),
                                           lineColorSpace = 'rgb255',
                                           pos = (-200,100),
                                           fillColor = (225,225,225),
                                           fillColorSpace = 'rgb255')
            play_button.draw()
            play_button_text.draw()

            ratingScale.draw()


            mywin.flip()

            mouse.clickReset()
            core.wait(0.2)
            soundClip.play()

    # add response to dictionary
    response_dict[trial] = ratingScale.getRating()/2
    ratingScale.reset()

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
