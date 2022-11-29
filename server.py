from distutils.log import debug
from fastapi import FastAPI, File, UploadFile, Form, Body, Request, Response
import uvicorn
from application import prediction as p, read_files as r
import os
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute


@app.get('/main')
async def hello():
	return "HELLO"
    
@app.post('/predict')
async def predict_api(file : UploadFile = None):
	
	extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
	if not extension:
		return "Image must be a [jpg, jpeg, png] format"
	image = r.read_files(await file.read())
	pred = p.predict(image)
	return pred
origins = [
   "https://testapi.consulting.repl.co",
   "https://www.greenlyai.space",
   "https://greenlyai.space"
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins,  allow_headers=["*"])
]

app = FastAPI(middleware=middleware)

ALLOWED_ORIGINS = '*' 

# handle CORS preflight requests
@app.options('/*')
async def preflight_handler(request: Request, rest_of_path: str) -> Response:
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_ORIGINS
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

# set CORS headers
@app.middleware("http")
async def add_CORS_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_ORIGINS
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


if __name__ == "__main__":
	uvicorn.run(app, host='0.0.0.0', port=os.environ.get('PORT', '5000'))
