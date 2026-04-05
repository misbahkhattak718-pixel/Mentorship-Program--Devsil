
import cv2
 
# --- SETTINGS ---
video_path = "./Practice/01_python_first/VID-20250214-WA0015.mp4"
output_file = 'VID-20250214-WA0015.mp4'
 
# --- VIDEO INPUT and OUTPUT ---
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, size, isColor=False)
 
# --- PROCESS FRAMES ---
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Convert to grayscale and write to output
    out.write(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
 
# --- CLEAN UP ---
cap.release()
out.release()
print(f"Grayscale video saved to {output_file}")

# Display the original and processed video side by side
cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    combined = cv2.hconcat([frame, cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)])
    cv2.imshow('Original (Left) vs Grayscale (Right)', combined)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# stop these videos and close the windows
cap.release()
cv2.destroyAllWindows