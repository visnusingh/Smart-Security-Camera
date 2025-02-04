import tkinter as tk
from tkinter import filedialog
import cv2
import time
import datetime
import os
import numpy as np

OUTPUT_DIR = "smart-security"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_video (video_source=0) :
    background_subtractor =  cv2.createBackgroundSubtractorMOG2()
    recording = False
    recorded_frames = []
    start_time = None

    video_capture = cv2.VideoCapture (video_source)
    if not video_capture.isOpened ():
        print ("Error opening video source.")
        return

    while True:
        ret, frame =  video_capture.read()
        if not ret:
            break

        gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
        mask = background_subtractor.apply (gray)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) )
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False
        total_motion_area = 0
        for contour in contours:
            area = cv2.contourArea (contour)
            if area > 100:
                x, y, w, h = cv2.boundingRect (contour)
                cv2.rectangle (frame,  (x, y), (x + w, y + h), (0, 255, 0), 2)
                total_motion_area += area
                motion_detected = True 

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        cv2.putText (frame, timestamp,  (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText (frame, f"Motion: {total_motion_area}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if motion_detected and not recording:
            recording = True
            start_time = time.time()
            recorded_frames = []
            print ("Motion detected! Recording started.")

        if recording:
            recorded_frames.append (frame.copy())
            if time.time() - start_time >= 10: 
                recording = False
                filename = os.path.join(OUTPUT_DIR, f"intrusion_{timestamp}.mp4")
                height, width, _ = recorded_frames[0].shape
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))
                for f in recorded_frames:
                    out.write(f)
                out.release()
                print(f"Recorded: {filename}")

        cv2.imshow("Motion Detection", frame)
        if cv2.waitKey (1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def open_file():
    filepath = filedialog.askopenfilename (title="Select Video File")
    if filepath:
        process_video(filepath)

def start_live():
    process_video() 

root =  tk.Tk()
root.title ("Motion Detection")

record_file_button = tk.Button (root, text="Recorded File Motion", command =open_file)
record_file_button.pack (pady=10)

live_button = tk.Button (root, text  = "Live Motion Detection", command = start_live)
live_button.pack (pady=10)

# %%
root.mainloop()
