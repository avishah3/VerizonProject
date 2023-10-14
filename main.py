import customtkinter
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("red.json")

app = customtkinter.CTk()
app.geometry("1920x1080")

# Image file path (replace with your image file path)
image_file_path = "verican first frame.png"

# Video file path (rename it to your video file)
video_file_path = "Verican Animation.mp4"

# Create a label to display the image
image = Image.open(image_file_path)
image = image.resize((1920, 1080))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(app, image=photo)
image_label.pack(expand=True, fill="both")

# Create and configure the video player
videoplayer = TkinterVideo(master=app, scaled=True)
videoplayer.load(video_file_path)
videoplayer.pack(expand=True, fill="both")

# Function to switch from image to video when the button is clicked
def switch_to_video():
    # Remove the image label
    image_label.pack_forget()

    # Play the video
    videoplayer.play()
    button.destroy()


# Create a central button to trigger the video transition
button = customtkinter.CTkButton(master=app, text="Feeling Lost", command=switch_to_video)
button.configure(height=200, width=400, font=("Roboto", 40))
button.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()
