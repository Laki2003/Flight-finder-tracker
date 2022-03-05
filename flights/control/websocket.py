import json
from channels.generic.websocket import WebsocketConsumer

class Control(WebsocketConsumer):
    def connect(self):
        self.accept()
    
    def disconnect(self, close_node):
        pass

    def receive(self, number):
        flightNumber = json.loads(number)['flightNumber']

        self.send(flightNumber = json.dumps({
            'flightNumber': flightNumber
        }))
        

    
