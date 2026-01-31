import cv2

# Character set from densest to lightest
CHARS = "@#S%?*+;:,.. "

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Resize for the terminal (width, height)
    img = cv2.resize(frame, (100, 40))
    # 2. Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Map pixels to characters
    output = ""
    for row in gray:
        for pixel in row:
            output += CHARS[pixel // 22]
        output += "\n"

    # 4. Print and reset cursor to top
    print("\033[H" + output, end="")

cap.release()