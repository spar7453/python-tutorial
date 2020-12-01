import asyncio
import websockets

async def message():
  async with websockets.connect("ws://127.0.0.1:5432") as socket:
    msg = input("input:")
    await socket.send(msg)
    print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
