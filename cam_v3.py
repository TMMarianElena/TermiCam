import cv2
import numpy as np

# Configuration
CHARS = "@#S%?*+;:,.. "
WIDTH, HEIGHT = 100, 40
MATRIX_MODE = True
ALPHA = 0.3  # 1.0 = No blur | 0.1 = Heavy ghosting/trail

cap = cv2.VideoCapture(0)
last_frame = None

print("TermiCam: Motion Edition Running...")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Basic Pre-processing
    frame = cv2.flip(cv2.resize(frame, (WIDTH, HEIGHT)), 1).astype(float)

    # 2. Motion Blur Logic (Weighted Average)
    if last_frame is None:
        last_frame = frame
    else:
        # Blending the current frame with the last one
        frame = cv2.addWeighted(frame, ALPHA, last_frame, 1.0 - ALPHA, 0)
        last_frame = frame

    # 3. Render Loop
    output = "\033[H"
    for row in frame.astype(np.uint8): # Convert back to int for rendering
        for pixel in row:
            b, g, r = pixel
            brightness = int(0.299*r + 0.587*g + 0.114*b)
            char = CHARS[brightness // 22]
            
            if MATRIX_MODE:
                # Custom neon green for motion
                color = f"\033[38;2;0;{max(100, brightness)};0m"
            else:
                color = f"\033[38;2;{r};{g};{b}m"
                
            output += f"{color}{char}"
        output += "\n"
    
    print(output + "\033[0m", end="")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()