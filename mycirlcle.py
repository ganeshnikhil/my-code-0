
import time
import pyttsx3
speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
speaker.setProperty('rate', 160)    # Speed percent (can go over 100)
speaker.setProperty('volume', 0.5)    # volume 0-1
my_circle=['harsh','parimal','mangal','aditya','kartik','anand','ankesh','kunal gaurav','ahsish','ankur','shivam',
           'harsh bardhan','subham','satyam','subham ramdri','golu','ravi kishan','kunal','abhishek',
           'ankush','ankit','nihal','hari om','sanu','raja','uttkarsh','shivam ramdri','angadh','tushar',
           'aman','rohit','lla','gatu','mihir arya','batu','anshu','sneh saurav','raman','arnav','ankur',
           'abhishek dantu','alok','rohan','aditya','sudhanshu','monu','sonu','akash','parth']


speaker.say("hello sir")
time.sleep(0.3)
speaker.say("welcome to your circle database")


while True:
  print("[enter exit in input for exit]")
  my_input=input("enter the name here:")

  for i in range(len(my_circle)):
    if my_input[0]==my_circle[i][0]:
      print(my_circle[i])
     
  time.sleep(0.5)
  speaker.say("total name in your circle=")
  a=len(my_circle)
  a=str(a)
  speaker.say(a)


  if my_input in my_circle:
    speaker.say("given input in your circle")
    time.sleep(0.5)
    speaker.say("position of your input is")
    b=my_circle.index(my_input)
    name=my_circle[b]
    b=str(b)
    speaker.say(b)
    name=str(name)
    speaker.say("name of your input is")
    speaker.say(name)

  else:
    speaker.say("input not found")
    time.sleep(0.8)
    speaker.say("may be this input is a unknown person")
    time.sleep(0.8)
    speaker.say("enter another name")
    time.sleep(0.8)
    speaker.say("or enter exit when done")
  speaker.runAndWait()
  if my_input=='exit':
    print(exit())



  