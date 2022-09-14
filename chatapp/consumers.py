import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type' : 'connection_established',
            'message': 'You are now connected!'
        }))




    
    # def receive(self, text_data=None, bytes_data=None):
    #     return super().receive(text_data, bytes_data)

    # def disconnect(self, code):
    #     return super().disconnect(code)