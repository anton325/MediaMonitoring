import warning
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import concurrent.futures
import time


# todo: eval dont doulbe select article even if chatgpt dictates it


import webscraping.dataclass_article as dataclass_article
import webscraping.scrape_wiwo as scrape_wiwo
import webscraping.scrape_handelsblatt as scrape_handelsblatt
import webscraping.scrape_ingenieur as scrape_ingenieur
import webscraping.scrape_mama as scrape_mama
import webscraping.scrape_sz as scrape_sz
import webscraping.scrape_faz as scrape_faz
import webscraping.scrape_produktion as scrape_produktion
import webscraping.scrape_nzz as scrape_nzz
import webscraping.scrape_spiegel as scrape_spiegel
import webscraping.scrape_deutschlandfunk as scrape_deutschlandfunk
import webscraping.scrape_welt as scrape_welt
import webscraping.scrape_capital as scrape_capital
import webscraping.scrape_tageschau as scrape_tagesschau
import webscraping.scrape_tagesspiegel as scrape_tagesspiegel
import webscraping.scrape_logistikheute as scrape_logistikheute
import webscraping.scrape_industryofthings as scrape_industryofthings
import webscraping.scrape_elektroniknet as scrape_elektroniknet

import prepare_query
import api
import translate_articles
import match_answers
import count_tokens
import to_docx
import filter_articles

one_bool = True

PHASE_SCRAPE = one_bool
GATHER = one_bool
PHASE_SANITY_CHECK = one_bool
PHASE_FILTER = one_bool
PHASE_SELECT = one_bool
PHASE_EVAL = True
PHASE_APPEND = True
PHASE_TRANSLATE = True

prepare_query.create_briefing_folder()

CHATGPTVERSION = 4

if PHASE_SCRAPE:
    scraping_functions = [scrape_wiwo.scrape_wiwo,
                        scrape_handelsblatt.scrape_handelsblatt,
                        scrape_ingenieur.scrape_ingenieur,
                        scrape_mama.scrape_mama,
                        scrape_logistikheute.scrape_logistikheute,
                        scrape_tagesspiegel.scrape_tagesspiegel,
                        scrape_sz.scrape_sz,
                        scrape_produktion.scrape_produktion,
                        scrape_faz.scrape_faz,
                        scrape_nzz.scrape_nzz,
                        scrape_elektroniknet.scrape_elektroniknet,
                        scrape_spiegel.scrape_spiegel,
                        scrape_deutschlandfunk.scrape_deutschlandfunk,
                        scrape_welt.scrape_welt,
                        scrape_tagesschau.scrape_tagesschau,
                        scrape_industryofthings.scrape_industryofthings,
                        scrape_capital.scrape_capital]

    # Define a function to scrape articles
    def scrape_articles_helper_function(scraping_function):
        # here try and except to avoid errors. Also save everything to be able to reload stuff?
        source = scraping_function.__name__
        new_articles = prepare_query.check_if_temp_exists(source)
        if new_articles != None:
            print("{} temp exists, loading".format(source))
            return new_articles
        new_articles = scraping_function()
        prepare_query.temp_save_articles(new_articles,source)
        return new_articles

    Articles = []

    start_time = time.time()

    # Create a ThreadPoolExecutor with a specified number of threads (adjust as needed)
    # scrape 0.05, num_threads = 2 -> 200s
    # scrape 0.05, num_threads = 4 -> 160s
    # scrape 0.05, num_threads = 6 -> 180s
    num_threads = 2  # You can adjust this based on your system's capabilities
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Map the scraping functions to the executor for parallel execution
        futures = executor.map(scrape_articles_helper_function, scraping_functions)

        # Collect the results
        for new_articles in futures:
            Articles.extend(new_articles)

    # dataclass_article.custom_print_articles(Articles)

    print("Scraping took {} seconds".format(time.time() - start_time))

if GATHER:
    print("Gathering...")
    Articles = prepare_query.load_temp_pickles()
    print("Remove duplicates...")
    Articles = prepare_query.remove_duplicate_articles(Articles)

    introduction,articles_to_be_judged = prepare_query.prepare_query(Articles)
    print("Create checkpoint...")
    prepare_query.create_checkpoint(Articles)
    count_tokens.estimate_costs(introduction+articles_to_be_judged,version = CHATGPTVERSION)
    print("Create Word document...")
    to_docx.create_word_document(Articles,language = "all")

if PHASE_SANITY_CHECK:
    if not PHASE_SCRAPE:
        introduction, articles_to_be_judged, Articles = prepare_query.load_checkpoint()
    warning.check_media_sources(Articles)

if PHASE_FILTER:
    if not PHASE_SANITY_CHECK:
        introduction, articles_to_be_judged, Articles = prepare_query.load_checkpoint()
    print("Number of Articles: {}".format(len(Articles)))
    Articles = filter_articles.filter_articles_by_date(Articles)
    print("Number of Articles after filter by date: {}".format(len(Articles)))
    try:
        Articles = filter_articles.filter_already_seen_exact_match(Articles)
        print("Number of Articles after filter by matching: {}".format(len(Articles)))
        to_docx.create_word_document(Articles,language = "beforembedding")
        Articles = filter_articles.filter_already_seen_embeddings(Articles)
        print("Number of Articles after filter by embedding: {}".format(len(Articles)))
        to_docx.create_word_document(Articles,language = "afterembedding")
    except:
        print("Couldnt filter by yesterday")
    Articles = filter_articles.filter_same_topic_articles(Articles)
    print("Number of Articles after filter by embedding only today's articles: {}".format(len(Articles)))
    to_docx.create_word_document(Articles,language = "aftertodayembedding")
    prepare_query.create_checkpoint(Articles)
    introduction,articles_to_be_judged = prepare_query.prepare_query(Articles)

    print("Costs after filtering:")
    count_tokens.estimate_costs(introduction+articles_to_be_judged,version = CHATGPTVERSION)

if PHASE_SELECT:    
    if not PHASE_FILTER:
        introduction, articles_to_be_judged, Articles = prepare_query.load_checkpoint()

    count_tokens.estimate_costs(introduction+articles_to_be_judged,version = CHATGPTVERSION)
    print("Reaching out to ChatGPT...")
    answer = api.ask_chatgpt(introduction,articles_to_be_judged,version = CHATGPTVERSION)

if PHASE_EVAL:
    if not PHASE_SELECT:
        answer = prepare_query.load_answer()
        introduction, articles_to_be_judged, Articles = prepare_query.load_checkpoint()
    selected_articles, articles_not_found = match_answers.eval_answer(answer,Articles)
    if len(selected_articles) < 2:
        print("Weniger als 2 Artikel gefunden, clean and repeat")
        answer_cleaned = match_answers.clean_response_quotes(answer)
        selected_articles, articles_not_found = match_answers.eval_answer(answer_cleaned,Articles)
    
    if len(selected_articles) < 2:
        print("Weniger als 2 Artikel gefunden, clean and repeat")
        answer_cleaned = match_answers.clean_response_dash(answer)
        selected_articles, articles_not_found = match_answers.eval_answer(answer_cleaned,Articles)
    
    if len(selected_articles) < 2:
        raise NotImplementedError("This GPT return format seems to take the script off guard")

    prepare_query.export_unclassified_articles(articles_not_found)
    prepare_query.export_selected_articles(selected_articles)

    prepare_query.create_checkpoint(selected_articles,"clean")

    to_docx.create_word_document(selected_articles,language = "DE")


"""
Phase append
Die Manuell erstellt Artikel werden dazugeladen und auch übersetzt und auch eingefügt in das Word Dokument
"""
appended_articles = None
if PHASE_APPEND:
    try:
        appended_articles = prepare_query.load_added_articles()
    except:
        print("nothing to append")

if PHASE_TRANSLATE:
    """
    translated arcticles is List of class Articles
    """
    if appended_articles is not None:
        selected_articles.extend(appended_articles)
    translated_articles = translate_articles.translate_articles(selected_articles) 

    to_docx.create_word_document(translated_articles,language = "EN")
    to_docx.create_word_document(translated_articles,language = "_edited")