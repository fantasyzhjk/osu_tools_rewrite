from requests import get
from json import loads
from json import load
import oppadc
import sys
sys.path.append("..")
import config
import requests
import httpx


def get_self_pp_plus():
    proxies = {
        "http": config.proxy_http,
        "https": config.proxy_https
    }
    url = 'https://syrin.me/pp+/api/user/' + config.user_id + '/'
    index = get(url=url, proxies=proxies)
    pp_plus = loads(index.text)
    return pp_plus['user_data']


def get_best():
    headers = {
        'cookie': config.cookie
        }
    proxies = {
        "http": config.proxy_http,
        "https": config.proxy_https
    }
    session = requests.Session()
    url1 = 'https://osu.ppy.sh/users/' + str(config.user_id) + '/scores/best?mode=osu&offset=0&limit=51'
    html1 = session.get(url1, headers=headers, proxies=proxies)  # 使用requests来发送请求
    html1 = loads(html1.text)
    url2 = 'https://osu.ppy.sh/users/' + str(config.user_id) + '/scores/best?mode=osu&offset=51&limit=51'
    html2 = session.get(url2, headers=headers, proxies=proxies)
    html2 = loads(html2.text)
    return html1, html2


class MapInfo:
    def __init__(self, dir):
        # dir = "D:/OSU/Songs/962593 inabakumori - Lost Umbrella (1)/inabakumori - Lost Umbrella (amanatu2) [Extra].osu"
        self.MapInfo = oppadc.OsuMap(file_path=dir)

    def note(self):
        i = self.MapInfo.amount_circle
        return i

    def slider(self):
        i = self.MapInfo.amount_slider
        return i


class GosuInfoStd:
    def __init__(self):
        r = httpx.get('http://localhost:24050/json')
        self.info = r.json()
        # self.info = loads(get('http://localhost:24050/json').content)
        # self.info = load(open('./package/gosu_output.json', 'r', encoding='utf8'))

    def state(self):
        i = self.info['menu']['state']
        return i

    def ur(self):
        i = self.info['gameplay']['hits']['unstableRate']
        return i

    def map_status(self):
        i = self.info['menu']['bm']['rankedStatus']
        return i

    def mode(self):
        i = self.info['menu']['gameMode']
        return i

    def map_dir(self):
        i = (self.info['settings']['folders']['songs'] + '\\' + self.info['menu']['bm']['path']['folder'] +
             '\\' + self.info['menu']['bm']['path']['file'])
        return i

    def songs_dir(self):
        i = self.info['settings']['folders']['songs']
        return i

    def bg_dir(self):
        i = self.info['settings']['folders']['songs'] + '\\' + self.info['menu']['bm']['path']['full']
        return i

    def title(self):
        i = self.info['menu']['bm']['metadata']['title']
        return i

    def artist(self):
        i = self.info['menu']['bm']['metadata']['artist']
        return i

    def cs(self):
        i = self.info['menu']['bm']['stats']['CS']
        return i

    def ar(self):
        i = self.info['menu']['bm']['stats']['AR']
        return i

    def od(self):
        i = self.info['menu']['bm']['stats']['OD']
        return i

    def hp(self):
        i = self.info['menu']['bm']['stats']['HP']
        return i

    def bpm_min(self):
        i = self.info['menu']['bm']['stats']['BPM']['min']
        return i

    def bpm_max(self):
        i = self.info['menu']['bm']['stats']['BPM']['max']
        return i

    def bid(self):
        i = self.info['menu']['bm']['id']
        return i

    def sid(self):
        i = self.info['menu']['bm']['set']
        return i

    def c300(self):
        i = self.info['resultsScreen']['300']
        return i

    def c100(self):
        i = self.info['resultsScreen']['100']
        return i

    def c50(self):
        i = self.info['resultsScreen']['50']
        return i

    def c0(self):
        i = self.info['resultsScreen']['0']
        return i

    def stars(self):
        i = self.info['menu']['bm']['stats']['fullSR']
        return i

    def slider_breaks(self):
        i = self.info['gameplay']['hits']['sliderBreaks']
        return i

    def pp_current(self):
        i = self.info['gameplay']['pp']['current']
        return i

    def player_name(self):
        i = self.info['gameplay']['name']
        return i

    def pp_ss(self):
        i = self.info['menu']['pp']['100']
        return i

    def pp_99(self):
        i = self.info['menu']['pp']['99']
        return i

    def pp_98(self):
        i = self.info['menu']['pp']['98']
        return i

    def pp_97(self):
        i = self.info['menu']['pp']['97']
        return i

    def pp_96(self):
        i = self.info['menu']['pp']['96']
        return i

    def pp_95(self):
        i = self.info['menu']['pp']['95']
        return i

    def pp_fc(self):
        i = self.info['gameplay']['pp']['fc']
        return i

    def mapper(self):
        i = self.info['menu']['bm']['metadata']['mapper']
        return i

    def difficulty(self):
        i = self.info['menu']['bm']['metadata']['difficulty']
        return i

    def key_count_k1(self):
        i = self.info['gameplay']['keyOverlay']['k1']['count']
        return i

    def key_count_k2(self):
        i = self.info['gameplay']['keyOverlay']['k2']['count']
        return i

    def key_count_m1(self):
        i = self.info['gameplay']['keyOverlay']['m1']['count']
        return i

    def key_count_m2(self):
        i = self.info['gameplay']['keyOverlay']['m2']['count']
        return i

    def score(self):
        i = self.info['resultsScreen']['score']
        return i

    def max_combo(self):
        i = self.info['resultsScreen']['maxCombo']
        return i

    def accuracy(self):
        i = self.info['gameplay']['accuracy']
        return i

    def time_length_full(self):
        i = self.info['menu']['bm']['time']['full']
        return i

    def mod_str(self):
        i = self.info['menu']['mods']['str']
        return i

    def rank_result(self):
        i = self.info['gameplay']['hits']['grade']['current']
        return i

    def pp_strains(self):
        i = self.info['menu']['pp']['strains']
        return i

    def ur_strains(self):
        i = self.info['gameplay']['hits']['hitErrorArray']
        return i


if __name__ == '__main__':
    a = MapInfo()
    print(a.note())
