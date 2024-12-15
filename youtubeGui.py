from tkinter import *
from yt_dlp import YoutubeDL

def HighQuality():
    try:
        link = myEntry.get()
        ydl_opts={
            "fromat":"best",
            "outtmpl":"downloads%(titles)s.%(est)s"
        }
        with YoutubeDL(ydl_opts)as ydl:
            ydl.download([link])

            print("the vedio has been Download High Quality")
    
    except Exception as e:
        print("Error Download High Quality ")

def LowQuality():
    try:
        link = myEntry.get()
        ydl_opts={
            "fromat":"worst",
            "outtmpl":"downloads%(titles)s.%(est)s"
        }
        with YoutubeDL(ydl_opts)as ydl:
            ydl.download([link])

            print("the vedio has been Download Low Quality")
    
    except Exception as e:
        print("Error Download Low Quality")

def Audio():
    try:
        link = myEntry.get()
        ydl_opts={
            "fromat":"bestaudio",
            "outtmpl":"downloads%(titles)s.%(est)s"
        }
        with YoutubeDL(ydl_opts)as ydl:
            ydl.download([link])

            print("the vedio has been Download Audio Only")
    
    except Exception as e:
        print("Error Download Audio Only")

myFrame=Tk()
myFrame.title("YouTube Video Downloader")
myFrame.geometry("500x300")

myLabel=Label(myFrame,text="Post Link Here :",font="bold")
myLabel.pack(pady=10)

myEntry=Entry(myFrame,width=50)
myEntry.pack(pady=10,padx=8)
button_high = Button(myFrame, text="Download High Quality", command=HighQuality, font=("Arial", 12), bg="red", fg="white",activeforeground="green")
button_high.pack(pady=5)

button_low = Button(myFrame, text="Download Low Quality", command=LowQuality, font=("Arial", 12), bg="blue", fg="white",activeforeground="green")
button_low.pack(pady=5)

button_audio = Button(myFrame, text="Download Audio Only", command=Audio, font=("Arial", 12), bg="green", fg="white",activeforeground="green")
button_audio.pack(pady=5)


myFrame.mainloop()




# def download_video(quality):
#     link = myEntry.get()
    
#     yt=YouTube(link)

#     save_path = "./"  # Default save path in the current directory

#     if quality == "High Quality":
#         stream = yt.streams.get_highest_resolution()
#     elif quality == "Low Quality":
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
#     elif quality == "Audio Only":
#         stream = yt.streams.filter(only_audio=True).first()
#     else:
#         messagebox.showerror("Error", "Invalid quality selection.")
#         return

#     stream.download(save_path)
#     messagebox.showinfo("Success", f"Downloaded successfully to {save_path}")
