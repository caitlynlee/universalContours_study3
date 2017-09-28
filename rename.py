import os
import shutil
import itertools
import random

cwd = os.getcwd()


for corners in range(1,14):

    cornerdir = os.path.join(cwd,"images",str(corners))

    print cornerdir
    linecount = 0
    pscount = 0

    for file in os.listdir(cornerdir):
        #    print file
        if file.find("linecurve") != -1:
            #        print "found lc"
            shutil.move(os.path.join(cornerdir,file),os.path.join(cornerdir,"LC_" + str(linecount)))
            linecount += 1
            continue
        
        if file.find("PS") != -1:
            #        print "found PS"
            shutil.move(os.path.join(cornerdir,file), os.path.join(cornerdir,"PS_" + str(pscount)))
            pscount += 1
            continue
        


    lc_choices = random.sample(range(linecount),15)
    ps_choices = random.sample(range(pscount),15)
    #picking 15 random lc images: 
    for num in range(15):
        lc = lc_choices[num]
        lc_file = "LC_" + str(lc)
        shutil.move(os.path.join(cornerdir, lc_file), os.path.join(cornerdir, "LC" + str(num)))

    #15 random ps images
    for num2 in range(15):
        ps = ps_choices[num2]
        ps_file = "PS_" + str(ps)
        shutil.move(os.path.join(cornerdir, ps_file), os.path.join(cornerdir,"PS" + str(num2)))

    

    for file in os.listdir(cornerdir):
        if file.find("_") != -1: 
            os.remove(os.path.join(cornerdir,file))
        
