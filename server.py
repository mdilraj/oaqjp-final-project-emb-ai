"""
This is the server code for sentiment analysis
"""
from flask import Flask, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")
@app.route('/emotionDetector')
def sent_analyzer():
    """
    This API calls the sentiment analyzer and returns the label 
    and score to ui
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = sentiment_analyzer(text_to_analyze)
    if result['label']:
        res = (f"The given text has been identified as {result['label'][5:]}"
        f" with a score of {result['score']}")
    else:
        res = "Invalid input! Try again."
    return res

@app.route('/')
def render_index_page():
    """
    This method renders index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
