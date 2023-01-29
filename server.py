import os
from flask import Flask, render_template, request
from petpy import Petfinder
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


@app.route('/search-results', methods=['GET'])
def search_results():
    """Page showing results for pets available for adoption"""

    pf = Petfinder(key=constants.API_KEY,
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
        animal_dict['url'] = response["animals"][i]['url']
        animal_dict['gender'] = response["animals"][i]['gender']
        animal_dict['age'] = response["animals"][i]['age']
        animal_dict['description'] = response["animals"][i]['description']
        animal_list.append(animal_dict)

    return render_template('search_results.html', animals=animal_list)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3800))
    app.run(port=port)
    # app.run(debug=True, host='0.0.0.0')
