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
output_title = ["fonts/comic sans ms.ttf", 27, 927, 85, (255, 255, 255), 'cc']
output_artist = ["fonts/comic sans ms.ttf", 21, 927, 120, (255, 255, 255), 'cc']
output_cs = ["fonts/comic sans ms.ttf", 24, 1249, 393, (255, 255, 255), 'cc']
output_ar = ["fonts/comic sans ms.ttf", 24, 1249, 452, (255, 255, 255), 'cc']
output_od = ["fonts/comic sans ms.ttf", 24, 1249, 513, (255, 255, 255), 'cc']
output_hp = ["fonts/comic sans ms.ttf", 24, 1249, 570, (255, 255, 255), 'cc']
output_bid = ["fonts/comic sans ms.ttf", 20, 1035, 513, (255, 255, 255), 'cc']
output_sid = ["fonts/comic sans ms.ttf", 20, 1035, 571, (255, 255, 255), 'cc']
output_c300 = ["fonts/comic sans ms.ttf", 20, 615, 515, (255, 255, 255), 'cc']
output_c100 = ["fonts/comic sans ms.ttf", 20, 780, 515, (255, 255, 255), 'cc']
output_c50 = ["fonts/comic sans ms.ttf", 20, 615, 600, (255, 255, 255), 'cc']
output_c0 = ["fonts/comic sans ms.ttf", 20, 780, 600, (255, 255, 255), 'cc']
output_slider_breaks = ["fonts/comic sans ms.ttf", 22, 615, 680, (255, 255, 255), 'cc']
output_stars = ["fonts/comic sans ms.ttf", 23, 561, 210, (255, 255, 255), 'lc']
output_pp_current = ["fonts/comic sans ms.ttf", 33, 1198, 677, (255, 255, 255), 'cc']
output_pp_ss = ["fonts/comic sans ms.ttf", 22, 950, 657, (255, 255, 255), 'lc']
output_pp_97 = ["fonts/comic sans ms.ttf", 22, 950, 657, (255, 255, 255), 'lc']
output_pp_fc = ["fonts/comic sans ms.ttf", 22, 950, 657, (255, 255, 255), 'lc']
output_bpm = ["fonts/comic sans ms.ttf", 24, 1032, 453, (255, 255, 255), 'cc']

output_mapper = ["fonts/simhei.ttf", 25, 1310, 333, (255, 255, 255), 'rc']
output_mapper_format = "'Mapper:' + str({0}).format(g_inf.mapper())"

output_difficulty = ["fonts/simhei.ttf", 25, 1310, 296, (255, 255, 255), 'rc']
output_difficulty_format = "'Diff:' + str({0}).format(g_inf.difficulty())"

output_player_name = ["fonts/comic sans ms.ttf", 31, 337, 606, (255, 255, 255), 'cc']
output_key_count_k1 = ["fonts/simhei.ttf", 20, 518, 399, (255, 255, 255), 'cc']
output_key_count_k2 = ["fonts/simhei.ttf", 20, 518, 449, (255, 255, 255), 'cc']
output_key_count_m1 = ["fonts/simhei.ttf", 20, 518, 499, (255, 255, 255), 'cc']
output_key_count_m2 = ["fonts/simhei.ttf", 20, 518, 549, (255, 255, 255), 'cc']

output_score = ["fonts/lucidahandwriting.ttf", 49, 1160, 235, (255, 255, 255), 'cc']

output_max_combo = ["fonts/comic sans ms.ttf", 22, 782, 427, (255, 255, 255), 'cc']

output_accuracy = ["fonts/comic sans ms.ttf", 22, 619, 427, (255, 255, 255), 'cc']

output_time_length_full = ["fonts/comic sans ms.ttf", 24, 1033, 393, (255, 255, 255), 'cc']
