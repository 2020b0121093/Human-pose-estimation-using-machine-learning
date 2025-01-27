import cv2
import mediapipe as mp
#Initialize MediaPipe Pose
mp_pose =mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils  #For drawing landmarks
# Capture Video: Replace with 'path_to_video.mp4' for a file or 0 for webcam
video_source = 0 #0 for live webcam, or replace with video file path
#cap = cv2.VideoCapture (video_source)
cap= cv2.VideoCapture ("C:/Users/admin/Downloads/my pics/WhatsApp Video 2022-01-28 at 02.58.34.mp4")
#Set video resolution for webcam (optional, adjust as needed for your laptop)
cap.set (cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set (cv2.CAP_PROP_FRAME_HEIGHT, 480)
# Initialize MediaPipe Pose
with mp_pose. Pose (static_image_mode=False, model_complexity=0, enable_segmentation=False, min_de)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video capture ended.")
            break
