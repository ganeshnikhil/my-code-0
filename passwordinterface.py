import random
import pandas as pd
import pyttsx3
import time
import base64



speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
speaker.setProperty('rate', 140)    # Speed percent (can go over 100)
speaker.setProperty('volume', 0.7)    # volume 0-1
count=0


o_password='c2hzZGt2Z2w='
a=o_password.encode("UTF-8")    
a1=base64.b64decode(a)
a2=a1.decode("UTF-8")                  
hint="".join(random.sample(a2,3))


while True:
    entry=input("enter your password:")
# Encoding the string into bytes
    b = entry.encode("UTF-8")
# Base64 Encode the bytes
    e = base64.b64encode(b)
# Decoding the Base64 bytes to string
    s1 = e.decode("UTF-8")
    if s1==o_password:
        #data = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/kepler-exoplanets-dataset/exoTrain.csv')
        #data=pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/project-3/sample_csv_file.csv")
        print("fetching...............")
        data=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
        print(data.head(60))
        speaker.say("hello sir!")
        speaker.say("welcome to your employe database")
        speaker.runAndWait()


    else:
        time.sleep(0.5)
        print("HINT:",hint)
        speaker.say("oops")
        speaker.say("your password is invalid!")
        speaker.runAndWait()
    count=count+1


    if count==4 or s1=='c2hzZGt2Z2w=':
        time.sleep(0.9)
        speaker.say("fuck off ,bhainchooda,mother chooda")
        speaker.say("thanks for using our service..")
        speaker.runAndWait()
        print(exit())