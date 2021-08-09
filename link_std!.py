from package.info import GosuInfoStd
from package.image import bg_maker
from package.image import Img
import time
from io import BytesIO
from json import loads
from time import localtime
from time import strftime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont
from PIL import ImageOps
from requests import get
import config


def main():
    g_inf = GosuInfoStd()

    if g_inf.state() == 7:
        if g_inf.mode() == 0:
            bg_dir = g_inf.bg_dir()
            if bg_dir[-3:] == 'png' or bg_dir[-3:] == 'jpg':
                bg = bg_dir
                bg = bg_maker(bg)
            else:
                with open(config.bg_if_non) as im:
                    bg = Image.open(im).point(lambda p: p * 0.90)
                    with Img(bg) as i:
                        bg = i.img_scale_resize(config.bg_resize_weight)
            score_model = Image.open(config.bg_model_dir)
            y_offset = int((bg.height - config.bg_resize_height) / 2)
            im = bg.paste(score_model, (0, y_offset), score_model)
            im = info_print(im, g_inf)
        else:
            print('你这不是std啊，是不是用错程序了啊喂！')
            exit(0)
    else:
        print('不在打图流程后的成绩界面，打个图或者看个回放吧！')
        exit(0)


def info_print(im, g_inf):
    for i in ['title',
              'artist',
              'cs',
              'od',
              'ar',
              'hp',
              'bid',
              'sid',
              'c300',
              'c100',
              'c50',
              'c0',
              'slider_breaks',
              'stars',
              'pp_current',
              'pp_ss',
              'pp_97',
              'pp_fc',
              ]:
        i = eval('''[g_inf.{0}(), config.output_{0}[0], config.output_{0}[1], config.output_{0}[2],
             config.output_{0}[3], config.output_{0}[4], config.output_{0}[5]]'''.format(i))
        print(i)

    bpm = str(g_inf.bpm_max()) if g_inf.bpm_min() == g_inf.bpm_max() else str(g_inf.bpm_min()) + '-' + str(g_inf.bpm_max())
    mapper = eval(config.output_mapper_format)
    difficulty = eval()
    print(mapper)


if __name__ == '__main__':
    # main()
    info_print(im=None, g_inf=GosuInfoStd())
