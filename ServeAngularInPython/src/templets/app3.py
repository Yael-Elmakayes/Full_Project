# # import asyncio
# # import websockets

# # async def echo(websocket, path):
# #     async for message in websocket:
# #         num = int(message)
# #         arr = [num] * 5
# #         await websocket.send(str(arr))

# # asyncio.get_event_loop().run_until_complete(
# #     websockets.serve(echo, 'localhost', 8000))
# # asyncio.get_event_loop().run_forever()


# import asyncio
# import base64
# import json
# import cv2
# import numpy as np
# import websockets

# async def process_frame(websocket, path):
#     async for message in websocket:
#         data = json.loads(message)
#         image_data = data['image']
#         image_data = image_data.split(',')[1]
#         image_bytes = base64.b64decode(image_data)
#         img_bgr = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
#         img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
#         ret, buffer = cv2.imencode('.jpg', img_gray)
#         processed_image_data = base64.b64encode(buffer).decode('utf-8')
#         await websocket.send(json.dumps({'image': processed_image_data}))

# if __name__ == '__main__':
#     start_server = websockets.serve(process_frame, 'localhost', 8000)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()