import json

from channels.generic.websocket import AsyncWebsocketConsumer


class CommonWebsocketConsumer(AsyncWebsocketConsumer):
    async def disconnect(self, code):
        self.extra_disconnect()
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        package = json_data.get('package')

        self.extra_receive()
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'signal_message',
                'message': json.dumps(package)
            }
        )

    async def signal_message(self, event):
        message = event.get('message')

        self.send(message)

    def extra_disconnect(self):
        pass

    def extra_receive(self):
        pass
