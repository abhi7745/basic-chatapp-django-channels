# Real time communication with django channels and websockets:-
 - Channels is a server
 - Websockets is a client

## Four Key Steps:-

- 1. Configure ASGI - asynchronous server gateway interface(django)
- 2. Consumers - channels version of django views
- 3. Routing - handle url routing for this consumers

- 4. Websockets - builtin js websocket api on the client side to initiate the handshake, 
   and create an open connection between our client and server.

## Quick start:-
   1. ```pip install channels```

   2. Add 'channels' to INSTALLED_APPS in settings.py
   ```bash
      INSTALLED_APPS = [
         'channels',
         ...
      ]
   ```

   3. asgi.py to add these lines:-
      ```bash
         from channels.routing import ProtocolTypeRouter, URLRouter # channels setup
         from channels.auth import AuthMiddlewareStack # channels setup
         import chatapp.routing # channels setup
         
         application = ProtocolTypeRouter({
            'http': get_asgi_application(),
            'websocket' : AuthMiddlewareStack(
               URLRouter(
                     chatapp.routing.websocket_urlpatters
               )
            )
         })
      ```

   4. settings.py to add these code after INSTALLED_APPS
      ```ASGI_APPLICATION = 'project_name.asgi.application'```

   5. Create a websocket script in the html file
   ```bash
      <script>
        let url = `ws://${window.location.host}/ws/socker-server/`
        console.log(url)

        const chatSocket = new WebSocket(url)

        chatSocket.onmessage = function(e){
            let data = JSON.parse(e.data)
            console.log('Data', data)
            
        }

      </script>
   ```

   6. create a 'consumers.py' file in the app directory and add these codes below:
   ```bash
      import json
      from channels.generic.websocket import WebsocketConsumer

      class ChatConsumer(WebsocketConsumer):
         def connect(self):
            self.accept()

            self.send(text_data=json.dumps({
                  'type' : 'connection_established',
                  'message': 'You are now connected!'
            }))
   ```

   7. create a 'routing.py' file in the app directory and add these codes below:
   ```bash
   from django.urls import re_path

   from . import consumers

   websocket_urlpatters = [
      re_path(r'ws/socker-server/', consumers.ChatConsumer.as_asgi())
   ]
   ```

   8. Migrate the database ```python manage.py migrate```
