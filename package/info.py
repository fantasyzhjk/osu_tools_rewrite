from requests import get
import json


class GosuInfoStd:
    def __init__(self):
        # self.info = loads(get('http://localhost:24050/json').content)
        self.info = json.load(open('./package/gosu_output.json', 'r', encoding='utf8'))

    def state(self):
        i = self.info['menu']['state']
        return i

    def mode(self):
        i = self.info['menu']['gameMode']
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
        i = self.info['menu']['bm']['stats']['SR']
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

    def pp_97(self):
        i = self.info['menu']['pp']['97']
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
