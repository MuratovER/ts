from PIL import Image, ImageDraw,ImageFont
import os

def average_image_color(filename): # Средний цвет всей картинки
    i = Image.open(filename)
    h = i.histogram()

    # split into red, green, blue
    r = h[0:256]
    g = h[256:256*2]
    b = h[256*2: 256*3]

    # perform the weighted average of each channel:
    # the *index* is the channel value, and the *value* is its weight
    return (
        int(sum( i*w for i, w in enumerate(r) ) / sum(r)),
        int(sum( i*w for i, w in enumerate(g) ) / sum(g)),
        int(sum( i*w for i, w in enumerate(b) ) / sum(b))
    )

def get_image(user_text, id, bg_id=1):
    # user_text = "Я выбираю классные фоны ыыыыыыыыы\nыыыыы\nыыы\nыыыыыыыыы"

    file = "mainsite/useful_lib/images_for_affirmation/bg_{}.png".format(bg_id)
    colors = average_image_color(file)
    color_font = (255-colors[0], 255-colors[1],255-colors[2])
    im = Image.open(file)
    d = ImageDraw.Draw(im)
    x, y =im.size
    fnt = ImageFont.truetype("mainsite/useful_lib/1.ttf", 42, layout_engine=ImageFont.LAYOUT_RAQM)
    # print(fnt.getbbox())
    print(fnt.getsize_multiline(user_text))
    d.multiline_text((x/2 - fnt.getsize_multiline(user_text)[0]/2, y/2 - fnt.getsize_multiline(user_text)[1]/2 ), user_text, font=fnt, fill=(255,255,255), stroke_width=2, stroke_fill=colors, align='center')

    im.save("mainsite/static/mainsite/images/affirmations/" + str(id)+".png", "PNG")
    return str(id)+".png"