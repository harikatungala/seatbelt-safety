pip install > requirements.txt
gunicorn app:app
import tkinter as tk

# Function to toggle seatbelt status
def toggle_seatbelt():
    global seatbelt_worn
    seatbelt_worn = not seatbelt_worn  # Toggle the status
    update_status()

# Function to update the seatbelt status on the screen
def update_status():
    if seatbelt_worn:
        status_label.config(text="✅ Seatbelt Detected. Safe to drive!", fg="green")
        status_label.config(font=('Arial', 18, 'bold'))  # Set bold font when safe
    else:
        status_label.config(text="❗ No Seatbelt Detected! Please wear it.", fg="red")
        status_label.config(font=('Arial', 20, 'bold'))  # Make font bigger for warning

# Function to display the college name on the app window


# Create the main window
root = tk.Tk()
root.title("Seatbelt Detector")
root.geometry("500x350")  # Set the window size

# Initialize seatbelt status (True means seatbelt is worn, False means not worn)
seatbelt_worn = True



# Heading for the app
heading_label = tk.Label(root, text="Seatbelt Detector", font=('Arial', 20, 'bold'))
heading_label.pack(pady=10)

# Status label to show seatbelt status
status_label = tk.Label(root, text="Checking Seatbelt...", font=('Arial', 18))
status_label.pack(pady=20)

# Button to simulate seatbelt detection
detect_button = tk.Button(root, text="Simulate Seatbelt Detection", font=('Arial', 14), command=toggle_seatbelt)
detect_button.pack(pady=20)



# Run the app
root.mainloop()
