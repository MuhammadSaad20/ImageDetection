import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk1
from PIL import ImageTk,Image
from tkinter import filedialog
import json
from watson_developer_cloud import VisualRecognitionV3
# -> import boto3

import random
import string
# -> import firebase_admin
# -> from firebase_admin import credentials
import pyrebase



def imagedet():

    root=tk1.ThemedTk()
    root.geometry('600x500')
    root.title("Food AI")
    root.get_themes()
    root.set_theme('equilux')

    label=Label(root,text='FOOD AI\nImage Detection Module Window',bd=1,relief='solid',font="Helvetica 20",background='#800080',anchor=N)
    label.pack()
    #te=tk.Text(root,height=5,width=35)
    #te.config(state='normal')
    #te.insert(tk.INSERT,"     FOOD AI IMAGE DETECTION    ")



    def browsefunc():
        filename = filedialog.askopenfilename()
        pathlabel = tk.Label(text=filename)
        pathlabel.pack()
        print(filename)
        print(type(filename))
        te = tk.Text(root, width=55, height=3,fg='#0a0000',bg='#d4c207',font='Helvetica 10',bd=1,relief='solid',padx=5,pady=5)

        config = {
           //write you own api key
        }
        # -> cred = credentials.Certificate("foodai-20f94-firebase-adminsdk-ykq31-3ef9b3822f.json")
        # ->firebase=firebase_admin.initialize_app(cred)

        firebase = pyrebase.initialize_app(config)

        storage = firebase.storage()

        fl = list()
        for i in range(1, 22):
            fl.append(i)
        fs = string.ascii_letters
        fn1 = random.choice(string.ascii_letters)
        fn2 = random.choice(fl)
        # ->print(fn1)
        # ->print(fn2)
        # ->print(type(fn2))
        fn = str(fn2) + fn1
        # -> print(type(fn))
        cloudpath = 'FoodAIUserData/' + str(fn) + '.jpg'
        #localpath = 'C:/Users/HP-PC/Desktop/Testdata/cat.jpg'
        localpath=filename
        visual_recognition = VisualRecognitionV3(
            'vwrite your own ersion',
            iam_apikey='write your own api key')

        with open(localpath, 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
                classifier_ids='DefaultCustomModel_1321097124').get_result()
        m = json.dumps(classes, indent=5)
        # -> print(a)
        # -> print(type(a))
        # -> print(type(classes))

        # ->print(classes.values())
        # -> print(classes.keys())
        k = classes['images']
        # -> print(k)
        # ->print(type(k))
        k = str(k)
        k = k.split(':')
        # ->print(k)
        a = " []}], 'image'"
        if (k[4] == a):
            answer="sorry our model is not recognized these image please help us to improve we save your food image to our server so next time we improve our results"
            print('sorry our model is not recognized these image '
                  'please help us to improve we save your food image to our server so next time we improve our results')
            storage.child(cloudpath).put(localpath)
        elif (k[4] != a):
            b = k[5]
            b = b.split(',')
            # ->print(b[1])
            l = " 'score'"
            if (b[1] == l):
                answer=b[0]
                print(b[0])
            elif (b[1] != l):
                answer = "sorry our model is not recognized these image please help us to improve we save your food image to our server so next time we improve our results"
                print('sorry our model is not recognized these image '
                      'please help us to improve we save your  food image to our server so next time we improve our results')
                storage.child(cloudpath).put(localpath)


        te.config(state='normal')
        te.delete(1.0,tk.END)
        te.insert(tk.INSERT,answer)
        te.config(state='disabled')
        te.pack()

    button1 = ttk.Button(root, text="Browse Image",command=browsefunc)
    button1.pack(side=BOTTOM)


    root.mainloop()



root=tk1.ThemedTk()
root.geometry('1000x500')
root.title("Food AI")
root.get_themes()
root.set_theme('equilux')


canvas=Canvas(root,width=1000,height=500)
image=ImageTk.PhotoImage(Image.open('C:/Users/HP-PC/Desktop/Myweb/ww.png'))
img=canvas.create_image(0,0,anchor=NW,image=image)


w=ttk.Label(canvas,text="FOOD AI",image=image,font='Helvetica 50 bold',compound='center')

button1 = ttk.Button(canvas, text="Food Chat..")
button1.pack(in_=canvas,side=BOTTOM)
button2 = ttk.Button(canvas, text="Food Image",command=imagedet)
button2.pack(in_=canvas,side=BOTTOM)
w.pack()
canvas.pack()


root.mainloop()
