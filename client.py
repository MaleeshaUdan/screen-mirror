#pip install pyautogui opencv-python numpy

import socket
import cv2
import pickle
import struct

def receive_screen_stream(client_socket):
    data = b""
    payload_size = struct.calcsize("L")

    while True:
        while len(data) < payload_size:
            data += client_socket.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        cv2.imshow('Screen Mirror', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def connect_to_screen_stream_server(host='192.168.1.70', port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    try:
        receive_screen_stream(client_socket)
    except Exception as e:
        print('Error:', e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    connect_to_screen_stream_server(host='192.168.1.70', port=5000)
