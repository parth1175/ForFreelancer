import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Url, db_drop_and_create_all
import re
from bs4 import BeautifulSoup
import sys


def insert_readings(urlValue, companyName, description):
    toBeInserted = Url(urlValue, companyName, description)
    toBeInserted.insert()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    """ uncomment at the first time running the app """
    # db_drop_and_create_all()

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({'message': 'Hello,hello, World!'})


    @app.route("/movies", methods=['GET', 'POST'])
    def get_movies():
        if(request.method == 'POST'):
            #do this
            reqs = request.get_data().decode('utf-8')

            try:
                reqs[:10]
                username = reqs.split('\n', 1)[0] ####################################
                print(username)
                rest = reqs.split('\n', 1)[1]

                url = rest.split('\n', 1)[0] #######################################
                print(url)
                text = rest.split('\n', 1)[1]

                notes = text.split('\n', 1)[0] #############################
                print(notes)
                htmlText = text.split('\n', 1)[1]


                result = re.search('<title>(.*)| LinkedIn</title>', htmlText)
                try:
                    companyJob = result.group(1)
                    companyJob = companyJob[5:]
                    companyJob = companyJob[:-18]
                except AttributeError:
                    companyJob = result

                print(companyJob)
                job = (companyJob.split('|', 1)[0])[:-1] ################################
                company = (companyJob.split('|', 1)[1])[1:] ###############################
                print(job)
                print(company)


                num1 = htmlText.find('<!----> <span>')
                num2 = htmlText.find('<!----> </span>', num1)

                print(num1)
                print(num2)
                print("size of text is: ")
                print(sys.getsizeof(htmlText))

                soup = BeautifulSoup(htmlText[num1:num2], 'html.parser')
                subtext = soup.get_text('\n','\n\n')
                subtext2 = subtext.replace('\n', ' ') #####################################
                print(subtext2)

                insert_readings(url, companyJob, subtext2)


                return jsonify(
                    {
                        "success": True,
                        "url": reqs[:10]
                    }
                ), 200
            except KeyError:
                raise JsonInvalidError()

        else:
            try:
                urls = Url.query.order_by(Url.id).all()
                url=[]
                url=[mov.url for mov in urls]
                return jsonify(
                    {
                        "success": True,
                        "url": url
                    }
                ), 200
            except:
                abort(500)


    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500
    return app

app = create_app()
if __name__ == '__main__':
    # migrate = Migrate(app, db)
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port,debug=True)
