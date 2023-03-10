import os
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
from PIL import Image
import io
from repl import fetch_replicate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Root Directory, redirect to docs"}

@app.post("/uploadfile/")
async def create_upload_file(file: bytes = File(...), room: str = Form(...), theme: str = Form(...)):

    image = Image.open(io.BytesIO(file))
    image.save("image/my_image.jpg")
    output = fetch_replicate('image/my_image.jpg' ,room, theme)
    json_response = {
        'image_url' : output[1]
    }
    return json_response

if __name__ == '__main__':
    uvicorn.run(app, host= '0.0.0.0', port= 8000)
