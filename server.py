import asyncio
import websockets
import deepcut
import json

async def tokenize(websocket, path):
    try:
        while True:
            text = await websocket.recv()
            toks = deepcut.tokenize(text)
            await websocket.send(json.dumps(toks))
    except websockets.exceptions.ConnectionClosed as e:
        print("CLOSE")

start_server = websockets.serve(tokenize, 'localhost', 8881)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
