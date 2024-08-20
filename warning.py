import pathlib
import os
import datetime

WARNING_FILE_NAME = "WARNING.txt"

LIST_OF_MEDIA_AND_NUM_DESIRED_ARTICLES = {
    'WirtschaftsWoche' : 10,
    'Handelsblatt' : 10,
    'Ingenieur.de' : 10,
    'Manager-Magazin' : 10,
    'Sueddeutsche' : 10,
    'Produktion.de' : 10,
    'FAZ' : 10,
    'NZZ' : 10,
    'Spiegel.de' : 10,
    'WELT' : 10,
    'Capital' : 10,
    'Deutschlandfunk' : 10,
    'Tagesschau' : 5,
    'Tagesspiegel' : 5,
    'Industry-of-things' : 5,
    'Logistik-heute' : 5,
    'Elektroniknet.de' : 5

}

def delete_warning_file():
    if os.path.isfile(pathlib.Path(WARNING_FILE_NAME)):
        os.remove(pathlib.Path(WARNING_FILE_NAME))

def write_warning_file(missing_media_articles, dict_source_and_number):

    message = "Dieses Dokument wurde am {} automatisiert erstellt.\
              \nEs enthält Informationen über Websites, die eventuell nicht mehr zu erreichen sind und wieviel generell pro Website gescapred wurde\n".format(datetime.datetime.now())

    for media_source in missing_media_articles:
        message += "Von der Quelle {} wurden {} Artikel gefunden\n".format(media_source,missing_media_articles[media_source])
    message += "\n"
    for media_source in dict_source_and_number:
        message += "Von der Quelle {} wurden {} Artikel gefunden\n".format(media_source,dict_source_and_number[media_source])
    today = datetime.datetime.now()
    month = today.month
    if month < 10:
        month = '0'+str(month)
    day = today.day
    if day < 10:
        day = '0' + str(day)
    year = today.year - 2000
    DATE_STRING = "{}{}{}".format(year,month,day)
    SUBFOLDER_NAME = "Messages"+DATE_STRING

    with open(pathlib.Path("Messages",SUBFOLDER_NAME,WARNING_FILE_NAME),'w') as f:
        f.write(message)

def check_media_sources(Articles):
    dict_source_and_number = {}
    for article in Articles:
        if dict_source_and_number.get(article.Source_name,None) == None:
            dict_source_and_number[article.Source_name] = 1
        else:
            dict_source_and_number[article.Source_name] += 1

    warning_media_sources = {}
    for media_source in LIST_OF_MEDIA_AND_NUM_DESIRED_ARTICLES:
        number_of_articles = 0
        for a in Articles:
            if a.Source_name == media_source:
                number_of_articles += 1
        if LIST_OF_MEDIA_AND_NUM_DESIRED_ARTICLES[media_source] > number_of_articles:
            warning_media_sources[media_source] = number_of_articles
    # if not warning_media_sources:
    #     delete_warning_file()
    # else:
    write_warning_file(warning_media_sources,dict_source_and_number)
        



