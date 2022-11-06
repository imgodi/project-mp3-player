from tkinter import *
import pygame # module you have to install first
from tkinter import filedialog # used to open file exploarer
from tkinter import messagebox
import tkinter.font as tkFont
import time 
from mutagen.mp3 import MP3    # to get length of song first instal it
import tkinter.ttk as ttk
from PIL import Image,  ImageTk
from tkinter import colorchooser # for colourpicker
import winsound
# for sliders

#print("Choose colour for background")
messagebox.showinfo("Choose Colour ----","Choose Colour For background")
my_color=colorchooser.askcolor()[1]

root=Toplevel()

root.title('Music Player')
#root.iconbitmap(r"C:\Users\aksshs.AKSSHS-PC\Desktop\Vexels-Office-Mp3-music-player.ico")
root.configure(bg=my_color)
fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
root.geometry("1600x800")

# to turn on pygame initialise
pygame.mixer.init()


# Grab Song Length Time Info
def play_time():
	
	# Check for double timing
	if stopped:
		return
	# Grab Current Song Elapsed Time
	current_time = pygame.mixer.music.get_pos() / 1000

	# throw up temp label to get data
	#slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}')
	# convert to time format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	# Get Currently Playing Song
	#current_song = song_box.curselection()
	#Grab song title from playlist
	song = song_Box.get(ACTIVE)
	# add directory structure and mp3 to song title
	
	# Load Song with Mutagen
	song_mut = MP3(song)
	# Get song Length
	global song_length
	song_length = song_mut.info.length
	# Convert to Time Format
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

	# Increase current time by 1 second
	current_time +=1
	
	if int(my_slider.get()) == int(song_length):
		status_bar.config(text=f'Time Elapsed: {converted_song_length}  of  {converted_song_length}  ')
	elif paused:
		pass
	elif int(my_slider.get()) == int(current_time):
		# Update Slider To position
		slider_position = int(song_length)
		my_slider.config(to=slider_position, value=int(current_time))

	else:
		# Update Slider To position
		
		slider_position = int(song_length)

		my_slider.config(to=slider_position, value=int(my_slider.get()))
		
		# convert to time format
		converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

		# Output time to status bar
		status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

		# Move this thing along by one second
		next_time = int(my_slider.get()) + 1
		my_slider.config(value=next_time)






	# Output time to status bar
	#status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

	# Update slider position value to current song position...
	#my_slider.config(value=int(current_time))
	
	
	# update time
	status_bar.after(1000, play_time)



#add song Function																		#giving file extensions and name 
def add_song():
	#song=filedialog.askopenfilename(initialdir=r"C:\Users\aksshs.AKSSHS-PC\Desktop",title="Choose a Song", filetypes=(("mp3 file", "*.mp3")))            # intialdir to give directory
        song=filedialog.askopenfilename(initialdir="C:/",title="Add a Song",filetypes=(("mp3  files","*.mp3"),))
     
                       
        #adding song to listbox
        song_Box.insert(END, song)
        if song!="":
                messagebox.showinfo("Added Song ----",song)
                messagebox.showinfo("To Play Song","To Play Song, Select Location Of Song In Playlist")
                
        else:
                messagebox.showwarning("Warning ----","No Song Added To Playlist,Please Add Song(s) To Use Mp3 Player")
                
#add many songs
def add_many_songs():
        songs=filedialog.askopenfilenames(initialdir="C:/",title="Add a Song",filetypes=(("mp3  files","*.mp3"),))
        # loop through song list
        for song in songs:
                song_Box.insert(END, song)
        if songs!="":
                messagebox.showinfo("----","Added Many Songs")
                messagebox.showinfo("To Play Songs","To Play Songs, Select Location Of Song In Playlist")
                freq = 3000
                dur=2000
                winsound.Beep(freq, dur)
                messagebox.showwarning("To Change Songs In Playlist","To Change Songs In Playlist First Press Stop Button Then Select Location Of Song") 
        else:
                messagebox.showwarning("Warning ----","No Song(s) Added To Playlist,Please Add Song(s) To Use Mp3 Player")
                

# Play selected song
def play():
	# Set Stopped Variable To False So Song Can Play
	global stopped
	stopped = False
	song = song_Box.get(ACTIVE)
	play_button['state']=DISABLED
	
	

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	# Call the play_time function to get song length
	play_time()

	
        #get current volume
	#current_volume=pygame.mixer.music.get_volume()
	#slider_label.config(text=current_volume*100)

	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)

	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)
	

	

# Stop playing current song
global stopped
stopped = False
def stop():
	# Reset Slider and Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)
	# Stop Song From Playing
	pygame.mixer.music.stop()
	song_Box.selection_clear(ACTIVE)

	# Clear The Status Bar
	status_bar.config(text='')

	# Set Stop Variable To True
	global stopped
	stopped = True

	 
	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)

	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)
	play_button['state']=NORMAL


	



# Delete A Song
def delete_song():
	stop()
	# Delete Currently Selected Song
	song_Box.delete(ANCHOR)
	# Stop Music if it's playing
	pygame.mixer.music.stop()

# Delete All Songs from Playlist
def delete_all_songs():
	stop()
	# Delete All Songs
	song_Box.delete(0, END)
	# Stop Music if it's playing
	pygame.mixer.music.stop()

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause The Current Song
def pause(is_paused):
	global paused
	paused = is_paused

	if paused:
		# Unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		# Pause
		pygame.mixer.music.pause()
		paused = True
		messagebox.showinfo(" Song Paused","To Play Song, Click Pause Button again")
	
# Create slider function
def slide(x):
	#slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
	song = song_Box.get(ACTIVE)
	

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0, start=int(my_slider.get()))
#creting master frame
master_frame=Frame(root)
master_frame.pack(pady=20, padx=30)


#create volume function
def volume(x):
	pygame.mixer.music.set_volume(volume_slider.get())

	# Get current Volume
	current_volume = pygame.mixer.music.get_volume()
	# Times by 100 to make it easier to work with
	current_volume = current_volume * 100
	#slider_label.config(text=current_volume * 100)





	# Change Volume Meter Picture
	if int(current_volume) < 1:
		volume_meter.config(image=vol0)
	elif int(current_volume) > 0 and int(current_volume) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_volume) >= 25 and int(current_volume) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_volume) >= 50 and int(current_volume) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_volume) >= 75 and int(current_volume) <= 100:
		volume_meter.config(image=vol4)	

	






#creating song playlist box
#using Listboxwidget
song_Box=Listbox(master_frame, bg="black", fg="blue",width=60,selectbackground="gray",selectforeground="black",font=fontExample)
song_Box.grid(row=0,column=0)

#create player control buttons
play_button_img=PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\play.png')
#adding png images to button first you need to define them
#forward_button_img=PhotoImage(file=r'C:\Users\aksshs.AKSSHS-PC\Desktop\GUI\project\button images\icons8-fast-forward-50.png')
#backward_button_img=PhotoImage(file=r'C:\Users\aksshs.AKSSHS-PC\Desktop\GUI\project\button images\icons8-rewind-button-round-50 (1).png')
pause_button_img=PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\pause.png')
stop_button_img=PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\stop.png')


# Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\volume0.png')
vol1 = PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\volume1.png')
vol2 = PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\volume2.png')
vol3 = PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\volume3.png')
vol4 = PhotoImage(file=r'C:\Users\imgod\OneDrive\Desktop\GUI\project\mp3 player\button images\volume4.png')


# Create Volume Meter
volume_meter=Label(master_frame, image=vol0)

volume_meter.grid(row=1, column=1, padx=2)





#create player control frame
controls_frame=Frame(master_frame)
controls_frame.grid(row=1,column=0,pady=20)

#create volume label frame
volume_frame=LabelFrame(master_frame,text="Volume")
volume_frame.grid(row=0,column=1,padx=20)

#Create player Control buttons
#borderwidth zero removes grid aroung image
play_button=Button(controls_frame,image=play_button_img, borderwidth=0,command=play)
#forward_button=Button(controls_frame,image=forward_button_img, borderwidth=0,command=forward_ten_seconds)
#backward_button=Button(controls_frame,image=backward_button_img, borderwidth=0,command=back_ten_seconds)
pause_button=Button(controls_frame,image=pause_button_img, borderwidth=0,command=lambda: pause(paused))
stop_button=Button(controls_frame,image=stop_button_img, borderwidth=0,command=stop)

play_button.grid(row=0,column=1,padx=10)
#forward_button.grid(row=0,column=4,padx=10)
#backward_button.grid(row=0,column=0,padx=10)
pause_button.grid(row=0,column=2,padx=10)
stop_button.grid(row=0,column=3,padx=10)
#create menu

my_menu=Menu(root)
root.config(menu=my_menu)

#add song menu\
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)#adding new dropdown menu
add_song_menu.add_command(label="Add One Song To Playlist",command=add_song)
#add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist",command=add_many_songs)
#Delete song menu
remove_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Remove  Songs",menu=remove_song_menu)
remove_song_menu.add_cascade(label="Delete A Song From Playlist",command=delete_song)
remove_song_menu.add_cascade(label="Delete All Songs From Playlist",command=delete_all_songs)


#cREAate staus bar
status_bar=Label(root ,text="",bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X,side=BOTTOM, ipady=2)

# create music position slider
my_slider= ttk.Scale(master_frame, from_=0,to=100, orient=HORIZONTAL, value=0,command=slide,length=360)
my_slider.grid(row=2,column=0,pady=10)

#Volume slider
volume_slider= ttk.Scale(volume_frame, from_=0,to=1, orient=VERTICAL, value=1,command=volume,length=125)
volume_slider.pack(pady=10)


# Create Temporary Slider Label
#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

messagebox.showwarning("Warning ----","No Songs Added To Playlist,Please Add Song(s) To Use Mp3 Player")
root.mainloop()

