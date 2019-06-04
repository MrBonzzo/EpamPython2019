# -*- coding: utf-8 -*-

# Задание 1: простейший parser/dumper
from collections import Counter, defaultdict


def get_dicts_from_json(path_to_json_file):
    with open(path_to_json_file, 'r') as json_file:
        json_string = json_file.read()[3:-3]
        objects = json_string.split('}, {"')
        objects = [obj.split(', "') for obj in objects]

        def pairs(d):
            return (d.split('": ')[0], d.split('": ')[1].strip('"'))
        objects = [dict(pairs(pair) for pair in obj) for obj in objects]
    return objects


def dump_to_json(list_of_dicts, dump_file_name):
    with open(dump_file_name, 'w') as json_file:
        replaces = [('\\\\', '\\'), ("{'", '{"'), ("'}", '"}')]
        replaces += [("': '", '": "'), ("', '", '", "'), ('\', ', '", ')]
        replaces += [(', \'', ', "'), ("': ", '": '), ("['", '["')]
        replaces += [("']", '"]'), ('"null"', 'null')]
        str_to_write = str(list_of_dicts)
        for r in replaces:
            str_to_write = str_to_write.replace(*r)
        json_file.write(f'{str_to_write}')


# Задание 2: объединение файлов, удаление дубликатов, сортировка


def get_unique_dicts(list_of_dicts):
    list_of_dict_items = [tuple(d.items()) for d in list_of_dicts]
    list_of_unique_dicts = [dict(s) for s in set(list_of_dict_items)]
    return list_of_unique_dicts


def sort_list_of_dicts(list_of_dicts):

    def key_to_sort(dict_elem):
        if dict_elem['price'] == 'null':
            return (1, dict_elem['variety'].lower())
        else:
            return (-int(dict_elem['price']), dict_elem['variety'].lower())
    sorted_list = sorted(list_of_dicts, key=key_to_sort)
    return sorted_list


# Задание 3: сбор статистики


def varieties_statistic(winedata):
    varieties = ['Gew\\u00fcrztraminer', 'Riesling']
    varieties += ['Merlot', 'Madera', 'Tempranillo', 'Red Blend']
    stats = ['average_price', 'min_price', 'max_price']
    stats += ['region', 'country', 'average_score']
    var_stat = {v: {s: 0 for s in stats} for v in varieties}
    for var in var_stat:
        var_stat[var]['min_price'] = float('inf')
        var_stat[var]['region'] = Counter()
        var_stat[var]['country'] = Counter()
        var_stat[var]['sum_price'] = 0
        var_stat[var]['sum_price_cnt'] = 0
        var_stat[var]['sum_score'] = 0
        var_stat[var]['sum_score_cnt'] = 0

    for variety in varieties:
        price = []
        for wine in winedata:
            if wine['price'] != 'null' and wine['variety'] == variety:
                price.append(int(wine['price']))
        if len(price):
            min_price, max_price = min(price), max(price)
            avg_price = round(sum(price) / len(price), 2)
        else:
            min_price, max_price, avg_price = 0, 0, 0
        var_stat[variety]['min_price'] = min_price
        var_stat[variety]['max_price'] = max_price
        var_stat[variety]['average_price'] = avg_price
        score = []
        for wine in winedata:
            if wine['points'] != 'null' and wine['variety'] == variety:
                score.append(int(wine['points']))
        if len(score):
            avg_score = round(sum(score) / len(score), 2)
        else:
            avg_score = 0
        var_stat[variety]['average_score'] = avg_score

    for wine in winedata:
        variety = wine['variety']
        if variety in varieties:
            if wine['region_1'] != 'null':
                var_stat[variety]['region'] += Counter([wine['region_1']])
            if wine['country'] != 'null':
                var_stat[variety]['country'] += Counter([wine['country']])
    for var in var_stat:
        if var_stat[var]['region']:
            var_stat[var]['region'] = var_stat[var]['region'].most_common(1)
            var_stat[var]['region'] = var_stat[var]['region'][0][0]
        else:
            var_stat[var]['region'] = 'null'
        if var_stat[var]['country']:
            var_stat[var]['country'] = var_stat[var]['country'].most_common(1)
            var_stat[var]['country'] = var_stat[var]['country'][0][0]
        else:
            var_stat[var]['country'] = 'null'
        var_stat_dict_keys = var_stat[var].keys()
        for wine_param in set(var_stat_dict_keys) - set(stats):
            del var_stat[var][wine_param]
    return var_stat


def common_statistic(winedata):
    price_list = set(int(w['price']) for w in winedata if w['price'] != 'null')
    max_price, min_price = max(price_list), min(price_list)
    most_expensive_wine = []
    for wine in winedata:
        if wine['price'] != 'null' and int(wine['price']) == max_price:
            most_expensive_wine.append(wine['title'])
    cheapest_wine = []
    for wine in winedata:
        if wine['price'] != 'null' and int(wine['price']) == min_price:
            cheapest_wine.append(wine['title'])
    score = set(int(w['points']) for w in winedata if w['points'] != 'null')
    max_score, min_score = max(score), min(score)
    counter, price = defaultdict(int), defaultdict(int)
    for wine in winedata:
        if wine['price'] != 'null' and wine['country'] != 'null':
            counter[wine['country']] += 1
            price[wine['country']] += int(wine['price'])
    avg_price_list = [(price[p] / counter[p], p) for p in price]
    max_avg_price = max(avg_price_list, key=lambda x: x[0])[1]
    min_avg_price = min(avg_price_list, key=lambda x: x[0])[1]
    counter, score = defaultdict(int), defaultdict(int)
    for wine in winedata:
        if wine['points'] != 'null' and wine['country'] != 'null':
            counter[wine['country']] += 1
            score[wine['country']] += int(wine['points'])
    avg_score_list = [(score[s] / counter[s], s) for s in score]
    max_avg_score = max(avg_score_list, key=lambda x: x[0])[1]
    min_avg_score = min(avg_score_list, key=lambda x: x[0])[1]
    tasters = Counter()
    for wine in winedata:
        if wine['taster_name'] != 'null':
            tasters += Counter([wine['taster_name']])
    most_active_commentator = tasters.most_common(1)[0][0]
    common_stat = {'most_expensive_wine': most_expensive_wine}
    common_stat['cheapest_wine'] = cheapest_wine
    common_stat['highest_score'] = max_score
    common_stat['lowest_score'] = min_score
    common_stat['most_expensive_coutry'] = max_avg_price
    common_stat['cheapest_coutry'] = min_avg_price
    common_stat['most_rated_country'] = max_avg_score
    common_stat['underrated_country'] = min_avg_score
    common_stat['most_active_commentator'] = most_active_commentator
    return common_stat


# Задание 4: markdown

def dump_stat_to_markdown(stat, markdown_file_name):
    with open(markdown_file_name, 'w') as md_file:
        md_file.write('# Statistic\n\n')
        md_file.write('## Certain wines\n')
        wine_stat = stat['statistic']['wine']
        wine_params = list(wine_stat['Merlot'].keys())
        table_head = f"| |{'|'.join(wine_params)}|"
        table_head = table_head.replace('_', ' ').title()
        delimiter = '-|'*(len(wine_params) + 1)
        md_file.write(f'{table_head}\n')
        md_file.write(f'{delimiter}\n')
        for wine in wine_stat:
            raw = f'|**{wine}**|'
            for params in wine_params:
                if wine_stat[wine][params] == 'null':
                    parameter_value = ' '
                else:
                    parameter_value = wine_stat[wine][params]
                raw += f'{parameter_value}|'
            md_file.write(f'{raw}\n')
        md_file.write('\n## Whole wines\n')
        md_file.write('* Most expensive wine:\n')
        for wine in stat['statistic']['most_expensive_wine']:
            md_file.write(f'\t* _{wine}_\n')
        md_file.write('* Cheapest wine:\n')
        for wine in stat['statistic']['cheapest_wine']:
            md_file.write(f'\t* _{wine}_\n')
        for s in stat['statistic']:
            if s not in ('wine', 'most_expensive_wine', 'cheapest_wine'):
                line = f"* {s.replace('_', ' ').capitalize()}: "
                line += f"_{stat['statistic'][s]}_\n"
                md_file.write(line)


if __name__ == '__main__':
    winedata_1 = get_dicts_from_json('winedata_1.json')
    winedata_2 = get_dicts_from_json('winedata_2.json')
    winedata_full = get_unique_dicts(winedata_1 + winedata_2)
    winedata_full = sort_list_of_dicts(winedata_full)
    dump_to_json(winedata_full, 'winedata_full.json')
    variety_statistic = varieties_statistic(winedata_full)
    common_statistic = common_statistic(winedata_full)
    whole_stat = {"statistic": {"wine": variety_statistic, **common_statistic}}
    dump_to_json(whole_stat, 'statistic.json')
    dump_stat_to_markdown(whole_stat, 'statistic.md')
