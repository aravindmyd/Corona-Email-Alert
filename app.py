from bs4 import BeautifulSoup
import requests

heading = ["State", "CC-In", "CC-F", "Cured", "Death"]

needed_table = []


def collect_content():
    final = []
    states = []
    final_dic = {}

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
    final.pop()
    final.pop(0)
    final.pop()
    for i in range(len(final)):
        states.append(final[i][1])
        final[i].remove(final[i][0])

    for i in range(len(final)):
        final_dic[states[i]] = final[i]
    #print(final)
    return final


def return_table():
    collect_content()
    return needed_table
