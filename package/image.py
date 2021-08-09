from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import sys
sys.path.append("..")

import config
from PIL import ImageFilter


def bg_maker(img_dir):
    with open(img_dir) as im:
        im = Image.open(im)
        im = im.filter(ImageFilter.GaussianBlur(radius=config.gaussian_blur))  # 高斯模糊
        im = im.point(lambda p: p * config.bg_dim)  # 暗化
        with Img(im) as i:
            im = i.img_scale_resize(config.bg_resize_weight)  # 等比缩放
    return im


class Img:
    def __init__(self, im):
        if type(im) == 'PIL.PngImagePlugin.PngImageFile':
            self.im = im
        elif type(im) == 'str':
            self.im = Image.open(im)

    def info_print(self, text, font, fontsize, x, y, color, align):
        with ImageDraw.Draw(self.im) as draw:
            width, height = ImageFont.truetype(font, fontsize).getsize(text)
            if align[0] == 'l':
                x = x
            elif align[0] == 'c':
                x = x - (width / 2)
            elif align[0] == 'r':
                x = x - width
            else:
                print('对齐参数设置有误，请确认，格式为 {左右对齐}{上下对齐} (可用参数c l r a b)，示例:rc(right,centre  右对齐，中间对齐)')
                exit(0)
            if align[1] == 'a':
                y = y
            elif align[1] == 'c':
                y = y - (height / 2)
            elif align[1] == 'b':
                y = y - height
            else:
                print('对齐参数设置有误，请确认，格式为 {左右对齐}{上下对齐} (可用参数c l r a b)，示例:rc(right,centre  右对齐，中间对齐)')
                exit(0)
            draw.text((x, y), text, fill=color, font=ImageFont.truetype(font, fontsize))
        return self.im

    def img_scale_resize(self, weigh):
        scale = weigh / self.im.width
        self.im = self.im.resize((int(self.im.width * scale), int(self.im.height * scale)))
        return self.im
