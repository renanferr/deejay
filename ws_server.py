#!/usr/bin/env python

import asyncio
import websockets
import json
from config import config
from playback import Track
from ytdl import download_track

class WebsocketServer:
    def __init__(self, addr='localhost', port=8765):
        self._websockets = websockets
        self.addr = addr
        self.port = port
        self.EVENTS = {
            'play track': self._on_play_track
        }

    async def handler_func(self, socket, path):
        async for message in socket:
            event = json.loads(message)
            event_handler = self.EVENTS.get(event.get('name'))
            if event_handler is not None:
                await event_handler(socket=socket, event=event)
            else:
                print('event handler not found for {}'.format(event.get('name')))

    async def _on_play_track(self, socket, event):
        payload = event.get('payload')
        track_url = payload.get('url')
        print(track_url)
        try:
            out_file = config.OUT_TMP
            track_info = download_track(track_url, out_file=out_file, codec=config.CODEC)
            file_path = config.OUT_TMP % dict(id=track_info.get('id'), ext=config.CODEC)
            t = Track(file_path=file_path, codec=config.CODEC, info=track_info)
            print('Playing {}'.format(track_info.get('title')))
            await self.emit(socket, 'playing now', payload={ 'track': track_info })
            t.play()
        except Exception as e:
            print(e)

    async def emit(self, socket, name, payload):
        event = {
                'name': name,
                'payload': payload
        }
        await socket.send(json.dumps(event))

    def start(self):
        start_server = websockets.serve(self.handler_func, self.addr, self.port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()