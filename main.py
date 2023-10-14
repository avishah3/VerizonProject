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

# Sample questions
questions = [
    {"text": "How would you rate the quality of this product?", "value": 3},
    {"text": "How satisfied are you with our service?", "value": 4},
    {"text": "How likely are you to buy from us again?", "value": 5}
]

current_question_index = 0

# Set up a label to display the question
question_label = tk.Label(app, text="", font=("Arial", 16))
question_label.pack(pady=20)

# Set up the slider
slider = tk.Scale(app, from_=1, to_=5, orient=tk.HORIZONTAL, length=200, sliderlength=20)
slider.pack(pady=5, padx=20)

def display_question():
    # Clear previous question and slider
    question_label.config(text=questions[current_question_index]['text'])
    slider.set(questions[current_question_index]['value'])

def submit_answer():
    global current_question_index

    # Here you can save, process, or print the answer.
    print(f"{questions[current_question_index]['text']}: {slider.get()}")

    # Move to the next question
    current_question_index += 1
    if current_question_index < len(questions):
        display_question()
    else:
        # All questions answered
        print("All questions answered.")
        app.quit()

# Display the first question initially
display_question()

# Button to submit answer and display next question
btn = customtkinter.CTkButton(app, text="Submit", command=submit_answer, font=("Arial", 14))
btn.pack(pady=20)

app.mainloop()
