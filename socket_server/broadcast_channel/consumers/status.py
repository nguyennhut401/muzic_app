from channels.generic.websocket import AsyncWebsocketConsumer

class DeviceStatus(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = 'device-status'
        self.room_group_name = 'socket-%s'%self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        return super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):
        return super().receive(text_data=text_data, bytes_data=bytes_data) 

    async def signal_message(self, text_data):
        pass

