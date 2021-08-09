"""
小工具配置文件，注意引号，逗号，中英文标点，路径可用绝对路径可用相对路径
标准python变量写法，自由发挥哦
布尔值只可以用True和False 注意大小写
字符串记得引号
不建议瞎改，改自己懂的就好
"""


'''
自主定义变量区
    PS:只是图个方便不再重复，没学过编程语言不建议使用，老老实实一个一个改
'''


'''
用户变量配置
'''
user_name = 'Freezetime'
user_id = '11350021'
'''


图片相关配置
'''
# 获取不到bg使用的背景
bg_if_non = "resource/image/bgifnon.png"
# bg背景暗化程度
bg_dim = 0.9
# bg高斯模糊像素
gaussian_blur = 2
# bg重置大小后的宽度，必须和你的模板宽度一致，最终为成绩图宽度
bg_resize_weight = 1366
# 最终的成绩图高度，也就是你的模板高度
bg_resize_height = 768
# 成绩图模板路径
bg_model_dir = "resource/image/image_model/score.png"


'''
信息输出打印配置:格式xxx = [字体路径, 大小, x, y, (R, G, B), 对齐方式]
    PS:对齐方式写法：
        示例:rl  cl
        格式:{左右对齐}{上下对齐}
        可用参数:l(left)  c(center)  r(right)  a(above)  b(below)

没学过python的format不建议自主修改以下变量
xxx_format变量:输出格式化，双引号内写入python表达式。
    PS:g_inf()类的函数可以在package/info.py文件内查看
'''
output_title = ["resource/fonts/comic sans ms.ttf", 27, 927, 125, (255, 255, 255), 'cc']
output_artist = ["resource/fonts/comic sans ms.ttf", 21, 927, 160, (255, 255, 255), 'cc']
output_cs = ["resource/fonts/comic sans ms.ttf", 24, 1249, 435, (255, 255, 255), 'cc']
output_ar = ["resource/fonts/comic sans ms.ttf", 24, 1249, 495, (255, 255, 255), 'cc']
output_od = ["resource/fonts/comic sans ms.ttf", 24, 1249, 555, (255, 255, 255), 'cc']
output_hp = ["resource/fonts/comic sans ms.ttf", 24, 1249, 613, (255, 255, 255), 'cc']
output_bid = ["resource/fonts/comic sans ms.ttf", 20, 1035, 556, (255, 255, 255), 'cc']
output_sid = ["resource/fonts/comic sans ms.ttf", 20, 1035, 614, (255, 255, 255), 'cc']
output_c300 = ["resource/fonts/comic sans ms.ttf", 20, 615, 558, (255, 255, 255), 'cc']
output_c100 = ["resource/fonts/comic sans ms.ttf", 20, 780, 558, (255, 255, 255), 'cc']
output_c50 = ["resource/fonts/comic sans ms.ttf", 20, 615, 643, (255, 255, 255), 'cc']
output_c0 = ["resource/fonts/comic sans ms.ttf", 20, 780, 643, (255, 255, 255), 'cc']
output_slider_breaks = ["resource/fonts/comic sans ms.ttf", 22, 615, 723, (255, 255, 255), 'cc']
output_stars = ["resource/fonts/comic sans ms.ttf", 23, 541, 251, (255, 255, 255), 'lc']
output_pp_current = ["resource/fonts/comic sans ms.ttf", 33, 1198, 718, (255, 255, 255), 'cc']
output_pp_ss = ["resource/fonts/comic sans ms.ttf", 22, 800, 692, (255, 255, 255), 'lc']
output_pp_97 = ["resource/fonts/comic sans ms.ttf", 22, 900, 692, (255, 255, 255), 'lc']
output_pp_fc = ["resource/fonts/comic sans ms.ttf", 22, 1000, 692, (255, 255, 255), 'lc']
output_bpm = ["resource/fonts/comic sans ms.ttf", 24, 1032, 496, (255, 255, 255), 'cc']

output_mapper = ["resource/fonts/simhei.ttf", 25, 1310, 392, (255, 255, 255), 'rc']
output_mapper_format = "'Mapper:' + str({0}).format(g_inf.mapper())"

output_difficulty = ["resource/fonts/simhei.ttf", 25, 1310, 355, (255, 255, 255), 'rc']
output_difficulty_format = "'Diff:' + str({0}).format(g_inf.difficulty())"

output_player_name = ["resource/fonts/comic sans ms.ttf", 31, 337, 646, (255, 255, 255), 'cc']
output_key_count_k1 = ["resource/fonts/simhei.ttf", 20, 519, 441, (255, 255, 255), 'cc']
output_key_count_k2 = ["resource/fonts/simhei.ttf", 20, 519, 491, (255, 255, 255), 'cc']
output_key_count_m1 = ["resource/fonts/simhei.ttf", 20, 519, 540, (255, 255, 255), 'cc']
output_key_count_m2 = ["resource/fonts/simhei.ttf", 20, 519, 590, (255, 255, 255), 'cc']

output_score = ["resource/fonts/lucidahandwriting.ttf", 49, 1160, 275, (255, 255, 255), 'cc']
output_score_format = "'{:,}'.format(g_inf.score())"

output_max_combo = ["resource/fonts/comic sans ms.ttf", 22, 782, 470, (255, 255, 255), 'cc']
output_max_combo_format = "'{:,}'.format(g_inf.max_combo())"

output_accuracy = ["resource/fonts/comic sans ms.ttf", 22, 619, 470, (255, 255, 255), 'cc']
output_accuracy_format = "str({0}).format(g_inf.accuracy()) + '%'"

output_time_length_full = ["resource/fonts/comic sans ms.ttf", 24, 1035, 434, (255, 255, 255), 'cc']
output_time_length_full_format = "str(int((float(str({0}).format(g_inf.time_length_full()))/1000)/60))+" \
                                 "':' + " \
                                 "str(round((float(str({0}).format(g_inf.time_length_full()))/1000)%60, 1))"
# 什么狗屁玩意又臭又长，真亏我写得出来，你们自己看着改改，反正最后要eval这个语句，要一句成表达式，或者你字符串拼接我也不管
