import vk
import config
import json
import matplotlib.pyplot as plt
import time
from datetime import datetime

groups = {'hse': -181137921, 'msu': -185065728}

session = vk.Session(access_token=config.vk)
vk_api = vk.API(session)

def is_hayer(uni_id, id):
    comm = vk_api.wall.getComments(owner_id=uni_id, post_id=id, count=100, v=5.103)
    time.sleep(1)
    for com in comm['items']:
        if com['text'].lower() == 'в отложке':
            return True
    return False

def update():
    for uni, uni_id in groups.items():
        with open(uni + '.json', 'r') as file:
            stat = json.load(file)
        posts = vk_api.wall.get(owner_id=uni_id, count=100, v=5.103)
        time.sleep(1)
        for post in posts['items']:
            end = post['text'].find('\n')
            if end == -1:
                end = len(post['text'])
            try:
                num = int(post['text'][:end])
            except Exception as e:
                print(e)
                continue
            if str(post['date']) not in stat:
                id = post['id']
                date = post['date']
                end = post['text'].find('\n')
                is_posted = is_hayer(uni_id, id)
                stat[date] = {'id': id, 'num': num, 'date': date, 'is_posted': is_posted}
            elif not stat[str(post['date'])]['is_posted']:
                stat[str(post['date'])]['is_posted'] = is_hayer(uni_id, post['id'])
        with open(uni + '.json', 'w') as file:
            json.dump(stat, file)


def graphic(start_date, end_date, uni='hse'):
    with open(uni + '.json', 'r') as file:
        stat = json.load(file)
    start_date = int(datetime.strptime(start_date, '%d.%m.%Y').strftime("%s"))
    end_date = int(datetime.strptime(end_date, '%d.%m.%Y').strftime("%s"))
    
    stat_block = {}
    stat_higher = {}
    
    for str_date, post in stat.items():
        if start_date <= int(str_date) <= end_date:
            num = post['num']
            is_posted = post['is_posted']
            if num in stat_block:
                stat_block[num] += 1
            else:
                stat_block[num] = 1
            if is_posted:
                if num in stat_higher:
                    stat_higher[num] += 1
                else:
                    stat_higher[num] = 1

    print(stat_block)
    print(stat_higher)

    stat_b = []
    stat_b_keys = []
    stat_h = []
    stat_h_keys = []

    for num, count in stat_block.items():
        stat_b_keys.append(num)
    for num, count in stat_higher.items():
        stat_h_keys.append(num)

    stat_b_keys.sort()
    stat_h_keys.sort()

    for num in stat_b_keys:
        stat_b.append(stat_block[num])
    for num in stat_h_keys:
        stat_h.append(stat_higher[num])

    stat_b_keys = list(map(str, stat_b_keys))
    stat_h_keys = list(map(str, stat_h_keys))

    plt.bar(stat_b_keys, stat_b, label='записи в блокчейне')
    plt.bar(stat_h_keys, stat_h, label='записи в ' + uni)
    plt.legend()
    plt.title("Количество постов в " + uni + " в интервале\n[" + datetime.utcfromtimestamp(start_date).strftime('%d.%m.%Y %H:%M:%S') + " - " + datetime.utcfromtimestamp(end_date).strftime('%d.%m.%Y %H:%M:%S') + ']')
    plt.savefig('high.png')
    
