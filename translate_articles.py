import deepl


def translate_articles(Articles):
    print("Translating articles...")
    translator = deepl.Translator("API_KEY")
    for a in Articles:
        # # to translate: title and leadtext
        a.Title = translator.translate_text(a.Title, target_lang="EN-US")
        a.Title = str(a.Title)
        try:
            a.Leadtext = translator.translate_text(a.Leadtext, target_lang="EN-US")
            a.Leadtext = str(a.Leadtext)
        except:
            print("leadtext not found for {} by {}".format(a.Title,a.Source_name))
            a.Leadtext = " "
    return Articles    

if __name__ == "__main__":
    translate_articles(None)