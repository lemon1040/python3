from channels.generic.websocket import AsyncWebsocketConsumer
import json


class HallConsumer(AsyncWebsocketConsumer):
    """"
    用户登录后进入游戏大厅
    用户发送邀请请求后，把被邀请人的id在组内广播，自己退出大厅进入名字为自己ID的房间
    """
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['userId']
        self.room_group_name = 'hall'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        print(message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))