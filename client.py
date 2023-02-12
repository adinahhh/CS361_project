import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to my zeromq server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Hello! Welcome to FurFinder. Please tell me your 5 digit zip code.")
zipcode = str(input())
print("How far do you want your search to be from that distance, in miles?")
distance = int(input())

request = {"zipcode": zipcode, "distance": distance}
json_request = json.dumps(request)  # use json loads?
print(f"Sending request {json_request} …")
socket.send_json(request)

#  Get the reply.
message = socket.recv_json()
print(f"Received reply {request} [ {message} ]")
