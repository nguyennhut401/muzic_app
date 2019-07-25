from channels.generic.websocket import AsyncWebsocketConsumer

import json

class TableStatus(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'table_updating'
        self.room_group_name = 'singal_%s'%self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        package = json_data.get('package')

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'broadcast_message',
            'message': package
        })


    async def broadcast_message(self, text_data):
        await self.send(text_data=json.dumps(text_data))