import cv2
import os 
import time
import numpy as np
import sys

VIDEO_PATH = "media/badapple.mp4"


CHARS = np.array(list(" .:-=+*#%@"))

def frame_to_ascii(frame, width=100):
    h, w = frame.shape[:2]
    aspect = h / w
    new_h = int(width * aspect * 0.55)

    frame = cv2.resize(frame, (width, new_h), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    idx = (gray / 255 * (len(CHARS) - 1)).astype(np.int32)
    return "\n".join("".join(CHARS[row]) for row in idx)


def main():
    cap = cv2.VideoCapture(VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    delay = 1.0 / fps

    sys.stdout.write("\x1b[2J")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        ascii_frame = frame_to_ascii(frame, 100)
        sys.stdout.write("\x1b[H")
        sys.stdout.write(ascii_frame)
        sys.stdout.flush()


        time.sleep(delay)

    cap.release()

if __name__ == "__main__":
    main()
