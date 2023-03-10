import replicate
import os
os.environ['REPLICATE_API_TOKEN'] = "1ceca98a76234217cf69af35b55f81651e441ed5"

def fetch_replicate(imageUrl, room, theme):

    model = replicate.models.get("jagilley/controlnet-hough")
    version = model.versions.get("854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b")

    # https://replicate.com/jagilley/controlnet-hough/versions/854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b#input
    inputs = {
            "image": open(imageUrl, 'rb'),
            "prompt": f"a {'room for gaming' if room == 'Gaming Room' else theme.lower()} {room.lower()}",
            "a_prompt": "best quality, extremely detailed, photo from Pinterest, interior, cinematic photo, ultra-detailed, ultra-realistic, award-winning",
            "n_prompt": "longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality"
        }


    # https://replicate.com/jagilley/controlnet-hough/versions/854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b#output-schema
    output = version.predict(**inputs)
    return output

if __name__ == '__main__':
    output = fetch_replicate('image\my_image.jpg', 'Dining Room', 'Modern')
    json_response = {
        'image_url' : output[1]
    }
    print(json_response)