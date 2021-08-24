from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

import sys
sys.path.append("..")

import config
from PIL import ImageFilter


def img_judge(im):
    if type(im) == 'PIL.PngImagePlugin.PngImageFile':
        im = im
    elif type(im) == 'str':
        im = Image.open(im)
    return im


def bg_maker(im):
    im = Image.open(im)
    im = im.convert('RGB')
    im = im.filter(ImageFilter.GaussianBlur(radius=config.gaussian_blur))  # 高斯模糊
    im = im.point(lambda p: p * config.bg_dim)  # 暗化
    im = img_scale_resize(im, config.bg_resize_weight)  # 等比缩放
    return im


def info_print(im, text, font, fontsize, x, y, color, align):
    # print(im)
    im = img_judge(im)
    # print(im)
    draw = ImageDraw.Draw(im)
    text = str(text)
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
    return im


def img_scale_resize(im, weigh):
    im = img_judge(im)
    scale = weigh / im.width
    im = im.resize((int(im.width * scale), int(im.height * scale)))
    return im
