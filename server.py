#pip install pyautogui opencv-python numpy

import socket
import cv2
import pickle
import struct
import pyautogui
import numpy as np

def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # Resize the frame to reduce data size
    frame = cv2.resize(frame, (960, 540))  # Adjust resolution as needed
    return frame

def start_screen_stream_server(host='0.0.0.0', port=5000, frame_rate=10):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on port", port)

    client_socket, addr = server_socket.accept()
    print('Connection from:', addr)

    try:
        while True:
            frame = capture_screen()
            data = pickle.dumps(frame, protocol=pickle.HIGHEST_PROTOCOL)
            message_size = struct.pack("L", len(data))
            client_socket.sendall(message_size + data)

            # Control the frame rate
            cv2.waitKey(int(1000 / frame_rate))
    except Exception as e:
        print('Error:', e)
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    start_screen_stream_server()
