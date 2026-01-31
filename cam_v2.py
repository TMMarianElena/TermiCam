import cv2
import os

# Configuration
CHARS = "@#S%?*+;:,.. "
WIDTH = 100
HEIGHT = 40
MATRIX_MODE = True  # Set to False for natural color

def get_matrix_color(brightness):
    """Returns shades of green based on pixel brightness."""
    # Darker pixels = dark green, Brighter pixels = neon green
    if brightness > 200:
        return "\033[38;2;150;255;150m" # Near white-green
    elif brightness > 100:
        return "\033[38;2;0;255;0m"     # Pure Matrix green
    else:
        return "\033[38;2;0;100;0m"     # Deep forest green

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(cv2.resize(frame, (WIDTH, HEIGHT)), 1)
    output = "\033[H" 
    
    for row in frame:
        for pixel in row:
            b, g, r = pixel
            brightness = int(0.299*r + 0.587*g + 0.114*b) # Luminance formula
            char = CHARS[brightness // 22]
            
            if MATRIX_MODE:
                color = get_matrix_color(brightness)
            else:
                color = f"\033[38;2;{r};{g};{b}m"
                
            output += f"{color}{char}"
        output += "\n"
    
    print(output + "\033[0m", end="")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()