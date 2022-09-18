from email import message
from http import client
import json
from channels.generic.websocket import WebsocketConsumer

from asgiref.sync  import async_to_sync

class ChatConsumer(WebsocketConsumer):

    # initialize channels connection
    def connect(self):

        print('client connected')

        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name, # automatically create by channels
        )
        self.accept()

        self.scope['abcd'] = 'Robin hood'

        print(self.scope['abcd'])




        # count = getattr(self.channel_layer, self.room_group_name, 0)
        # if not count:
        #     setattr(self.channel_layer, self.room_group_name, 1)
        # else:
        #     setattr(self.channel_layer, self.room_group_name, count + 1)
        # print(count,' count')

        # # sending data to client(html page)
        # self.send(text_data=json.dumps({
        #     'type' : 'connection_established',
        #     'message': 'You are now connected!'
        # }))

    # data sending from client side
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message : ', message)

        # sending response back to client(html page)
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':message
            }
        )

    def chat_message(self, event):
        message = event['message']

        # print(message,"event['message']")

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message':message
        }))

    # def disconnect(self):
    #    print('client disconnected')
    #    count = getattr(self.channel_layer, self.room_group_name, 0)
    #    setattr(self.channel_layer, self.room_group_name, count - 1)
    #    if count == 1:
    #         delattr(self.channel_layer, self.room_group_name)