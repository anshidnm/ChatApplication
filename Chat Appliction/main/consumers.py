from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatroomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
        # await self.channel_layer.group_send(self.room_group_name,{'type':'tester_message','tester':'Hello world'})
    
    # async def tester_message(self,event):
    #     tester = event['tester']
    #     await self.send(text_data=json.dumps({'tester':tester}))
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    async def receive(self, text_data, bytes_data=None):
        message = json.loads(text_data)['message']
        user_name = json.loads(text_data)['user_name']
        await self.channel_layer.group_send(self.room_group_name,{'type':'chat_message','message':message,'user_name':user_name})

    async def chat_message(self,event):
        message = event['message']
        user_name = event['user_name']
        await self.send(text_data=json.dumps({'message':message,'user_name':user_name}))
