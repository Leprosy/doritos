# coding=utf-8>

from PIL import Image, ImageDraw, ImageFont, ImageOps
import shutil
import os
import datetime
from random import choice, random


class Writer():
    def __init__(self):
        pass

    def generate_name(self):
        adj = ["Lesbian", "Burning", "Smelly", "Dry", "Furry", "Hairy", "Wet", "Rotten", "Capitalist", "Hedonist",
               "Stupid", "Gruesome", "Tasty", "Gay"]
        sub = ["Spider", "Grass", "Dirt", "Smoke", "Wood", "Flower", "Cat", "Crap", "Dog", "Mustache", "Hair", 
               "Feet", "Snot", "Sweat"]
        return "%s %s" % (choice(adj), choice(sub))

    def save_picture(self):
        #Our canvas
        canvas = Image.new('RGBA', (334, 483))

        #Dorito template
        img = Image.open("img/doritos-template.png")
        img_logo = Image.open("img/doritos-logo.png")
        img_tortilla = Image.open("img/doritos-tortilla.png")
        img.convert("RGBA")
        ovr = Image.new("RGBA", (334, 483))
        draw = ImageDraw.Draw(ovr)
        draw.rectangle(((0, 0), (334, 483)), fill=(int(random() * 255), int(random() * 255), int(random() * 255), 100))
        img.alpha_composite(ovr)

        #Text
        quote = self.generate_name()
        fnt = ImageFont.truetype('font.ttf', 16)
        fnt_icon = ImageFont.truetype('font.ttf', 50)
        txt = Image.new('RGBA', (200,100))
        draw = ImageDraw.Draw(txt)
        draw.text( (1, 1), quote,  font=fnt, fill=(0,0,0))
        draw.text( (0, 0), quote,  font=fnt, fill=(255,255,40))
        #draw.text( (36, 21), self.generate_icon(), font=fnt_icon, fill=(0, 0,0))
        #draw.text( (35, 20), self.generate_icon(), font=fnt_icon, fill=(50,50,255))
        w = txt.rotate(5,  expand=1)

        #canvas.paste(ImageOps.colorize(img, (0,0,0), (255,255,84)), (0, 0))
        canvas.paste(img, (0, 0))
        canvas.paste(img_logo, (0, 0), img_logo)
        canvas.paste(img_tortilla, (0, 0), img_tortilla)
        canvas.paste(w, (162, 232), w)
        canvas.save("out_%s.png" % "{:%Y_%m_%d_%H_%M_%S}".format(datetime.datetime.now()))

if __name__ == '__main__':
    print("Creating dorito...")
    W = Writer()
    W.save_picture()
    print("Done")