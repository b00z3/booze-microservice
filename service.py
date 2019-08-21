import os

from sanic import Sanic, request
from sanic.response import json
from sanic_cors import CORS, cross_origin

app = Sanic(__name__)
cors = CORS(app)
port = os.environ.get('PORT', 8000)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin(app)
async def test_fanction(request):
    return json({'result': 'big things on the way'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=False)

