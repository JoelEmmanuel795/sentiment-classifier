import csv

# List of punctuation characters to be removed from words
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word_str):
    """
    Removes punctuation characters from a given string.
    Args:
        word_str (str): The input string.
    Returns:
        str: The string without punctuation.
    """
    for punc_str in punctuation_chars:
        word_str = word_str.replace(punc_str, "").strip()
    return word_str

# Test strip_punctuation function
word = "hello;: !"
new2 = strip_punctuation(word)
print(new2)

# List of positive words to use
positive_words = []
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        # Skip comment lines or empty lines
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# Sample string to test positive word counting
ghost_str = "adequate, hateful, loving, fun, crazy, stupid, funny"

def get_pos(stri):
    """
    Counts the number of positive words in a given string.
    Args:
        stri (str): The input string.
    Returns:
        int: The count of positive words in the string.
    """
    stri_list = stri.lower().split()
    pos_values = 0
    for word in stri_list:
        if strip_punctuation(word) in positive_words:
            pos_values += 1
    return pos_values

# Test get_pos function
print(get_pos(ghost_str))

# List of negative words to use
negative_words = []
with open("assets/negative_words.txt") as neg_f:
    for lin in neg_f:
        # Skip comment lines or empty lines
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(stri):
    """
    Counts the number of negative words in a given string.
    Args:
        stri (str): The input string.
    Returns:
        int: The count of negative words in the string.
    """
    stri_list = stri.lower().split()
    neg_values = 0
    for word in stri_list:
        if strip_punctuation(word) in negative_words:
            neg_values += 1
    return neg_values

# Test get_neg function
print(get_neg(ghost_str))

# Open and extract data from project_twitter_data.csv
with open("assets/project_twitter_data.csv", "r") as twit_data:
    reader = csv.reader(twit_data)
    header = next(reader)  # Skip the header row

    # Initialize lists to store data from the file
    tweets, retweets, replies = [], [], []
    for row in reader:
        tweets.append(row[0])
        retweets.append(int(row[1]))
        replies.append(int(row[2]))

# Open and write processed data to resulting_data.csv
with open("resulting_data.csv", "w", newline='') as res_data:
    writer = csv.writer(res_data)

    # Write header row
    header = ["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"]
    writer.writerow(header)

    # Initialize lists for positive, negative, and net scores
    pos_scores, neg_scores, net_scores = [], [], []

    # Process each tweet and calculate scores
    for tweet in tweets:
        pos_score = get_pos(tweet)
        neg_score = get_neg(tweet)
        pos_scores.append(pos_score)
        neg_scores.append(neg_score)
        net_scores.append(pos_score - neg_score)

    # Write data rows to the CSV
    for row in range(len(tweets)):
        writer.writerow([
            retweets[row],
            replies[row],
            pos_scores[row],
            neg_scores[row],
            net_scores[row]
        ])
