from prettytable import PrettyTable
from package import info
from package import pretty_table


def table1_filling(table, best1, best50):
    n = 1
    return1 = pretty_table.table_score_add(table, best1, n)
    table = return1[0]
    return2 = pretty_table.table_score_add(table, best50, return1[1])
    table = return2[0]

    return table


def table2_filling(table, best1, best50):
    n = 0
    total_pp = 0
    total_acc = 0
    for i in best1:
        total_pp += i['weight']['pp']
        total_acc += i['accuracy']
        n += 1
    for i in best50:
        total_pp += i['weight']['pp']
        total_acc += i['accuracy']
        n += 1
    return_ = pretty_table.table_bp_info_add(table, total_pp, total_acc, n)
    return return_


if __name__ == '__main__':
    best = info.get_best()
    table_bp = pretty_table.table_bp_score()
    table_bp = table1_filling(table_bp, best[0], best[1])
    print(table_bp)
    table_nbp = pretty_table.table_bp_info()
    table_nbp = table2_filling(table_nbp, best[0], best[1])
    print(table_nbp)
    input()
