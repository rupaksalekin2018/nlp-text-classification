# nlp text classification 
 A simple NLP classifier 
To run everything smoothly in Mac OS, follow the steps:
1. pip install virtualenv
2. virtualenv myenv -p python3.8
3. source myenv/bin/activate 
4. export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
5. (install pip if necessary)
6. pip install bltk

***** Important *****

Scraped Data File With Label: youtube_comments_labeled_multilingual_with_banglish.csv
Final Code For Scraped Data: scraped_data_final.ipynb
5. (install pip if pip is not installed)
6. pip install bltk

**** What is done in the project ****

1. Data is collected from YouTube comment
2. Manually label is added (Here 0 is negative, 1 is positive & 2 is a neutral label in the youtube CSV file)
3. Tokenizing from each sentence, Truncating punctuation, Truncating StopWords & Collecting the label.
4. xs for X and ys for label Y
5. Data Split for train and test
6. Training the predictive models
