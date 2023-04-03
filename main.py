# ====================================Importing Packages===========================================
from tkinter import *
from moviepy.editor import VideoFileClip, AudioFileClip
from tkinter.filedialog import *
from tkinter.messagebox import *

root = Tk()
root.geometry("1100x550")
root.title("YouTube Downloader")
root.configure(bg='white')

# ====================================Global Variables=====================================================

def audio_func():
    def my_func():
        global my_dir
        my_dir = askopenfilename()

    my_func()


def video_func():
    def my_func_1():
        global my_dir_1
        my_dir_1 = askopenfilename()

    my_func_1()

# ====================================Concat Function======================================================

def concat_func():
    if my_dir == '' and my_dir_1 != '':
        showinfo("Message", "Audio File")
    elif (my_dir_1 == '' and my_dir != ''):
        showinfo("Message", 'Please select Video File')
    elif (my_dir_1 == '' and my_dir == ''):
        showinfo("Message", 'Please select Audio and Video File to continue..')
    else:
        audio_clip = AudioFileClip(my_dir)
        video_clip = VideoFileClip(my_dir_1)
        abd = asksaveasfilename()
        print(abd)
        concat_both = video_clip.set_audio(audio_clip)
        concat_both.write_videofile(abd)

# =======================================Labels========================================================

title_label = Label(root, width=30, height=3, font='Helvetica 25 bold', text='Audio Video Synchronization')
title_label.place(x=270, y=75)

# ========================================Buttons=======================================================

b_1 = Button(root, width=12, height=1, font='Helvetica 15 bold', text='Select Audio', command=audio_func)
b_1.place(x=300, y=275)

b_2 = Button(root, width=12, height=1, font='Helvetica 15 bold', text='Select Video', command=video_func)
b_2.place(x=650, y=275)

b_3 = Button(root, width=12, height=1, font='Helvetica 15 bold', text='Synchronize', command=concat_func)
b_3.place(x=475, y=350)

root.mainloop()
