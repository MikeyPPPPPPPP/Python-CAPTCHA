"""

Draw PIXLE art: https://www.pixilart.com/draw?ref=home-page#



start with an square image 

make 3 sqwigly lines across 3 random sections horazontally


add 3 letters and or charectors to each line in a randome place, but at least have a little space between each so they dont overlapfor a total of 9

Charector:
    make transparent 
    random rotation
    slight random resize


make a key in the background corasponding to they origanal charector and the order there in



1. make two captcha requirments

2. instant IP band for 3 hours

3. give a unique cookie if you succed






"""

from io import BytesIO
import random, os, base64, re

from PIL import Image


class customCaptcha:
    def __init__(self, charector_image_path: str):
        
        self.charector_image_path = charector_image_path
        self.width = 320
        self.height = 320
        self.new_gray = self.newGray()
        self.catchaImage = Image.new("RGBA", (self.width, self.height), self.new_gray) 
        self.catchaImage.convert("RGBA")

    def newGray(self) -> tuple[int, int, int]:
        return (random.randint(192,200),random.randint(192,222),random.randint(196,205))
    

    def point_avrages(self, p1: tuple[int, int], p2: tuple[int, int]):
        avrgX = (p1[0] + p2[0]) / 2#get the avreg of the X's
        avrgY = (p1[1] + p2[1]) / 2#get the arveg of the Y's
        return (int(avrgX), int(avrgY))
    

    def random_image(self)  -> tuple[str, int]:
        image_path = [f"{os.path.join(self.charector_image_path,img)}" for img in os.listdir(self.charector_image_path) if img.endswith("png")]
        file_name = image_path[random.randint(0, len(image_path) - 1)]
        random_img = Image.open(file_name)
        random_img.convert("RGBA")

        #add slight rotation
        random_img = random_img.rotate(random.randint(-30,30))

        #resize the images a little
        (width, height) = (random_img.width + random.randint(-8,16), random_img.height + random.randint(-8,16))
        random_img = random_img.resize((width, height))


        #Create new images in memory, Access the pixel data of the image
        pixels = list(random_img.getdata())
        modified_pixels = [self.new_gray if pixel == (0, 0, 0, 0) else pixel for pixel in pixels]

        modified_image = Image.new("RGBA", random_img.size)
        modified_image.putdata(modified_pixels)

        image_key = re.findall("(?<=testing\/captcha\/)(.*)(?=.png)", file_name)[0]
        if image_key == "UP":
            image_key = "P"

        return image_key, modified_image
    
    def drawInvisibleLine(self, between_height: tuple[int, int]) -> list[str]:
        line_width_start = 0
        line_width_segment = round(self.width / 15)
        files_keys = []
        skip_first_line_point = 0
        ran_starting_line_heigh = random.randint(between_height[0], between_height[1])
        for num in range(0, 15):
            ran_ending_line_height = random.randint(between_height[0], between_height[1])

            if num % 3 == 0:
                if skip_first_line_point != 0:

                    img_key, obfuscated_image = self.random_image()
                    files_keys.append(img_key)

                    #obfuscated_image = obfuscated_image.convert("RGBA")

                    self.catchaImage.paste(obfuscated_image, box=self.point_avrages((line_width_start, ran_starting_line_heigh), (line_width_start+line_width_segment, ran_ending_line_height)), mask=obfuscated_image)

                    #image_object.save(image_object, 'PNG')
                else:
                    skip_first_line_point += 1

            ran_starting_line_heigh = ran_ending_line_height
            line_width_start += line_width_segment


        return files_keys
    

    def newCaptch(self) -> str| bytes:
        

        level1 = self.drawInvisibleLine((20,100))
        level2 = self.drawInvisibleLine((140,220))
        level3 = self.drawInvisibleLine((240,290))

        # Save the image to a BytesIO object
        img_io = BytesIO()
        self.catchaImage.save(img_io, 'PNG')
        img_io.seek(0)

        return ''.join(level1 + level2 + level3), base64.b64encode(img_io.getvalue()).decode('utf-8')


botDetectionCaptcha = customCaptcha(".")
answare, new_image = botDetectionCaptcha.newCaptch()
