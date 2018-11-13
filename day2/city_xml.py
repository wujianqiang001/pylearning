#coding=utf-8
import xlsxwriter,xlrd
import xml.etree.ElementTree as ET
import requests
def get_xmldata():
    tree = ET.parse("city.xml")
    city_list =[]
    for child in tree.iter(tag='d'):
        city_list.append(child.attrib)
    return city_list

def write_excel():
    city_list = get_xmldata()
    rk = xlsxwriter.Workbook("city.xlsx")
    rt = rk.add_worksheet("Sheet1")
    for i in range(len(city_list)):
        values = list(city_list[i].values())
        for j in range(len(values)):
            rt.write(i,j,values[-1-j])

    rk.close()
def get_weather():
    wb = xlsxwriter.Workbook("weatherinfo.xlsx")
    st = wb.add_worksheet("Sheet1")
    #wk = xlrd.open_workbook("weather.xlsx")
    #sh = wk.sheet_by_index(0)
    #rows = sh.nrows
    weather_list =[]
    for i in range(10):
        #weather_code = sh.cell(i,3).value
        resp = requests.get("http://www.weather.com.cn/data/sk/101010700.html")#%(weather_code))
        resp.encoding = "utf-8"
        weather_list.append(resp.json())
    #print(weather_list[0]["weatherinfo"]["city"])
    print(weather_list)

    for i in range(len(weather_list)):
        values = list(weather_list[i]["weatherinfo"].values())
        for j in range(len(values)):
            st.write(i,j,values[j])

    wb.close()
if __name__ == '__main__':
    #write_excel()
    get_weather()
