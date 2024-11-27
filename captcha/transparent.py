from PIL import Image, ImageDraw 
import random, os




def random_image():
    image_path = [f"charectors/{img}" for img in os.listdir("charectors/")]
    random_img = image_path[random.randint(0, len(image_path) - 1)]
    return random_img

def convertImage():
    image_path = [f"charectors/{img}" for img in os.listdir("charectors/")]
    for image in image_path: 
        img = Image.open(image)
        img = img.convert("RGBA")
    
        datas = img.getdata()
    
        newData = []
    
        for item in datas:
            if item[0] != 0 and item[1] != 0 and item[2] != 0:
                newData.append((0, 0, 0, 0))
            else:
                newData.append(item)
    
        img.putdata(newData)
        img.save(image.split("/")[1], "PNG")
        print("Successful")
 
convertImage()