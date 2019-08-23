import os

from sanic import Sanic, request
from sanic.response import json,text,redirect
from sanic_cors import CORS, cross_origin

app = Sanic(__name__)
cors = CORS(app)
port = os.environ.get('PORT', 8000)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin(app)
async def test_fanction(request):
    return json({'result': 'big things definitely on the way'})


@app.route("/<name:string>" , methods=['GET'])
async def funcname(request,name):
    return json({'name' : name.format()})


#this redirects all other traffice (i.e invalid trafic ) 
@app.route('/<path:path>')
async def catch_all(request , path=''):
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=False)

