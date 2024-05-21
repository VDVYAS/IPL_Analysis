from bs4 import BeautifulSoup
import requests
import pandas as pd

inn = []
No = []
Runs = []
HS = []
Ave = []
BF = []
SR = []
Hundred = []
fifty = []
zero = []
fours = []
sixs = []
BatsManNames = []


def creat_xls():
    data = {
        "PlayerName": BatsManNames,
        "Innings": inn,
        "Not Out": No,
        "Runs": Runs,
        "Highest Score": HS,
        "Average": Ave,
        "Ball Play": BF,
        "Strike Rate": SR,
        "Hundred": Hundred,
        "Fifty": fifty,
        "Duck": zero,
        "4s": fours,
        "6s": sixs,
    }
    df = pd.DataFrame(data)
    file_path = "BatsmanData.xlsx"
    df.to_excel(file_path, index=False)
    print("Data saved to", file_path)


def batsman_name():
    html_text = requests.get(
        "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/indian-premier-league-2023-15129"
    ).text

    soup = BeautifulSoup(html_text, "lxml")

    tables = soup.find(
        "tbody",
        # class_="ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line ds-mb-4",
    )

    batsman_names = tables.find_all(
        "span",
        class_="ds-text-tight-s ds-font-regular ds-text-typo-primary hover:ds-text-typo-primary-hover ds-block",
    )

    batsman_names = tables.find_all(
        "a",
        # class_="ds-cursor-pointer",
    )
    for name in batsman_names:
        batsman_name = name.find(
            "span",
            class_="ds-text-tight-s ds-font-regular ds-text-typo-primary hover:ds-text-typo-primary-hover ds-block",
        ).text
        BatsManNames.append(batsman_name)
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
                No.append(vd)
            elif count == 4:
                Runs.append(vd)
            elif count == 5:
                HS.append(vd)
            elif count == 6:
                Ave.append(vd)
            elif count == 7:
                BF.append(vd)
            elif count == 8:
                SR.append(vd)
            elif count == 9:
                Hundred.append(vd)
            elif count == 10:
                fifty.append(vd)
            elif count == 11:
                zero.append(vd)
            elif count == 12:
                fours.append(vd)
            elif count == 13:
                sixs.append(vd)
            count += 1

    creat_xls()


if __name__ == "__main__":
    batsman_name()
