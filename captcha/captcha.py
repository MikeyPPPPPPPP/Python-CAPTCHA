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



from PIL import Image, ImageDraw 
import random, os




def random_image(background_color)  -> tuple[str, int]:
    #image_path = [f"charectors/{img}" for img in os.listdir("charectors/")]
    image_path = [f"{img}" for img in os.listdir() if img.endswith("png")]
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
    modified_pixels = [background_color if pixel == (0, 0, 0, 0) else pixel for pixel in pixels]

    modified_image = Image.new("RGBA", random_img.size)
    modified_image.putdata(modified_pixels)




    return file_name, modified_image#random_img




def point_avrages(p1: tuple[int, int], p2: tuple[int, int]):
    #get the avreg of the X's
    avrgX = (p1[0] + p2[0]) / 2

    #get the arveg of the Y's
    avrgY = (p1[1] + p2[1]) / 2
    

    return (int(avrgX), int(avrgY))
 



#point_avrages((-2, 0), (4, 2))




def draw_line(image_object ,between_height: tuple[int, int], background_color) -> list[str]:
    line_width_start = 0

    line_width_end = 320#220

    line_w_seg = round(320 / 15)#round(220 / 15)

    three_random_points = []
    files_keys = []
    temp = 0
    ran_starting_line_heigh = random.randint(between_height[0], between_height[1])
    for num in range(0, 15):

        ran_ending_line_height = random.randint(between_height[0], between_height[1])
        ran_line = [(line_width_start, ran_starting_line_heigh), (line_width_start+line_w_seg, ran_ending_line_height)]#[(w, h), (w, h)]

        #if odd number
        if num % 3 == 0:
            if temp != 0:

                img_key, obfuscated_image = random_image(background_color)
                files_keys.append(img_key.strip(".png"))
                three_random_points.append(point_avrages((line_width_start, ran_starting_line_heigh), (line_width_start+line_w_seg, ran_ending_line_height)))
                #image_object.text(point_avrages((line_width_start, ran_starting_line_heigh), (line_width_start+line_w_seg, ran_ending_line_height)), "A", font_size=29)
                #image_object.paste(random_image(), point_avrages((line_width_start, ran_starting_line_heigh), (line_width_start+line_w_seg, ran_ending_line_height)))
                image_object.paste(obfuscated_image, box=point_avrages((line_width_start, ran_starting_line_heigh), (line_width_start+line_w_seg, ran_ending_line_height)))
            else:
                temp += 1


        ran_starting_line_heigh = ran_ending_line_height

        #img1 can draw lines
        #image_object.line(ran_line)

        line_width_start += line_w_seg

    return files_keys

def random_gray():
    return (random.randint(192,200),random.randint(192,222),random.randint(196,205))

w, h = 320, 320#220

new_grey = random_gray()
img = Image.new("RGBA", (w, h), new_grey) 
img.convert("RGBA")
img1 = ImageDraw.Draw(img)   


level1 = draw_line(img, (20,100), new_grey)

level2 = draw_line(img, (140,220), new_grey)

level3 = draw_line(img, (240,290), new_grey)
img.show() 

print(level1 + level2 + level3)


