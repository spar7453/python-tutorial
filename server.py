import asyncio
import websockets

async def response(websocket: websockets.WebSocketServerProtocol, path: str):
  message = await websocket.recv()
  print(f"Messaged from Clinet: {message}")
  await websocket.send(f"Server ! received message: {message}")

server = websockets.serve(response, '127.0.0.1', 5432)
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()