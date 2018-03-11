#import some libraries from PsychoPy
from psychopy import visual, core, event, data, sound
import os
import itertools
import random
import json

def run(subjectID, subjectAge, subjectGender, date):
    ###
    ### Experiment data
    ###
    cwd = os.getcwd()
    output_dir = os.path.join(cwd, "output")
    sub_id = subjectID
    subject_dir = os.path.join(output_dir,str(sub_id))

    # setting up sub info for the first time
    if not os.path.exists(subject_dir):
        sub_dict = {}
        os.mkdir(subject_dir)
        sub_dict["Age"] = str(subjectAge)
        sub_dict["Gender"] = subjectGender
        sub_dict["Date"] = str(date)

        sub_dict_path = os.path.join(subject_dir, 'subject_info.json')
        with open(sub_dict_path, 'w') as f:
            json.dump(sub_dict, f, sort_keys=True, indent=4)

    # get number of runs:
    num_runs = 2

    ###
    ### Do all the setting up
    ###

    #create a window
    mywin = visual.Window([1000,750], color=(255,255,255), monitor="testMonitor")

    #keep track of the mouse
    mouse = event.Mouse(visible=True)
    buttons = mouse.getPressed()

    #the rating scale(s): valence and arousal
    mark = visual.TextStim(mywin, text='|', color=(0,0,0), colorSpace='rgb255')
    valenceRatingScale = visual.RatingScale(mywin, low=1, high=200, marker = mark,
                                     markerColor = 'Black', scale = None,
                                     tickMarks = None, tickHeight = 0,
                                     labels = ('Negative', 'Positive'),
                                     showValue = False, lineColor = 'LightGray',
                                     stretch = 2.5, markerExpansion = 0.5,
                                     textColor = 'Black', showAccept = False)

    arousalRatingScale = visual.RatingScale(mywin, low=1, high=200, marker = mark,
                                     markerColor = 'Black', scale = None,
                                     tickMarks = None, tickHeight = 0,
                                     labels = ('Low energy', 'High Energy'),
                                     showValue = False, lineColor = 'LightGray',
                                     stretch = 2.5, markerExpansion = 0.5,
                                     textColor = 'Black', showAccept = False)

    next_button_text = visual.TextStim(mywin,text="Next",
                                       color=(0,0,0), colorSpace='rgb255',
                                       pos=(0,-280), height=20, units = 'pix')
    next_button = visual.Rect(mywin, width=150, height=50, units='pix',
                                 lineColor=(0,0,0), lineColorSpace='rgb255',
                                 pos=(0,-280), fillColor = (255,255,255),
                                 fillColorSpace = 'rgb255')

    # the play button for sounds
    play_button_text = visual.TextStim(mywin,text="Click play button to play sound",
                                       color=(0,0,0), colorSpace='rgb255',
                                       units = 'pix', pos=(-200,150), height=18)
    button_vertices = [[-20,33],[-20,-13],[20,10]]

    # another sound related button - for testing mostly
    noSound_button_text = visual.TextStim(mywin,text="Could not hear sound",
                                       color=(0,0,0), colorSpace='rgb255',
                                       pos=(-200,0), height=12, units = 'pix')
    noSound_button = visual.Rect(mywin, width=150, height=30, units='pix',
                                 lineColor=(0,0,0), lineColorSpace='rgb255',
                                 pos=(-200,-0), fillColor = (255,255,255),
                                 fillColorSpace = 'rgb255')

    # Set the stimulus directory
    stimulus_dir = os.path.join(os.path.dirname(cwd),'STIMULI')



    ###
    ### Show instruction screen
    ###
    instructions = ("In the following task, you will be presented with some visual"
                    + " or auditory stimuli. Click and drag along the scale at the"
                    + " bottom of the screen to reflect how negative or positive the"
                    + " video or sound is.\n\n\n"
                    + " Click the button to start")
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
    ### Do multiple runs
    ###

    for run in range(num_runs):

        order_data_path = os.path.join(subject_dir,
                        'videoPresentationOrder_run' + str(run) + '.json')
        order_data = open(order_data_path, 'w')
        stim_dict = {}

        stim_response_path = os.path.join(subject_dir,
                            'videoRatings_run' + str(run) + '.json')
        stim_response = open(stim_response_path, 'w')
        response_dict = {}


        # Pick the order of the images and the sounds
        video_zscore_order = random.sample(range(13),13)

        present_order = []

        ###
        ### Do the drawings
        ###
        for trial in range(13):
            # pick an image file
            video_zscore = video_zscore_order[trial]
            video_dir = os.path.join(stimulus_dir, "images",
                                     str(video_zscore))
            video_file = os.path.join(video_dir, random.choice(os.listdir(video_dir)))

            # making the stimuli
            clip = visual.MovieStim(mywin, video_file, loop=false,
                                    units = 'pix',pos=(0,120))

            # adding files presented to dictionary
            stim_dict[trial] = (image_file, sound_file)

            # reset things:
            rating = False

            # draw and wait for response
            while rating == False:
                clip.draw()

                valenceRatingScale.draw()
                arousalRatingScale.draw()

                next_button.setFillColor(color = (255,255,255), colorSpace='rgb255')
                next_button.draw()
                next_button_text.draw()

                mywin.flip()

                if mouse.isPressedIn(next_button, buttons = [0]):
                    next_button.setFillColor(color = (225,225,225), colorSpace='rgb255')
                    next_button.draw()
                    next_button_text.draw()

                    clip.draw()

                    valenceRatingScale.draw()
                    arousalRatingScale.draw()

                    mywin.flip()

                    mouse.clickReset()
                    core.wait(0.2)

                    if valenceRatingScale.getRating() and arousalRatingScale.getRating():
                        rating = True

                        finalValenceRating = valenceRatingScale.getRating()/2
                        finalArousalRating = arousalRatingScale.getRating()/2

            #if sound is still playing, stop
            clip.stop()

            # add response to dictionary, whether or not heard sound
            response_dict[trial] = [finalValenceRating, finalArousalRating]

            valenceRatingScale.reset()
            arousalRatingScale.reset()


            # clean the window
            mywin.flip()


        ###
        ### write data to files
        ###
        json.dump(stim_dict, order_data, sort_keys=True, indent=4)
        json.dump(response_dict, stim_response, sort_keys=True, indent=4)


    finish_text = "End"
    finish = visual.TextStim(mywin, text=finish_text, color=(0,0,0),
                                           colorSpace='rgb255', pos=(0,0),
                                           height=0.075)
    finish.draw()
    mywin.flip()
    core.wait(5)

    #cleanup
    mywin.close()
    order_data.close()
    stim_response.close()
    core.quit()
