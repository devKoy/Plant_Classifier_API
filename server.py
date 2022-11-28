from distutils.log import debug
from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
from application import prediction as p, read_files as r
import os
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

origins = [
   "https://testapi.consulting.repl.co",
   "https://www.greenlyai.space",
   "https://greenlyai.space"
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins,  allow_headers=["*"])
]

app = FastAPI(middleware=middleware)


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

if __name__ == "__main__":
	uvicorn.run(app, host='0.0.0.0', port=os.environ.get('PORT', '5000'))
