# Sentiment Classifier for Twitter Data

This project processes Twitter data to classify tweets based on sentiment. Using Python, it calculates **positive**, **negative**, and **net scores** for each tweet based on predefined word lists. The script then outputs a CSV file with these scores, along with the number of retweets and replies for each tweet. 

## Key Features

### Data Processing:
- Reads Twitter data from `project_twitter_data.csv`.
- Cleans tweets by removing punctuation for accurate word matching.

### Sentiment Analysis:
- Uses `positive_words.txt` and `negative_words.txt` to identify sentiment scores for tweets.
- Outputs sentiment scores as:
  - **Positive Score**: Count of positive words.
  - **Negative Score**: Count of negative words.
  - **Net Score**: Positive score minus negative score.

### Result Export:
- Outputs processed data to `resulting_data.csv`, including:
  - Number of retweets.
  - Number of replies.
  - Positive, negative, and net sentiment scores.

## Input

### `project_twitter_data.csv`:
- A CSV file containing columns for tweets, number of retweets, and replies.

### Word Lists:
- `positive_words.txt`: A list of predefined positive words.
- `negative_words.txt`: A list of predefined negative words.

## Output

### `resulting_data.csv`:
- A CSV file containing:
  - Number of retweets.
  - Number of replies.
  - Positive score.
  - Negative score.
  - Net score.

## How to Use

1. Clone the repository and place the required files (`project_twitter_data.csv`, `positive_words.txt`, and `negative_words.txt`) in the `assets` directory.
2. Run the script to process the data:
   ```bash
   python sentiment_classifier.py
   ```
3. View the results in the `resulting_data.csv` file.
