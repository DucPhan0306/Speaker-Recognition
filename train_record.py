"Record audio for training"
import pyaudio
import wave
import os.path

# Record data---------------------------------------------------------------------
def record_data(x,RECORD_SECONDS = 31):          # x = File name input
        CHUNK = 1024                             # (2^11) Specifies the number of frames per buffer.
        FORMAT = pyaudio.paInt16                 # 16 bit int
        CHANNELS = 2                             # Number of channels
        RATE = 16000                             # Sampling rate
        p = pyaudio.PyAudio()

        # Create directory of speaker
        path1 = "D:\\Speaker-Recognition\\data_set\\"+x+"-"+"\\wav"    
        try: 
            os.makedirs(path1)     
        except:
            print("Directory already exists!!")

        i=1
        while("TRUE"):
            fname=path1+"\\"+x+str(i)+".wav"
            # Check file already exists??
            if os.path.isfile(fname):                                             
                i+=1
            else:
                break
        fname =path1+"\\"+x+str(i)+".wav"

        # open stream
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,input_device_index=0)
        print("* recording")

        frames = []
        
        # read data
        for i in range(0, int(RATE / CHUNK * int(RECORD_SECONDS))):                # vd: RECORD_SECONDS = 31 -> (0,484)
            data = stream.read(CHUNK)                                              # append 484 times     
            frames.append(data) 
        print("* done recording")
        
        # stop stream
        stream.stop_stream()
        stream.close()
        p.terminate()                                                              # close Pyaudio
        
        wf = wave.open(fname, 'wb')                                                # write only
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))        # Nối chuỗi các khung data trong frames lại với khoảng trắng ở giữa mỗi khung data                                     
        wf.close()
        i+=1
        return fname

