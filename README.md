# CS361_project

## About this project
My project is using PetFinder's API to receive information about pets available for adoption. One part of this project
can be run by calling python3 app.py and will open a web app. The microservices part of this project utilizes
ZeroMQ, an asynchronous messaging library.

## Microservice Communication Contract
___ 
### UML Sequence Diagram
![alt text](https://github.com/adinahhh/CS361_project/blob/main/uml-diagram.png "UML Sequence Diagram")

### Setup
Download and install ZeroMQ server. See [here](https://pypi.org/project/pyzmq/) for instructions.

### How to request data:
Your project should already have the ZeroMQ module imported.
Change your localhost to port 5555. My microservice will be receiving messages from this port.
Then, your project will make a request using ZeroMQ. The request should include a zip code and
distance (in miles). The request should be in this JSON format:
```
request = {"zipcode": "30301", "distance": 15}
```

Making a call and getting a response could look like this:
```
request = {"zipcode": "30301", "distance": 15}
json_request = json.dumps(request)
socket.send_json(request)

message = socket.recv_json()
print(f"Received reply {request} [ {message} ]")
```

### How to send data:
Once my microservice receives your message, it will send back a JSON response in this format:
```
[{"name": "TYLER", "url": "https://www.petfinder.com/dog/tyler-59931916/ga/atlanta/fulton-county-animal-services-ga217/?referrer_id=18777580-e00f-4a0e-afd1-d540ca6d9663", "gender": "Male", "age": "Senior", "description": null}]
```
The JSON response includes a pet's name, url to their profile on PetFinder, gender, age, and a description, if any. The
response above is only one pet. There will be 12 pets total in the response.

### Video Demo
You can view a demo of my project [here](https://media.oregonstate.edu/media/t/1_3kx0ywtc)
