def eval_answer(answer,Articles):

    selected_articles = []
    articles_that_were_not_found = []

    for headline in answer.split("\n"):
        if headline == "":
            continue
        # if "Schaeffler" in headline:
        #     print(headline)
        category = headline.split(":")[0]
        # print(category)
        title = ""
        for part in headline.split(":")[1:]:#.strip()
            title += part+":"
        title = title[:-1].strip()

        # find article in Articles:
        found = False
        for a in Articles:
            # if "Schaeffler" in title :
            #     print(title)
            #     print(category)
            #     if "Schaeffler" in a.Title:
            #         print(a)
            if a.Title == title and a.Category == category:
                selected_articles.append(a)
                found = True
                break
        if not found:
            # print("{} not found".format(headline))
            articles_that_were_not_found.append(headline)

    # check if we can match the articles that were not found using only the headline

    for headline in articles_that_were_not_found:
        for a in Articles:
            if a in selected_articles:
                continue

            if a.Title == headline:
                selected_articles.append(a)
                articles_that_were_not_found.remove(headline)
                break


    return selected_articles, articles_that_were_not_found

def clean_response_quotes(answer:str) -> str:
    new_answer = ""
    for b in answer.split("\n"):
        if b != "":
            if b[0] =='"' and b[-1] == '"':
                new = b[1:-1]
                new_answer += new + "\n"
    print("Die korrigierte Answer von ChatGPT sieht so aus: ")
    print(new_answer)
    return  new_answer

def clean_response_dash(answer:str) -> str:
    new_answer = ""
    for b in answer.split("\n"):
        if b != "":
            if b[0] =='-':
                new = b[2:] # skip dash AND space after dash
                new_answer += new + "\n"
    print("Die korrigierte Answer von ChatGPT sieht so aus: ")
    print(new_answer)
    return  new_answer

if __name__ == "__main__":
    eval_answer(None,None)