"Train models with 5 sample audio"

import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn import mixture 
from speakerfeatures import extract_features
import warnings
import os
warnings.filterwarnings("ignore")

def train_model(x):
    # j = number file .wav in speaker folder
    list = os.listdir("data_set\\"+x+"-"+"\\wav") 
    j = len(list)
    print(j)

    # write directory of file .wav in file data_set_enroll.txt
    file_paths=open("data_set_enroll.txt" ,'a')
    file_paths_copy=open("data_set_enroll_copy.txt" ,'a')
    i=1
    while i<(j+1):
        file_paths.write(x+"-"+"\\wav\\"+x+str(i)+".wav\n")
        file_paths_copy.write(x+"-"+"\\wav\\"+x+str(i)+".wav\n")
        i+=1
    file_paths.close()

    # path to training data
    source   = "data_set\\"   

    # path where training speakers will be saved
    dest = "speaker_models\\"

    train_file = "data_set_enroll.txt"        
    file_paths = open(train_file,'r')
    count = 1

    # Extracting features for each speaker (5 files per speakers)
    features = np.asarray(())
    for path in file_paths:    
        path = path.strip()   
        print(path)
        
        # read the audio
        sr,audio = read(source + path)
        
        # extract 40 dimensional MFCC & delta MFCC features
        vector   = extract_features(audio,sr)
        
        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))
        # when features of 5 files of speaker are concatenated, then do model training
        if count == j:    
            gmm = mixture.GaussianMixture(n_components = 16, max_iter = 200, covariance_type='diag',n_init = 3)
            gmm.fit(features)
            
            # dumping the trained gaussian model
            picklefile = path.split("-")[0]+".gmm"
            pickle.dump(gmm,open(dest + picklefile,'wb'))
            print ('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)    
            features = np.asarray(())
            count = 0
        count = count + 1
    