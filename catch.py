from bs4 import BeautifulSoup
import requests
import pandas as pd

PlayerName = []
inn = []
catch = []
max_catch = []


def creat_xls():
    data = {
        "PlayerName": PlayerName,
        "Innings": inn,
        "Catch": catch,
        "Max Catch": max_catch,
    }
    df = pd.DataFrame(data)
    file_path = "CatchData.xlsx"
    df.to_excel(file_path, index=False)
    print("Data saved to", file_path)


def batsman_name():
    html_text = requests.get(
        "https://www.espncricinfo.com/records/tournament/fielding-most-catches-career/indian-premier-league-2023-15129"
    ).text

    soup = BeautifulSoup(html_text, "lxml")

    tables = soup.find("tbody")

    catcher_names = tables.find_all("a")
    for name in catcher_names:
        catcher_name = name.find("span").text
        PlayerName.append(catcher_name)

    infos = tables.find_all("td", class_="ds-min-w-max ds-text-right")
    # rint(infos)
    ved = []
    for vd in infos:
        vd1 = vd.text
        ved.append(vd1)

    count = 0

    for vd in ved:
        if vd == "2023-2023":
            count = 1
        else:
            if count == 2:
                inn.append(vd)
            elif count == 3:
                catch.append(vd)
            elif count == 4:
                max_catch.append(vd)
            count += 1
    print("player Name:", PlayerName)
    print("Innings:", inn)
    print("Catch:", catch)
    print("Max_Catch:", max_catch)
    creat_xls()


if __name__ == "__main__":
    batsman_name()
