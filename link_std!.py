from package.info import GosuInfoStd
from package.info import MapInfo
from package.image import bg_maker
from package.image import img_scale_resize
from package.image import info_print
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from datetime import datetime
from io import BytesIO
from json import loads
from time import localtime
from time import strftime
from time import strptime
import win32clipboard
from PIL import ImageFilter
from PIL import ImageFont
from requests import get
import config

'''------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------------------------------'''
# 别问我为什么 我也不知道 改成调用就没信息我也很难

import os
import psutil
import re
from ctypes import *
from Memory64 import *


def Get_Name_Pid(name):
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
            if name in process.name():
                return pid
        except Exception:
            pass


def Search_Memory_Code(name, code):
    Game_Pid = Get_Name_Pid(name)
    Drive = SetupProcess(Game_Pid)

    Dream_dll = CDLL(os.getcwd() + "/package/Dream.dll")
    ret_number = Dream_dll.Search_Code(code.encode("ISO-8859-1"))  # ISO-8859-1
    Result = string_at(ret_number).decode("ISO-8859-1")  # gbk

    Rule = re.compile(r"\d+")
    Res_data = re.findall(Rule, Result)
    for Final_data in Res_data:
        Ret_Value = Drive.ReadMemory64_Wchar(int(Final_data), 180, 0)
        # print(Ret_Value)
        if "20" in Ret_Value:
            first = re.search('\S+[0-9]', Ret_Value)
            end = re.search('\s\d{1,2}:\d{1,2}:\d\d', Ret_Value)
            return [first.group() + end.group()]
    # print('-------------------------------------------------------------')


def get_played_time():
    result = Search_Memory_Code("osu!.exe", "50 00 6C 00 61 00 79 00 65 00")
    return result


'''------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------------------------------'''
'''------------------------------------------------------------------------------------------------------------------'''


def main():
    g_inf = GosuInfoStd()
    if g_inf.state() == 7 or 2:  # 判断打完图或回放后或者fail的结算或者暂停界面
        if g_inf.mode() == 0:  # 判断std
            bg_dir = g_inf.bg_dir()
            if bg_dir[-3:] == 'png' or bg_dir[-3:] == 'jpg':  # 判断后缀做背景
                bg = bg_dir
                bg = bg_maker(bg)
            else:
                im = config.bg_if_non
                bg = Image.open(im).point(lambda p: p * 0.90)  # 背景暗化
                bg = img_scale_resize(bg, config.bg_resize_weight)  # 等比缩放

            score_model = Image.open(config.bg_model_dir)
            # 因为背景图比例不一，而且已经缩放到和模板一致宽度，所以才有了y_offset
            y_offset = int((bg.height - config.bg_resize_height) / 2)

            # 合并背景和模板
            bg.paste(score_model, (0, y_offset), score_model)

            im = output_info(bg, g_inf, y_offset)  # 大部分输出
            im = output_rank_icon(im, g_inf, y_offset)
            im = output_method_mod(im, g_inf.mod_str(), y_offset)
            im = output_method_avatar(im, g_inf, y_offset)
            im = output_line_chart_pp(im, g_inf, y_offset)
            im = output_line_chart_ur(im, g_inf, y_offset)
            im = output_note_count(im, g_inf, y_offset)
            im = output_rank_status(im, g_inf, y_offset)
            im = output_pp(im, g_inf, y_offset)
            im = output_game_time(im, y_offset)  # 一定要放在所有打印的最后边 我也不知道为什么！！！

            box = (0, y_offset, config.bg_resize_weight, y_offset + config.bg_resize_height)
            im = im.crop(box)
            try:
                im.show()
                exit(0)
            except Exception:
                print('显示图片失败, 生成结果将直接保存在运行目录下')
                im.save('结果.jpg')
                exit(0)
        else:
            print('你这不是std啊，是不是用错程序了啊喂！')
            exit(0)
    else:
        print('不在打图流程后的成绩界面 or Fail的暂停界面，打个图或者看个回放吧！')
        exit(0)


def output_rank_status(im, g_inf, y_offset):
    # unknown 0, unsubmitted 1, pending/wip/graveyard 2, unused 3, ranked 4, approved 5, qualified 6, loved 7
    status = g_inf.map_status()
    status_list = [config.map_status_unknown,
                   config.map_status_unsubmitted,
                   config.map_status_pending_wip_graveyard,
                   config.map_status_unused,
                   config.map_status_ranked,
                   config.map_status_approved,
                   config.map_status_qualified,
                   config.map_status_loved
                   ]
    status_img = status_list[status]
    status_img = Image.open(status_img)
    status_img.resize(config.map_status_size)
    im.paste(status_img, (config.map_status_position[0], config.map_status_position[1] + y_offset), status_img)
    return im


def output_rank_icon(im, g_inf, y_offset):
    rank = g_inf.rank_result()
    rank = str(rank)
    if g_inf.state() == 2:
        rank = Image.open(config.result_rank_icon_f)
    elif g_inf.state() == 7:
        if rank == 'SSH':
            rank = Image.open(config.result_rank_icon_ssh)
        elif rank == 'SS':
            rank = Image.open(config.result_rank_icon_ss)
        elif rank == 'SH':
            rank = Image.open(config.result_rank_icon_sh)
        elif rank == 'S':
            rank = Image.open(config.result_rank_icon_s)
        elif rank == 'A':
            rank = Image.open(config.result_rank_icon_a)
        elif rank == 'B':
            rank = Image.open(config.result_rank_icon_b)
        elif rank == 'C':
            rank = Image.open(config.result_rank_icon_c)
        elif rank == 'D':
            rank = Image.open(config.result_rank_icon_d)
        else:
            print('无法获取到正确的成绩，请重试')
            exit(0)

    rank = rank.resize(config.result_rank_size)
    rank = rank.convert('RGBA')
    im.paste(rank, (config.position_rank[0], config.position_rank[1] + y_offset), rank)
    return im


def output_info(im, g_inf, y_offset):
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
              'pp_ss',
              'pp_99',
              'pp_98',
              'pp_97',
              'pp_96',
              'pp_95',
              'pp_fc',
              'player_name']:
        i = eval('''[g_inf.{0}(), config.output_{0}[0], config.output_{0}[1], config.output_{0}[2],
             config.output_{0}[3], config.output_{0}[4], config.output_{0}[5]]'''.format(i))
        im = info_print(im, i[0], i[1], i[2], i[3], i[4] + y_offset, i[5], i[6])

    bpm = str(g_inf.bpm_max()) if g_inf.bpm_min() == g_inf.bpm_max() else str(g_inf.bpm_min()) + '-' + str(
        g_inf.bpm_max())
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
    time_length_now = eval(config.output_time_length_now_format)
    user_signature = config.user_signature
    ur = eval(config.output_ur_format)
    a = ['bpm', 'mapper', 'difficulty', 'key_count_k1', 'key_count_k2', 'key_count_m1', 'key_count_m2', 'score',
         'max_combo', 'accuracy', 'user_signature', 'ur',
         'time_length_now' if g_inf.state() == 2 else 'time_length_full']
    for i in a:
        i = eval('''[eval(i), config.output_{0}[0], config.output_{0}[1], config.output_{0}[2],
                     config.output_{0}[3], config.output_{0}[4], config.output_{0}[5]]'''.format(i))
        im = info_print(im, i[0], i[1], i[2], i[3], i[4] + y_offset, i[5], i[6])
    return im


# mod图标输出方式，默认为从设定位置开始依次向下100xp
def output_method_mod(im, mods_str, y_offset):  # 输入图片,mod的字符串,输出打印完的图片
    mods_str = str.lower(mods_str)  # 把所有字符中的大写字母转换成小写字母
    if mods_str == 'nm':  # 判断是否无mod
        a = ''
    else:
        a = []
        i = 0
        tmp = ""
        for v in mods_str:
            tmp += v
            i += 1
            if i % 2 == 0:
                a.append(tmp)
                tmp = ""
    x = config.position_mod[0]
    y = config.position_mod[1]
    for a in a:  # 循环打印
        img = eval('config.mod_icon_{}'.format(a))
        img = Image.open(img)
        img = img.resize(config.size_mod)
        im.paste(img, (x, y + y_offset), img)
        y = y + 100
    return im


# 头像打印方法，默认裁为圆形
def output_method_avatar(im, g_inf, y_offset):  # 传入im, y_offset，传出im
    if g_inf.player_name() == 'osu!':
        avatar = Image.open(config.osu_image)
    else:
        avatar = Image.open(config.user_avatar)
    avatar = avatar.resize(config.avatar_size)
    border = Image.open('resource/image/image_model/avatar-a.png')
    border = border.resize(config.avatar_size).convert('L')
    invert = ImageOps.invert(border)
    avatar.putalpha(invert)
    im.paste(avatar, (config.position_avatar[0], config.position_avatar[1] + y_offset), avatar)
    return im


def output_line_chart_pp(im, g_inf, y_offset):
    pp_strains_size = [config.pp_strains_location2[0] - config.pp_strains_location[0],
                       config.pp_strains_location2[1] - config.pp_strains_location[1]]
    pp_strains = g_inf.pp_strains()
    if pp_strains is None:
        pass
    else:
        y = pp_strains
        # 生成x列表
        n = 0
        for i in pp_strains:
            n += 1
        m = 0
        x = []
        for i in range(n):
            x.append(m)
            m += 1
        # y列表等比例缩放
        max_num_y = 0
        for num in y:
            if num > max_num_y:
                max_num_y = num
            else:
                pass
        scale_y = pp_strains_size[1] / max_num_y
        new_y = []
        for num in y:
            new_num = num * scale_y
            new_y.append(new_num)
        # y列表等比例缩放
        max_num_x = x[-1]
        scale_x = pp_strains_size[0] / max_num_x
        new_x = []
        for num in x:
            new_num = num * scale_x
            new_x.append(new_num)
        # 换算成对应坐标
        final_y = []
        for y in new_y:  # 里边有一步轴对称
            new_y_ = config.pp_strains_location2[1] - y + y_offset
            final_y.append(new_y_)
        final_x = []
        for x in new_x:
            new_x_ = config.pp_strains_location[0] + x
            final_x.append(new_x_)
        xy = []
        for i in range(n):
            xy.append((final_x[i], final_y[i]))
        # 画线
        draw = ImageDraw.Draw(im)
        for i in range(n - 1):
            x_y = [xy[i], xy[i + 1]]
            draw.line(x_y, fill=config.pp_strains_color, width=config.pp_strains_line_width)
    return im


def output_line_chart_ur(im, g_inf, y_offset):
    ur_strains_size = [config.ur_strains_location2[0] - config.ur_strains_location[0],
                       config.ur_strains_location2[1] - config.ur_strains_location[1]]
    ur_strains = g_inf.ur_strains()
    y = ur_strains
    # 生成x列表
    n = 0
    for i in ur_strains:
        n += 1
    m = 0
    x = []
    for i in range(n):
        x.append(m)
        m += 1
    # y列表等比例缩放
    min_num_y = 0
    for num in y:
        if num > min_num_y:
            min_num_y = num
        else:
            pass

    yyy = []
    for num in y:
        new_y = num + min_num_y
        yyy.append(new_y)

    y = yyy

    max_num_y = 0
    try:
        for num in y:
            if num > max_num_y:
                max_num_y = num
            else:
                pass
        scale_y = ur_strains_size[1] / max_num_y

        new_y = []
        for num in y:
            new_num = num * scale_y
            new_y.append(new_num)
    except:
        new_y = y
    # else:
    #     new_y = y
    # x列表等比例缩放
    max_num_x = x[-1]
    scale_x = ur_strains_size[0] / max_num_x

    new_x = []
    for num in x:
        new_num = num * scale_x
        new_x.append(new_num)

    # 换算成对应坐标
    final_y = []
    for y in new_y:  # 里边有一步轴对称
        new_y_ = config.ur_strains_location2[1] - y + y_offset
        final_y.append(new_y_)

    final_x = []
    for x in new_x:
        new_x_ = config.ur_strains_location[0] + x
        final_x.append(new_x_)

    xy = []
    for i in range(n):
        xy.append((final_x[i], final_y[i]))

    # 画线
    draw = ImageDraw.Draw(im)
    for i in range(n - 1):
        x_y = [xy[i], xy[i + 1]]
        draw.line(x_y, fill=config.ur_strains_color, width=config.ur_strains_line_width)
    return im


def output_game_time(im, y_offset):
    try:
        time_str = eval(str(get_played_time()))[0]
        time = time_str.split(' ')
        time[1] = time[1].split(':')[0] + ':' + time[1].split(':')[1]
    except:
        time_str = strftime("%Y/%m/%d %H:%M", localtime())
        time = time_str.split(' ')
        time[1] = time[1].split(':')[0] + ':' + time[1].split(':')[1]

    i = config.output_time_day
    im = info_print(im, time[0], i[0], i[1], i[2], i[3] + y_offset, i[4], i[5])
    i = config.output_time_min
    im = info_print(im, time[1], i[0], i[1], i[2], i[3] + y_offset, i[4], i[5])
    return im


def output_note_count(im, g_inf, y_offset):
    dir = g_inf.map_dir()
    a = MapInfo(dir)
    circle = a.note()
    slider = a.slider()

    i = config.output_note_circle
    im = info_print(im, circle, i[0], i[1], i[2], i[3] + y_offset, i[4], i[5])
    i = config.output_note_slider
    im = info_print(im, slider, i[0], i[1], i[2], i[3] + y_offset, i[4], i[5])
    return im


def output_pp(im, g_inf, y_offset):
    pp_current = g_inf.pp_current()

    font = config.output_pp_current[0]
    fontsize = config.output_pp_current[1]
    text = str(pp_current)
    num_width, num_height = ImageFont.truetype(font, fontsize).getsize(text)

    text = 'pp'
    font = config.output_str_pp[0]
    fontsize = config.output_str_pp[1]
    pp_width, pp_height = ImageFont.truetype(font, fontsize).getsize(text)

    total_width = num_width + pp_width
    total_height = num_height + pp_height

    x = config.output_pp_current_position[0]
    y = config.output_pp_current_position[1]
    align = config.output_pp_current_position[2]
    draw = ImageDraw.Draw(im)

    if align[0] == 'l':
        num_x = x
        pp_x = x + num_width
    elif align[0] == 'c':
        num_x = x - (total_width / 2)
        pp_x = num_x + num_width
    elif align[0] == 'r':
        num_x = x - total_width
        pp_x = x
    else:
        print('对齐参数设置有误，请确认，格式为 {左右对齐}{上下对齐} (可用参数c l r a b)，示例:rc(right,centre  右对齐，中间对齐)')
        exit(0)

    if align[1] == 'a':
        y = y
    elif align[1] == 'c':
        y = y - (total_height / 2)
    elif align[1] == 'b':
        y = y - total_height
    else:
        print('对齐参数设置有误，请确认，格式为 {左右对齐}{上下对齐} (可用参数c l r a b)，示例:rc(right,centre  右对齐，中间对齐)')
        exit(0)
    fill = config.output_pp_current[2]
    font = str(config.output_pp_current[0])
    size = int(config.output_pp_current[1])
    draw.text((num_x, y + y_offset), str(pp_current), fill=fill,
              font=ImageFont.truetype(font, size))
    fill = config.output_str_pp[2]
    font = str(config.output_str_pp[0])
    size = int(config.output_str_pp[1])
    draw.text((pp_x, y + y_offset + config.output_str_pp_y_offset), 'pp', fill,
              font=ImageFont.truetype(font, size))
    return im


if __name__ == '__main__':
    main()
    # print(output_game_time('im', 'y_offset'))
