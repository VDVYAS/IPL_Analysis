from bs4 import BeautifulSoup
import requests
import pandas as pd

PlayerName = []
inn = []
dismissals = []
ct = []
st = []
max_dt = []


def creat_xls():
    data = {
        "PlayerName": PlayerName,
        "Innings": inn,
        "Dismissals": dismissals,
        "caght_as_Keeper": ct,
        "Stumping": st,
        "Max_Dismissals": max_dt,
    }
    df = pd.DataFrame(data)
    file_path = "WicketData.xlsx"
    df.to_excel(file_path, index=False)
    print("Data saved to", file_path)


def batsman_name():
    html_text = requests.get(
        "https://www.espncricinfo.com/records/tournament/keeping-most-dismissals-career/indian-premier-league-2023-15129"
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
                dismissals.append(vd)
            elif count == 4:
                ct.append(vd)
            elif count == 5:
                st.append(vd)
            elif count == 6:
                max_dt.append(vd)
            count += 1
    print("player Name:", PlayerName)
    print("Innings:", inn)
    print("Catch:", ct)
    print("Max_Catch:", max_dt)
    print("stumping:", st)
    creat_xls()


if __name__ == "__main__":
    batsman_name()
