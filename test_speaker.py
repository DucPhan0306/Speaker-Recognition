
import os
import pickle
import numpy as np
import sys
import numpy
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
numpy.set_printoptions(threshold=sys.maxsize)

def test():
    #path to training data
    source   = "data_set\\"   
    modelpath = "speaker_models\\"

    """ test_file = "data_set_test.txt"
    file_paths = open(test_file,'r') """

    gmm_files = [os.path.join(modelpath,fname) for fname in 
                os.listdir(modelpath) if fname.endswith('.gmm')]

    #Load the Gaussian gender Models
    models = [pickle.load(open(fname,'rb')) for fname in gmm_files]
    print("models",models)
    speakers = [fname.split("\\")[-1].split(".gmm")[0] for fname 
                in gmm_files] 

    """ for path in file_paths:
        path = path.strip()
        print(path)
        sr,audio = read(source + path)
        vector   = extract_features(audio,sr)
        log_likelihood = np.zeros(len(models)) 
        for i in range(len(models)):
            gmm    = models[i]         #checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()

        winner = np.argmax(log_likelihood)
        print ("Speaker is: ", speakers[winner]) """

    path = "testfile.wav"
    sr,audio = read(path)
    vector   = extract_features(audio,sr)
    print(vector)
    print(vector.shape)
    log_likelihood = np.zeros(len(models)) 
    for i in range(len(models)):
        gmm    = models[i]         #checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()

    print("log_likelihood:\n",log_likelihood)
    winner = np.argmax(log_likelihood)
    print("winner",winner)
    print ("Speaker is: ", speakers[winner])
    result = speakers[winner]
    return result
    # time.sleep(1.0)
