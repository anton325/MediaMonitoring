import datetime

month_lookup = {
    'Januar' : 1,
    'Februar' : 2,
    'März' : 3,
    'April' : 4,
    'Mai' : 5,
    'Juni' : 6,
    'Juli' : 7,
    'August' : 8,
    'September' : 9,
    'Oktober' : 10,
    'November' : 11,
    'Dezember' : 12,
}

month_lookup_abreviations = {
    'Jan.' : 1,
    'Feb.' : 2,
    'Mär.' : 3,
    'Apr.' : 4,
    'Mai.' : 5,
    'Jun.' : 6,
    'Jul.' : 7,
    'Aug.' : 8,
    'Sep.' : 9,
    'Okt.' : 10,
    'Nov.' : 11,
    'Dez.' : 12,
}

def simple_point_split(date):
    year = date.split(".")[2]
    month = date.split(".")[1]
    day = date.split(".")[0]
    return year,month,day

def parse_date(date,source):
    
    if source == "WELT":
        if "Uhr" in date:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
        else:
            date_date = date.split(":")
            year,month,day = simple_point_split(date_date)
        
    # "Stand: 12.10.2023 14:11 Uhr"
    elif source == "Tagesschau":
        date_date = date.replace("Stand: ","").split(" ")[0]
        year,month,day = simple_point_split(date_date)

    elif source == "Tagesspiegel":
        # 11.10.2023, 14:09 Uhr
        # Heute, 12:49 Uhr
        if "Heute" in date:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
        else:
            date_date = date.split(",")[0]
            year,month,day = simple_point_split(date_date)
    elif source == "Logistik-heute":
        year,month,day = simple_point_split(date)

    # 11. Oktober 2023, 14:10 Uhr | Tobias Schlichtmeier
    elif source == "Elektroniknet.de":
        date_date = date.split("|")[0]
        date_date = date_date.split(",")[0]
        day = date_date.split(" ")[0].split(".")[0]
        month = month_lookup[date_date.split(" ")[1]]
        year = date_date.split(" ")[2]


    # handelsblatt "08.10.2023 - 07:20 Uhr"
    elif len(date.split("-")) > 1:
        # print("handelsblatt")
        date_date = date.split("-")[0]
        # print(date_date)
        year,month,day = simple_point_split(date_date)
    
    # ingenieur, manager-magazin "07.10.2023, 12.38 Uhr"
    elif len(date.split(",")) > 1 and len(date.split(" ")) < 4:
        # print("mama")
        date_date = date.split(",")[0]
        year,month,day = simple_point_split(date_date)

    # wiwo "08. Oktober 2023, 10:20"
    elif len(date.split(" ")) > 1 and len(date.split("|")) < 2:
        # print("wiwo")
        year = date.split(" ")[2].split(",")[0]
        month = month_lookup[date.split(" ")[1]]
        day = date.split(" ")[0].split(".")[0]
    
    # 09. Okt. 2023 | 07:56 Uhr
    elif len(date.split("|")) > 1 and date.split(" ")[0] != "Von":
        date_date = date.split("|")[0]
        year = date_date.split(" ")[2]
        month = month_lookup_abreviations[date_date.split(" ")[1]]
        day = date_date.split(" ")[0].split(".")[0]

    # manchmal deutschlandfunk: "Von Tobias Pastoors | 24.09.2023"
    elif date.split(" ")[0] == "Von":
        date_date = date.split("|")[1]
        year,month,day = simple_point_split(date_date)

    else:
        year,month,day = simple_point_split(date)
    
    parsed_date = datetime.datetime(int(year),int(month),int(day))
    return parsed_date

if __name__ == "__main__":
    date = "08.10.2023 - 07:20 Uhr"
    # date = "07.10.2023, 12.38 Uhr"
    # date = "8. Oktober 2023, 10:20 Uhr"
    date = "09. Okt. 2023 | 07:56 Uhr"
    date = "11.10.2023, 05.30 Uhr"
    date = "Von Tobias Pastoors | 24.09.2023"
    date = "24.09.2023"
    date = "11. Oktober 2023, 14:10 Uhr | Tobias Schlichtmeier"
    print(parse_date(date,"Elektroniknet.de"))
    print(type(parse_date(date,"Elektroniknet.de")))
