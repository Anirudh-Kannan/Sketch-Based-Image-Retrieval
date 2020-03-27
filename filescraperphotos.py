import os
import shutil

classes = os.listdir('/home/anirudh/srfp/rendered_256x256/256x256/sketch/tx_000100000000/')

source = '/home/anirudh/srfp/rendered_256x256/256x256/photo/tx_000100000000/'

for i in classes:
    files = os.listdir(source+i+'/test')
    os.mkdir('/home/anirudh/srfp/Training_Test/images_test/'+i)
    for j in files:
        shutil.copy(source + i + '/test/'+j,'/home/anirudh/srfp/Training_Test/images_test/'+i)
