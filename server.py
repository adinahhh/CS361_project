import os

from flask import Flask, render_template
# from petpy import Petfinder

app = Flask(__name__, template_folder='templates')


@app.route('/')
def landing_page():
    """Landing page with user search form"""
    return render_template('homepage.html')


@app.route('/about/')
def about_me():
    """Page for project information"""
    return render_template('about.html')


@app.route('/search-results')
def search_results():
    """Page showing results for pets available for adoption"""
    return render_template('search_results.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3800))
    print("this is the port number found: ", port)
    app.run(port=port)
    # app.run(debug=True, host='0.0.0.0')
