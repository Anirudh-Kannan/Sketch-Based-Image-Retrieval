import os
import shutil
import re

classes = os.listdir('/home/anirudh/srfp/rendered_256x256/256x256/sketch/tx_000100000000/')
source = '/home/anirudh/srfp/rendered_256x256/256x256/sketch/tx_000100000000/'


for i in classes: 
    files = os.listdir(source+i+'/invalid')
    os.mkdir('/home/anirudh/srfp/Training_Test/sketches_invalid/'+i)
    for j in files:
        shutil.copy(source + i + '/invalid/'+j,'/home/anirudh/srfp/Training_Test/sketches_invalid/'+i)