import tiktoken

def estimate_costs(question,version = 3):
    num_tokens = count_tokens_in_request(question)
    print("There are {} tokens in the question".format(num_tokens))
    if version == 3:
        priceperthousand = 0.0015
        if num_tokens > 4000:
            priceperthousand = 0.003
    elif version == 4:
        priceperthousand = 0.03
        if num_tokens > 8000:
            priceperthousand = 0.06
    
    costs = num_tokens * priceperthousand/1000

    # output cost
    # assume 5% of articles are accepted 
    if version == 3:
        # $ 0.002 per thousand output tokens
        costs += 0.05 * num_tokens * 0.002/1000
    elif version == 4:
        # 6 cents per thousand in 8k context
        costs += 0.05 * num_tokens * 0.06/1000

    # costs usually estimated too low:
    costs *= 1.3

    print("The request and answer costs around {}$".format(costs))

def count_tokens_in_request(text):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    #text = "This is an example sentence to count tokens."
    token_count = len(encoding.encode(text))
    
    print(f"The text contains {token_count} tokens and {len(text.split(' '))} words.")
    return token_count

if __name__ == "__main__":
    estimate_costs('Hat der Artikel mit dieser Überschrift etwas mit Politik oder Wirtschaft oder Wissenschaft zu tun? Antworte nur mit ja oder nein: Israel, Ukraine, Taiwan: Ich bin mir nicht sicher, ob die arabischen Staaten über das Vorgehen der Hamas sehr glücklich sind')#