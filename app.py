import requests
from flask import Flask, render_template, request
import petpy
import constants

app = Flask(__name__, template_folder='templates')


@app.route('/')
def landing_page():
    """Landing page with user search form"""
    return render_template('homepage.html')


@app.route('/about/')
def about_me():
    """Page for project information"""
    return render_template('about.html')


@app.route('/pet-services', methods=['GET'])
def services():
    """Page for users to search for clinics, groomers, or other services for their pets."""
    return render_template('pet_services.html')


@app.route('/pet-services-results', methods=['GET'])
def pet_services():
    """Page for users to search for clinics, groomers, or other services for their pets."""

    # getting arguments from html form
    services_type = request.args.get('service')
    zipcode = request.args.get('zipcode')
    distance = int(request.args.get('distance'))
    params = {'zip_code': zipcode, 'radius_miles': distance, 'keywords': [services_type]}

    # send those arguments to a request from partner's microservice, receive response back
    response = requests.get("http://127.0.0.1:5000/places_api", params=params)
    data = response.json()

    # put response in pet services result
    for business in data:
        name = business['name']
        rating = business['rating']
        distance = business['distance_miles']
        place_id = business['place_id']
    return render_template('pet_services_results.html', data=data)


@app.route('/search-results', methods=['GET'])
def search_results():
    """Page showing results for pets available for adoption"""

    pf = petpy.Petfinder(key=constants.API_KEY,
                         secret=constants.API_SECRET)

    # getting data from html form
    pet_type = request.args.get('type')
    zipcode = request.args.get('zipcode')
    distance = int(request.args.get('distance'))

    # sending request to petfinder api
    response = pf.animals(animal_type=pet_type, location=zipcode, distance=distance, results_per_page=12)

    # response from api
    animal_list = []
    for i in range(len(response["animals"])):
        animal_dict = dict()
        animal_dict['name'] = response["animals"][i]['name']
        if response["animals"][i]['primary_photo_cropped'] is not None:
            animal_dict['photo'] = response["animals"][i]['primary_photo_cropped']['small']
        else:
            animal_dict['photo'] = 'static/paw-print.jpg'
        animal_dict['url'] = response["animals"][i]['url']
        animal_dict['gender'] = response["animals"][i]['gender']
        animal_dict['age'] = response["animals"][i]['age']
        animal_dict['description'] = response["animals"][i]['description']
        animal_list.append(animal_dict)

    return render_template('search_results.html', animals=animal_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3800, debug=True)
