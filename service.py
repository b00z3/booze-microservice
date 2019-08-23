import os

from sanic import Sanic, request
from sanic.response import json
from sanic_cors import CORS, cross_origin
import predictor

app = Sanic(__name__)
cors = CORS(app)
port = os.environ.get('PORT', 8000)
app.config['CORS_HEADERS'] = 'Content-Type'

test_team = [{'age': 19, 'gender': 'Male', 'married': False},
 {'age': 19, 'gender': 'Male', 'married': True},
 {'age': 57, 'gender': 'Female', 'married': True},
 {'age': 57, 'gender': 'Female', 'married': True}]


@app.route("/", methods=['POST', 'GET'])
@cross_origin(app)
async def test_fanction(request):
    answer = predictor.get_answers(test_team)
    print(list(answer))
    return json({'result': answer})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)

