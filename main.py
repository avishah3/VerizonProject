import customtkinter
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("red.json")

app = customtkinter.CTk()
app.geometry("1920x1080")

# Image file path (replace with your image file path)
image_file_path = "first frame.png"

# Video file path (rename it to your video file)
video_file_path = "Verizon Intro Better.mp4"

# Function to switch from image to video
def switch_to_video():
    # Remove the image label
    image_label.pack_forget()

    # Create and display the video player
    videoplayer = TkinterVideo(master=app, scaled=True)
    videoplayer.load(video_file_path)
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

# Create a label to display the image
image = Image.open(image_file_path)
image = image.resize((1920, 1080))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(app, image=photo)
image_label.pack(expand=True, fill="both")

# Preload the video in the background
preload_videoplayer = TkinterVideo(master=app)
preload_videoplayer.load(video_file_path)

# Create a central button to trigger the animation
button = customtkinter.CTkButton(master=app, text="Play Video", command=switch_to_video)
button.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()