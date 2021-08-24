import config
from package.info import GosuInfoStd
from package.info import MapInfo


def map_get():
    g_inf = GosuInfoStd()
    map = g_inf.map_dir()
    return map


'''
title artist difficulty
stars
pp100--95 pp_strain
circle_count slider_count spinner_count
background
cs ar od hp
bpm length
bid sid
rank_status


leaderboard
'''


def map_info(map):
    map = MapInfo(map)
