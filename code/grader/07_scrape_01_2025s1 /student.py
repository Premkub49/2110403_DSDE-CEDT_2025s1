from bs4 import BeautifulSoup
from lxml import etree
import dateparser


def open_file(file_path: str) -> BeautifulSoup:
    with open(file_path, "r") as file:
        global html_file
        html_file = file.read()
    soup = BeautifulSoup(html_file, "lxml")
    return soup


def Q1(file_path):  # DO NOT modify this line
    soup = open_file(file_path)
    # all_days = soup.select("html.fontawesome-i2svg-active.fontawesome-i2svg-complete body form#form1 div#container div.content-main-fullwidth div.bdr-10.p-5.mt-10 div.col-list div#print_div1 div div.bud-day")
    all_days = soup.find_all("div", class_="bud-day-col")
    all_days_as_date = [0, 0, 0, 0, 0, 0, 0]
    dict_day = {
        "จันทร์": 0,
        "อังคาร": 1,
        "พุธ": 2,
        "พฤหัสบดี": 3,
        "ศุกร์": 4,
        "เสาร์": 5,
        "อาทิตย์": 6
    }
    for day in all_days:
        date_time = day.get_text(strip=True)
        if "วัน" not in date_time or "(" in date_time:
            continue
        weekday = date_time.split(" ")[0].replace("วัน", "").replace("ที่", "")
        if weekday not in dict_day:
            raise Exception("bruh")
            continue
        all_days_as_date[dict_day[weekday]] += 1
    return all_days_as_date


def Q2(file_path):  # DO NOT modify this line
    soup = open_file(file_path)
    spe_days = soup.find_all(title="วันวิสาขบูชา")[0].parent.parent.find_all()[0].text
    return spe_days


exec(input().strip())  # do not delete this line
