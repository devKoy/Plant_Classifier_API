
from distutils.log import debug
from fastapi import FastAPI, File, UploadFile
from nbformat import read
import uvicorn
from application import prediction as p, read_files as r


app = FastAPI()
@app.get('/index')
async def hello():
	return "HELLO"
@app.post('/predict')
async def predict_api(file: UploadFile = File(...)):
	extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
	if not extension:
		return "Image must be a [jpg, jpeg, png] format"
	image = r.read_files(await file.read())
	pred = p.predict(image)
	
	return pred
if __name__ == "__main__":
	uvicorn.run(app, port = 8080, debug = True)