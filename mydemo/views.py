from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from mydemo.models import EnergyElectric, Gdp, FixedInvest, HouseInvest, NbFixedInvest, NbHouseInvest, NbGdp
from mydemo.models import EnergyCoal
from django.db.models import Count
from django.http import JsonResponse
import json
from django.core import serializers


def gdp_year(request):
    gdp = Gdp.objects.filter(year=2017)
    type = []
    data = []
    total = 0
    for i in gdp:
        if i.city == '浙江省':
            total = i.gdp
        else:
            type.append(i.city)
            data.append(i.gdp)
    type.insert(0, '浙江省')
    data.insert(0, total)

    data2 = [0]
    for i in range(1, len(data)):
        if i == len(data) - 1:
            data2.append(0)
        else:
            data2.append(total - data[i])
            total = total - data[i]

    city = ['杭州市', '宁波市', '温州市', '嘉兴市', '湖州市', '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市']
    year = ['year', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
    city_gdp = []
    city_gdp.append(year)

    for item in city:
        gdp_hang = Gdp.objects.all().filter(city=item).order_by('year')
        test = [item]
        for i in gdp_hang:
            test.append(i.gdp)
        city_gdp.append(test)

    gdp_map = []
    for item in city:
        gdp_item = Gdp.objects.all().filter(city=item).filter(year=2019).values('gdp')
        item_data = {'name': item, 'value': gdp_item[0]['gdp']}
        gdp_map.append(item_data)

    city.append('浙江省')
    coal_data = []
    electric_data = []
    for item in city:
        temp1 = []
        temp2 = []
        coal_item = EnergyCoal.objects.all().filter(city=item).order_by('year')
        electric_item = EnergyElectric.objects.all().filter(city=item).order_by('year')
        for i in coal_item:
            temp1.append(i.num)
        coal_data.append(temp1)
        for i in electric_item:
            temp2.append(i.num)
        electric_data.append(temp2)
    # print(coal_data)
    # print(electric_data)

    y_data = []
    year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    for y in year:
        gdp_y = Gdp.objects.all().filter(year=y).order_by('city')
        coal_y = EnergyCoal.objects.all().filter(year=y).order_by('city')
        electric_y = EnergyElectric.objects.all().filter(year=y).order_by('city')

        city_temp = []
        for i in range(12):
            temp = [coal_y[i].num, electric_y[i].num, gdp_y[i].gdp, electric_y[i].city, electric_y[i].year]
            city_temp.append(temp)

        y_data.append(city_temp)

    # data for citys'fixed and house invest
    fixed_year = []
    for i in range(2000, 2018, 1):
        fixed_year.append(i)
    fixed_city = ['杭州市', '宁波市', '温州市', '嘉兴市', '绍兴市', '金华市']
    fixed_invest = []
    house_invest = []
    city_index = 0
    for c in fixed_city:
        temp1 = FixedInvest.objects.all().filter(city=c).order_by('year')
        temp2 = HouseInvest.objects.all().filter(city=c).order_by('year')
        year_index = 0
        for i in temp1:
            temp_invest1 = [city_index, year_index, i.num]
            fixed_invest.append(temp_invest1)
            year_index += 1
        year_index = 0
        for i in temp2:
            temp_invest2 = [city_index, year_index, i.num]
            house_invest.append(temp_invest2)
            year_index += 1
        city_index += 1

    # data for Ningbo'area fixed invest
    xAxisData = ['鄞州区', '象山县', '宁海县', '余姚市', '慈溪市', '奉化市']
    customData_fixed = []
    customData_house = []
    i = 0
    for area in xAxisData:
        area_fixed_invest = [i]
        invest_list = NbFixedInvest.objects.all().filter(area=area)
        for num in invest_list:
            area_fixed_invest.append(num.num)
        customData_fixed.append(area_fixed_invest)
        area_house_invest = [i]
        house_list = NbHouseInvest.objects.all().filter(area=area)
        for num in house_list:
            area_house_invest.append(num.num)
        customData_house.append(area_house_invest)
        i += 1

    legendData = ['trend']
    encodeY = []
    j = 2007
    dataList_fixed = []
    dataList_house = []
    for i in range(1, 11, 1):
        year_temp = j + i
        legendData.append(str(year_temp))
        encodeY.append(i)
        year_fixed_invest = []
        invest_list = NbFixedInvest.objects.all().filter(year=year_temp)
        for num in invest_list:
            year_fixed_invest.append(num.num)
        dataList_fixed.append(year_fixed_invest)
        year_house_invest = []
        house_list = NbHouseInvest.objects.all().filter(year=year_temp)
        for num in house_list:
            year_house_invest.append(num.num)
        dataList_house.append(year_house_invest)


    #data for Ningbo'gdp
    nb_gdp_year=['area']
    for i in range(2008,2018,1):
        nb_gdp_year.append(str(i))
    nb_gdp=[nb_gdp_year]

    nb_area=['鄞州区', '奉化区','余姚市', '慈溪市', '宁海县', '象山县']
    for i in nb_area:
        area_gdp=[i]
        gdp_list= NbGdp.objects.all().filter(area=i)
        for num in gdp_list:
            area_gdp.insert(1,num.num)
        nb_gdp.append(area_gdp)

    print(nb_gdp)

    return render(request, 'whole_page.html',
                  {'type': type, 'data': data, 'data2': data2, 'gdp': city_gdp, 'gdp_map': gdp_map, 'city': city,
                   'coal_data': coal_data, 'electric_data': electric_data, 'y_data': y_data, 'fixed_year': fixed_year,
                   'fixed_city': fixed_city, 'fixed_invest': fixed_invest, 'house_invest': house_invest,
                   'xAxisData': xAxisData, 'customData_fixed': customData_fixed, 'legendData': legendData,
                   'dataList_fixed': dataList_fixed, 'encodeY': encodeY, 'customData_house': customData_house,
                   'dataList_house': dataList_house,'nb_gdp':nb_gdp})
