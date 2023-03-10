import os
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
from PIL import Image
import io


from repl import fetch_replicate

os.environ['REPLICATE_API_TOKEN'] = "1ceca98a76234217cf69af35b55f81651e441ed5"

app = FastAPI()


@app.get("/")
def read_root():
    return {"Root Directory"}
@app.post("/files/")
async def create_file(file: bytes = File()):
    output = fetch_replicate(file ,)
    json_response = {
        'image_url' : output[1]
    }
    return {"file_size": len(file)}
@app.post("/uploadfile/")
async def create_upload_file(file: bytes = File(...), room: str = Form(...), theme: str = Form(...)):

    # file_like_object = io.BytesIO(file)

    # read the image data as binary using Pillow
    # image = Image.open(file_like_object)
    image = Image.open(io.BytesIO(file))
    image.save("image/my_image.jpg")
    output = fetch_replicate('image/my_image.jpg' ,room, theme)
    json_response = {
        'image_url' : output[1],
        'room': room,
        'theme': theme
    }
    return json_response

if __name__ == '__main__':
    uvicorn.run(app, host= '0.0.0.0', port= 8000)
