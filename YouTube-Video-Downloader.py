from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

window = Tk()
line = "\n"
window.title("YouTube Video Downloader")

window.geometry("500x400")

imgicon = PhotoImage(file="youtube.png")
imglabel = Label(window,image=imgicon)
imglabel.place(x=20,y=15)

titlelabel = Label(window,text='YouTube Video Downloader',font='Consolas 17 bold' ,fg='red')
titlelabel.place(x=70,y=7)

def cleartext():
	print("Okk")
	entry.delete(0, END)

label = Label(window,text='YouTube Video URL',font='Consolas 10 bold',fg='black')
label.place(x=10,y=100) 

entry = Entry(window,fg='black',font='Consolas 10')
entry.place(x=200,y=100)

button2 = Button(window,text='Clear',fg='black',bg='red',font='Consolas 10 bold', command=cleartext)
button2.place(x=410,y=100)

label2 = Label(window,text='Video Resolusion',font='Consolas 10 bold',fg='black')
label2.place(x=10,y=170)

x = IntVar()

def select():
	if (x.get() == 0):
		print('360p')
	elif (x.get() == 1):
		print('720p')
	elif (x.get() == 2):
		print('1080p')
	else:
		print("Pleaase select !")

radio1 = Radiobutton(window,text='360p',variable=x,value=0,font='Consolas 10 bold',fg='black', command=select)
radio2 = Radiobutton(window,text='720p',variable=x,value=1,font='Consolas 10 bold',fg='black', command=select)
radio3 = Radiobutton(window,text='1080p',variable=x,value=2,font='Consolas 10 bold',fg='black', command=select)

radio1.place(x=200,y=170)
radio2.place(x=305,y=170)
radio3.place(x=410,y=170)

def download():
	if (len(entry.get()) != 0 and len(entry2.get()) != 0):
		link = entry.get()
		yt = YouTube(link)
		
		print("Title : ", yt.title)
		print("Views : ", yt.views)

		print(x.get())

		if (x.get() == 0):
			yd = yt.streams.first().download(entry2.get())
			print("360p")
		elif (x.get() == 1):
			yd = yt.streams.filter(res="360p").first().download(entry2.get())
			print("720p")
		elif (x.get() == 2):
			yd = yt.streams.get_highest_resolution().download(entry2.get())
			print("1080p")
		else:
			print("Please select !")
		messagebox.showinfo(title='Message',message='YouTube video download successful !')
	else:
		print("Enter Please")
		messagebox.showinfo(title='Warning message',message='Please enter above filled :(')

def dir_location():
	print("Okk")
	filename = filedialog.askdirectory()
	print(filename)
	entry2.insert(0, filename)

label3 = Label(window,text='Path Location',font='Consolas 10 bold',fg='black')
label3.place(x=10,y=250)

entry2 = Entry(window,fg='black',font='Consolas 10')
entry2.place(x=200,y=250)

button3 = Button(window,text='Choose',fg='black',bg='red',font='Consolas 10 bold',command=lambda:dir_location())
button3.place(x=410,y=244)
                                           
button = Button(window,text='Download',fg='black',bg='red',font='Consolas 10 bold',command=download)
button.place(x=200,y=350)

window.mainloop()