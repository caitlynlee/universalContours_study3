# Moving into directories based on generating method

import os
import shutil

type = "sounds"

cwd = os.getcwd()
type_dir = os.path.join(cwd, "STIMULI", type)

for zscore in range(13):
    if type == "images":
        zscore_dir = os.path.join(type_dir, str(zscore))

        LC_dir = (os.path.join(type_dir, str(zscore), "LC"))
        #print LC_dir
        if not os.path.exists(LC_dir):
            os.mkdir(LC_dir)
        PS_dir = (os.path.join(type_dir, str(zscore), "PS"))
        #print PS_dir
        if not os.path.exists(PS_dir):
            os.mkdir(PS_dir)

        for file in os.listdir(zscore_dir):
            if os.path.isdir(os.path.join(zscore_dir, file)):
                continue

            if file.find("LC") != -1:
                shutil.move(os.path.join(zscore_dir, file),
                            os.path.join(LC_dir, file))
            elif file.find("PS") != -1:
                shutil.move(os.path.join(zscore_dir, file),
                            os.path.join(PS_dir, file))

    if type =="sounds":
        zscore_dir = os.path.join(type_dir, str(zscore))

        LFO_dir = (os.path.join(type_dir, str(zscore), "LFO"))
        if not os.path.exists(LFO_dir):
            os.mkdir(LFO_dir)

        SAW_dir = (os.path.join(type_dir, str(zscore), "SAW"))
        if not os.path.exists(SAW_dir):
            os.mkdir(SAW_dir)

        ROS_dir = (os.path.join(type_dir, str(zscore), "ROS"))
        if not os.path.exists(ROS_dir):
            os.mkdir(ROS_dir)

        for file in os.listdir(zscore_dir):
            if os.path.isdir(os.path.join(zscore_dir, file)):
                continue

            if file.find("LFO") != -1:
                shutil.move(os.path.join(zscore_dir, file),
                            os.path.join(LFO_dir, file))

            elif file.find("SAW") != -1:
                shutil.move(os.path.join(zscore_dir, file),
                            os.path.join(SAW_dir, file))

            elif file.find("ROS") != -1:
                shutil.move(os.path.join(zscore_dir, file),
                            os.path.join(ROS_dir, file))
