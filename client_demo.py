import asyncio
import websockets

async def tokenize():
    async with websockets.connect(
            'ws://localhost:8881') as websocket:
        for text in ["ฉันกินไก่ในบ้าน", "กากกา"]:
            await websocket.send(text)
            print(text)
            toks = await websocket.recv()
            print(toks)

asyncio.get_event_loop().run_until_complete(tokenize())
