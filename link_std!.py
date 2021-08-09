from package.info import GosuInfoStd
from package.image import bg_maker
from package.image import img_scale_resize
from package.image import info_print
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
                    bg = img_scale_resize(config.bg_resize_weight)
            score_model = Image.open(config.bg_model_dir)
            y_offset = int((bg.height - config.bg_resize_height) / 2)
            bg.paste(score_model, (0, y_offset), score_model)
            im = inf_print(bg, g_inf)
            TODO = '还差 个签 rank图标 mod图标 头像  PP格式化 铺面status图标'
            im.show()
        else:
            print('你这不是std啊，是不是用错程序了啊喂！')
            exit(0)
    else:
        print('不在打图流程后的成绩界面，打个图或者看个回放吧！')
        exit(0)


def inf_print(im, g_inf):
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
              'player_name'
              ]:
        i = eval('''[g_inf.{0}(), config.output_{0}[0], config.output_{0}[1], config.output_{0}[2],
             config.output_{0}[3], config.output_{0}[4], config.output_{0}[5]]'''.format(i))
        im = info_print(im, i[0], i[1], i[2], i[3], i[4], i[5], i[6])

    bpm = str(g_inf.bpm_max()) if g_inf.bpm_min() == g_inf.bpm_max() else str(g_inf.bpm_min()) + '-' + str(g_inf.bpm_max())
    mapper = eval(config.output_mapper_format)
    difficulty = eval(config.output_difficulty_format)
    key_count_k1 = str(g_inf.key_count_k1() if g_inf.key_count_k1() != 0 else 'K1')
    key_count_k2 = str(g_inf.key_count_k2() if g_inf.key_count_k2() != 0 else 'K2')
    key_count_m1 = str(g_inf.key_count_m1() if g_inf.key_count_m1() != 0 else 'M1')
    key_count_m2 = str(g_inf.key_count_m2() if g_inf.key_count_m2() != 0 else 'M2')
    score = eval(config.output_score_format)
    max_combo = eval(config.output_max_combo_format)
    accuracy = eval(config.output_accuracy_format)
    time_length_full = eval(config.output_time_length_full_format)
    for i in ['bpm',
              'mapper',
              'difficulty',
              'key_count_k1',
              'key_count_k2',
              'key_count_m1',
              'key_count_m2',
              'score',
              'max_combo',
              'accuracy',
              'time_length_full']:
        i = eval('''[eval(i), config.output_{0}[0], config.output_{0}[1], config.output_{0}[2],
                     config.output_{0}[3], config.output_{0}[4], config.output_{0}[5]]'''.format(i))
        im = info_print(im, i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    return im


if __name__ == '__main__':
    main()
    # inf_print(im=None, g_inf=GosuInfoStd())
