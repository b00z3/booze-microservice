import os

from sanic import Sanic, request, response
from sanic.response import json
from sanic_cors import CORS, cross_origin
import predictor
import iowa_predictor
import json as j 

app = Sanic(__name__)
cors = CORS(app)
port = os.environ.get('PORT', 8000)
app.config['CORS_HEADERS'] = 'Content-Type'

test_team = [{'age': 19, 'gender': 'Male', 'married': False},
 {'age': 19, 'gender': 'Male', 'married': True},
 {'age': 57, 'gender': 'Female', 'married': True},
 {'age': 57, 'gender': 'Female', 'married': True}]

@app.route("/" , methods=['POST'])
@cross_origin(app)
async def test_fanction(request):
    answer = married_to_bool(request.json)
    predicted_sentences = predictor.get_answers(answer)
    return response.json({'answer': predicted_sentences})
    
@app.route("/" , methods=['OPTIONS'])
@cross_origin(app)
async def test_fanction(request):
    return response.json({'looks':'good'})

@app.route("/iowa" , methods=['POST'])
@cross_origin(app)
async def test_fanction(request):
    answer = married_to_bool(request.json)
    predicted_sentences = iowa_predictor.get_answers(answer)
    return response.json({'answer': predicted_sentences})

@app.route("/iowa" , methods=['OPTIONS'])
@cross_origin(app)
async def test_fanction(request):
    return response.json({'looks':'good'})

def married_to_bool(team):
    for i in team:
        i['married'] = i['married'] == 'Married' 
    return team    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)



