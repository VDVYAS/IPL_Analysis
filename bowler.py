from bs4 import BeautifulSoup
import requests
import pandas as pd

BowlerNames = []
inn = []
Ball = []
Overs = []
Mdns = []
Runs = []
Wtks = []
BBI = []
Ave = []
Econ = []
SR = []
fours_wtks = []
five_wtks = []


def creat_xls():
    data = {
        "PlayerName": BowlerNames,
        "Innings": inn,
        "Ball": Ball,
        "Over": Overs,
        "Mdns": Mdns,
        "Runs": Runs,
        "Wtks": Wtks,
        "BBI": BBI,
        "Average": Ave,
        "Economy": Econ,
        "Strike Rate": SR,
        "4_Wtks": fours_wtks,
        "6_Wtks": five_wtks,
    }
    df = pd.DataFrame(data)
    file_path = "BowlerData.xlsx"
    df.to_excel(file_path, index=False)
    print("Data saved to", file_path)


def batsman_name():
    html_text = requests.get(
        "https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/indian-premier-league-2023-15129"
    ).text

    soup = BeautifulSoup(html_text, "lxml")

    tables = soup.find("tbody")

    bowler_names = tables.find_all("a")
    for name in bowler_names:
        bowler_name = name.find("span").text
        BowlerNames.append(bowler_name)

    print(BowlerNames)

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
                Ball.append(vd)
            elif count == 4:
                Overs.append(vd)
            elif count == 5:
                Mdns.append(vd)
            elif count == 6:
                Runs.append(vd)
            elif count == 7:
                Wtks.append(vd)
            elif count == 8:
                BBI.append(vd)
            elif count == 9:
                Ave.append(vd)
            elif count == 10:
                Econ.append(vd)
            elif count == 11:
                SR.append(vd)
            elif count == 12:
                fours_wtks.append(vd)
            elif count == 13:
                five_wtks.append(vd)
            count += 1
    creat_xls()


if __name__ == "__main__":
    batsman_name()
