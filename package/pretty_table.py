from prettytable import PrettyTable


def table_bp_score():
    table = PrettyTable()
    table.field_names = ["", "原pp", "权重", "折合后", "acc", "Stars", "bid", "标题", "Mods", "游玩时间"]
    table.align["Stars"] = "l"
    table.align["bid"] = "l"
    table.align["折合后"] = "l"
    table.align["原pp"] = "l"
    table.align["权重"] = "l"
    table.align[""] = "l"
    table.align["游玩时间"] = "l"
    return table


def table_score_add(table, best, n):
    for i in best:
        mods = ''
        if not i['mods']:
            pass
        else:
            for m in i['mods']:
                mods += str(m)
        table.add_row([n,
                       round(i['pp'], 2),
                       str(round(i['weight']['percentage'], 2)) + '%',
                       round(i['weight']['pp'], 2),
                       str(round((i['accuracy'] * 100), 2)) + '%',
                       i['beatmap']['difficulty_rating'],
                       i['beatmap']['id'],
                       i['beatmapset']['title_unicode'],
                       mods,
                       i['created_at']])
        n += 1
    return table, n


def table_bp_info():
    table = PrettyTable()
    table.field_names = (['Total PP', 'Total Acc', 'BP count'])
    return table


def table_bp_info_add(table, total_pp, total_acc, nbp):
    table.add_row([round(total_pp, 2), round(total_acc / nbp * 100, 2), nbp])
    return table
