import os
import shutil
import re

test = [ line.rstrip('jpg\n')+'png' for line in open('info/info/testset.txt')] #test set list

er = 0

classes = os.listdir('sketches/sketches')


photo = 'rendered_256x256/256x256/photo/tx_000100000000'
path_txt = 'sketches/sketches'
render = 'rendered_256x256/256x256/sketch/tx_000100000000'

for i in classes:
    
    path_invalid = path_txt+'/' + i + '/invalid.txt'
    path_valid = path_txt+'/' + i + '/checked.txt'

    invalid = [line.rstrip('\n') for line in open(path_invalid)]

    c = 0

    #--------------------------------- TEST VALID -----------------------------------------------

    os.mkdir(render+'/'+ i + '/valid_test')

    testset_path = 'info/info/testset.txt'
    testset = [line.rstrip('.jpg\n') for line in open(testset_path)]

    for k in testset:
        p = k.split('/')
        if p[0] == i:
            try:
                    files = os.listdir(render+'/'+i)
                    for n in files:
                        if n.startswith(p[1]):
                            shutil.move(render+ '/' + i + '/' +n, render+'/'+ i + '/valid_test')  
                    
            except:
                    er+=1



    # ---------------------------------- INVALID ------------------------------------------------------


    os.mkdir(render+'/'+ i + '/invalid')

    for j in invalid:
        if j != 'Unidentifiable/ambiguous':
            if j.startswith('n'):
                try:
                    shutil.move(render+ '/' + i + '/' + j + '.png', render+'/'+ i + '/invalid')  
                except:
                    er+=1
            c+=1
        else:
            c+=1
            break


    #--------------------------------   AMBIGUOUS   ---------------------------------------------------
    os.mkdir(render+'/'+ i + '/ambiguous')

    for j in range(c, len(invalid)):
        if invalid[j].startswith('n'):
            try:
                shutil.move(render+ '/' + i + '/' + invalid[j] + '.png', render+'/'+ i + '/ambiguous')
            except:
                er+=1


    #------------------------------------ VALID -------------------------------------------------------


    rem = os.listdir(render+'/'+i)

    os.mkdir(render+'/'+ i + '/valid')


    for j in rem:
        if j.startswith('n'):
            try:
                shutil.move(render+ '/' + i + '/' + j , render+'/'+ i + '/valid')
            except:
                er+=1

    #----------------------------------------- PHOTO ---------------------------------------------#

    testset_photo = [line.rstrip('\n') for line in open(testset_path)]

    os.mkdir(photo+'/'+i+'/test')
    os.mkdir(photo+'/'+i+'/train')


    for k in testset:
        p = k.split('/')
        if p[0] == i:
            try:
                    files = os.listdir(photo+'/'+i)
                    for n in files:
                        if n.startswith(p[1]):
                            shutil.move(photo+ '/' + i + '/' +n, photo+'/'+ i + '/test')  
                    
            except:
                    er+=1

    files = os.listdir(photo+'/'+i)

    for n in files:
        if n.startswith('n'):
            shutil.move(photo+ '/' + i + '/' +n, photo+'/'+ i + '/train')  

        