from fastapi import FastAPI, WebSocket
import cv2
import numpy as np

app = FastAPI()

@app.websocket("/ws")
async def video_stream(websocket: WebSocket):
    await websocket.accept()
    cv2.namedWindow("Video Stream", cv2.WINDOW_NORMAL)

    while True:
            # Receive binary data from the client
            frame_data = await websocket.receive_bytes()

            # Convert the byte data to a NumPy array
            nparr = np.frombuffer(frame_data, np.uint8)

            # Decode the image
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if frame is not None:
                cv2.imshow("Video Stream", frame)

                # Press 'q' to exit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("Received invalid frame")


    cv2.destroyAllWindows()
    await websocket.close()
