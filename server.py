''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, request, jsonify, render_template, url_for, redirect

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app

app = Flask('Sentiment Analyzer')


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    analysis = sentiment_analyzer(text_to_analyse)
    return analysis


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
'''

app.run(debug = True, host="0.0.0.0", port=5000)

