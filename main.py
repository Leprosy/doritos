# coding=utf-8>

from PIL import Image, ImageDraw, ImageFont, ImageOps
import shutil
import os
import datetime
from random import choice


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
        img = Image.open("img/doritos-template.png")
        quote = self.generate_name()
        fnt = ImageFont.truetype('font.ttf', 16)
        fnt_icon = ImageFont.truetype('font.ttf', 50)

        txt = Image.new('RGBA', (200,100))
        d = ImageDraw.Draw(txt)
        d.text( (1, 1), quote,  font=fnt, fill=(0,0,0))
        d.text( (0, 0), quote,  font=fnt, fill=(255,255,40))
        #d.text( (36, 21), self.generate_icon(), font=fnt_icon, fill=(0, 0,0))
        #d.text( (35, 20), self.generate_icon(), font=fnt_icon, fill=(50,50,255))
        w = txt.rotate(5,  expand=1)

        img.paste(w, (162, 232), w)
        #img.paste( ImageOps.colorize(w, (0,0,0), (255,255,84)), (170, 230),  w)

        img.save("out_%s.png" % "{:%Y_%m_%d_%H_%M_%S}".format(datetime.datetime.now()))

if __name__ == '__main__':
    print("Creating dorito...")
    W = Writer()
    W.save_picture()
    print("Done")