import os
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import messagebox  # Import messagebox

# Initialize the app
app = ctk.CTk()
app.geometry("1000x750")
app.title("Task Manager Layout")

# Set appearance mode and theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Set the app icon using a .png file
try:
    logopath = ImageTk.PhotoImage(file=os.path.join("assets", "media", "app_icon.png"))
    iconpath = ImageTk.PhotoImage(file=os.path.join("assets", "media", "app_icon.png"))
    app.iconphoto(False, logopath)
    app.iconbitmap(False, iconpath)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load icon: {e}")
    print(f"Failed to load icon: {e}")

# Create the main frame
main_frame = ctk.CTkFrame(app, width=1000, height=750)
main_frame.pack(fill="both", expand=True)

# Create a side frame for the tabs (menu buttons)
side_frame = ctk.CTkFrame(main_frame, width=200, height=750)
side_frame.pack(side="left", fill="y")

# Function to handle tab selection (change button color)
def select_tab(selected_button):
    # Reset all buttons to transparent background
    for b in button_list:
        b.configure(fg_color="transparent", text_color="white")

    # Set selected button to a light gray color
    selected_button.configure(fg_color="#3a3a3a")

# Create buttons for each tab on the left side
buttons = [
    "Processes", "Performance", "App history", "Startup apps", "Users", "Details", "Services"
]

button_list = []
for button_text in buttons:
    button = ctk.CTkButton(
        side_frame,
        text=button_text,
        width=180,
        height=50,
        anchor="w",
        fg_color="transparent",  # Make button transparent by default
        text_color="white",
        hover_color="#3a3a3a",  # Gray hover effect
        command=lambda b=buttons: select_tab(b)  # Corrected lambda function
    )
    button.pack(pady=5, padx=10, anchor="w")
    button_list.append(button)

# Create a settings button at the bottom
settings_button = ctk.CTkButton(
    side_frame, text="Settings", width=180, height=50, anchor="w",
    fg_color="transparent", text_color="white", hover_color="#3a3a3a"
)
settings_button.pack(side="bottom", pady=10, padx=10, anchor="w")

# Create a content frame on the right side for the content of each tab
content_frame = ctk.CTkFrame(main_frame, width=800, height=750)
content_frame.pack(side="right", fill="both", expand=True)

# Example content for the Performance tab (can be updated for other tabs)
performance_label = ctk.CTkLabel(content_frame, text="Performance tab content", font=("Arial", 24))
performance_label.pack(pady=20)

# Select the default tab
select_tab(button_list[1])  # Automatically select "Performance" tab

# Start the app
app.mainloop()
