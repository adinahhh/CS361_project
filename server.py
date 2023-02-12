import zmq
import time
import petpy
import constants
import json

# for microservice
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv_json()
    print(f"Received request: {message}")
    print("this is location: ", message["zipcode"])
    print("this is distance: ", message["distance"])
    time.sleep(3)

    pf = petpy.Petfinder(key=constants.API_KEY, secret=constants.API_SECRET)
    response = pf.animals(location=str(message["zipcode"]), distance=int(message["distance"]), results_per_page=int(10))

    # build response back to user
    animal_list = []
    for i in range(len(response["animals"])):
        animal_dict = dict()
        animal_dict['name'] = response["animals"][i]['name']
        animal_dict['url'] = response["animals"][i]['url']
        animal_dict['gender'] = response["animals"][i]['gender']
        animal_dict['age'] = response["animals"][i]['age']
        animal_dict['description'] = response["animals"][i]['description']
        animal_list.append(animal_dict)

    json_response = json.dumps(animal_list)

    #  Send the reply back to client
    socket.send_json(json_response)
