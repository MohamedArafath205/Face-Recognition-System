import cv2
from simple_facerec import SimpleFacerec
import tkinter as tk
import threading
import webbrowser
from tkinter import ttk

root = tk.Tk()

global run
run = True
cap = None

def run_model():
    global cap
    str = SimpleFacerec()
    str.load_encoding_images('images/')

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while run:
        ret, img = cap.read()
        face_locations, face_names = str.detect_known_faces(img)

        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1  = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow('frame', img)
        key = cv2.waitKey(1) & 0xFF
        
        if key == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
            cap.release()
            cv2.destroyAllWindows()
            break
        
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

def run_thread_model():
    global run
    run = True
    runmodel = threading.Thread(target=run_model)
    runmodel.start()

def stop_model():
    global run, cap
    run = False
    if cap is not None:
        cap.release()
        cap = None
    cv2.destroyAllWindows()
    
    
# tkinter GUI
root.geometry("700x500")
root.title("Face Recognition")
root.resizable(False, False)
root.configure(bg="#ffffff")

# heading
heading = tk.Label(root, text="Face Recognition", bg="#ffffff", fg="#000000", font=("fira code", 23))
heading.place(x=220, y=50)

# Description
description = tk.Label(root, text="By Mohamed Arafath", bg="#ffffff", fg="#000000", font=("fira code", 10))
description.place(x=260, y=100)

# personal website
website = tk.Label(root, text="Check out my website: ", bg="#ffffff", fg="#000000", font=("fira code", 13))
website.place(x=50, y=180)

website_link = tk.Label(root, text="https://mohamedarafath205.github.io/", bg="#ffffff", fg="blue", cursor="hand2", font=("fira code", 13, "underline"))
website_link.bind("<Button-1>", lambda e: webbrowser.open("https://mohamedarafath205.github.io/"))
website_link.place(x=280, y=180)

# linkedin
linkedin = tk.Label(root, text="Connect with me on LinkedIn: ", bg="#ffffff", fg="#000000", font=("fira code", 13))
linkedin.place(x=50, y=220)
linkedin_link = tk.Label(root, text="mohdarafath", bg="#ffffff", fg="blue", cursor="hand2", font=("fira code", 13))
linkedin_link.bind("<Button-1>", lambda e: webbrowser.open("https://www.linkedin.com/in/mohdarafath/"))
linkedin_link.place(x=350, y=220)

# GitHub
github = tk.Label(root, text="Check out my GitHub: ", bg="#ffffff", fg="#000000", font=("fira code", 13))
github.place(x=50, y=260)

github_link = tk.Label(root, text="mohamedarafath205", bg="#ffffff", fg="blue", cursor="hand2", font=("fira code", 13))
github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/mohamedarafath205"))
github_link.place(x=350, y=260)

# email
email = tk.Label(root, text="Email me at: ", bg="#ffffff", fg="#000000", font=("fira code", 13))
email.place(x=50, y=300)

email_link = tk.Label(root, text="mohamedarafath205@gmail.com", bg="#ffffff", fg="blue", cursor="hand2", font=("fira code", 13))
email_link.bind("<Button-1>", lambda e: webbrowser.open("mailto:mohamedarafath205@gmail.com"))
email_link.place(x=200, y=300)

# run button
run_button = ttk.Button(root, text="Run", width=10, cursor="hand2", command=run_thread_model)
run_button.place(x=200, y=450)

# stop button
stop_button = ttk.Button(root, text="Stop", width=10, cursor="hand2", command=stop_model)
stop_button.place(x=440, y=450)

root.mainloop()