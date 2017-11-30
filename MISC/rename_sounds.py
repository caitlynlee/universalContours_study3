# Code to pick and rename 10 of the total generated sounds

import os
import shutil
import itertools
import random

cwd = os.getcwd()


for sc in range(1,14):

    scDir = os.path.join(cwd,"sounds",str(sc*150))

    print scDir
    ros_count = 0
    saw_count = 0
    lfo_count = 0

    for file in os.listdir(scDir):
        #    print file
        if file.find("Ros") != -1:
            #        print "found ROS"
            shutil.move(os.path.join(scDir,file),os.path.join(scDir,"ROS_" + str(ros_count)))
            ros_count += 1
            continue

        elif file.find("SAW") != -1:
            #        print "found SAW"
            shutil.move(os.path.join(scDir,file), os.path.join(scDir,"SAW_" + str(saw_count)))
            saw_count += 1
            continue

        else:
            #   print "found LFO"
            shutil.move(os.path.join(scDir,file), os.path.join(scDir,"LFO_" + str(lfo_count)))
            lfo_count += 1
            continue



    ros_choices = random.sample(range(ros_count), 10)
    saw_choices = random.sample(range(saw_count), 10)
    lfo_choices = random.sample(range(lfo_count), 10)

    #picking 10 random ros sounds:
    for num in range(10):
        ros = ros_choices[num]
        ros_file = "ROS_" + str(ros)
        shutil.move(os.path.join(scDir, ros_file), os.path.join(scDir, "ROS" + str(num)))

    #10 random saw sounds
    for num2 in range(10):
        saw = saw_choices[num2]
        saw_file = "SAW_" + str(saw)
        shutil.move(os.path.join(scDir, saw_file), os.path.join(scDir,"SAW" + str(num2)))

    #10 random lfo sounds
    for num3 in range(10):
        lfo = lfo_choices[num3]
        lfo_file = "LFO_" + str(lfo)
        shutil.move(os.path.join(scDir, lfo_file), os.path.join(scDir, "LFO" + str(num3)))


    for file in os.listdir(scDir):
        if file.find("_") != -1:
            os.remove(os.path.join(scDir,file))
