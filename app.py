import datetime

from bs4 import BeautifulSoup
import requests
import json
import mail
import main

FILE_NAME = 'prev.json'
heading = ["State", "CC-In", "CC-F", "Cured", "Death"]

needed_table = []
current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')


def save(x):
    with open(FILE_NAME, 'w') as f:
        json.dump(x, f)


def load():
    res = {}
    with open(FILE_NAME, 'r') as f:
        res = json.load(f)
    return res


def collect_content():
    final = []
    URL = 'https://www.mohfw.gov.in/'
    response = requests.get(URL).content
    soup = BeautifulSoup(response, "html.parser")
    table = soup.findChildren('table')
    global needed_table
    needed_table = table[0]
    all_rows = needed_table.find_all('tr')
    for row in all_rows:
        stats_row = []
        stats_row.append(row.find_all('td'))
        for spec_row in stats_row:
            ans = []
            for stats in spec_row:
                ans.append(stats.string)
            final.append(ans)
    final.pop(0)
    print(final)
    cur_data = {x[0]: {current_time: x[1:]} for x in final}
    past_data = load()

    if past_data != cur_data:
        mail.create_mail(needed_table, "", main.name_email()[0], main.name_email()[1])
        save(cur_data)

    else:
        print(f"No update at {current_time}")


def return_table():
    return needed_table


