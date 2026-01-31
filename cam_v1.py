import cv2
import os

# Configuration
CHARS = "@#S%?*+;:,.. "
WIDTH = 100  # Adjust based on your terminal size
HEIGHT = 40  # Adjust based on your terminal size

def get_color_escape(r, g, b):
    """Returns the ANSI escape code for the given RGB color."""
    return f"\033[38;2;{r};{g};{b}m"

cap = cv2.VideoCapture(0)

print("TermiCam Running...")
print("Controls: 'q' to Quit | 's' to Save Snapshot")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize and flip for 'mirror' effect
    frame = cv2.flip(cv2.resize(frame, (WIDTH, HEIGHT)), 1)
    
    output = "\033[H" # Reset cursor to top-left
    
    for row in frame:
        for pixel in row:
            b, g, r = pixel
            brightness = int(sum(pixel) / 3)
            char = CHARS[brightness // 22]
            # Combine color + character
            output += f"{get_color_escape(r, g, b)}{char}"
        output += "\n"
    
    print(output + "\033[0m", end="") # Print and reset color

    # Key Listeners
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        with open("snapshot.txt", "w") as f:
            # Clean version without color codes for the file
            f.write(output.replace("\033[H", "")) 
        print("\n[!] Snapshot saved to snapshot.txt")

cap.release()
cv2.destroyAllWindows()
print("\033[2J\nTermiCam session ended.")