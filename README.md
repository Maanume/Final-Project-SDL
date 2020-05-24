# My Software Design Lab Final Project
My final project removes words from a text file using the stopword list from the NLTK package in Python. This project also shows you how to add additional words to the stopword list in Python. 

## Installation
If you do not have anaconda or nltk installed on your computer follow the steps below.
For anaconda go to this link and click download. 

For nltk enter this line in Bash:

    pip install --user -U nltk

Test installation by typing:
    
    python

then
    
    import nltk

## Usage
To run the project, start with this line in Bash:

    import nltk 
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

The first two lines of code imports in the nltk library and then imports the stopwords folder. The next line breaks down the text file into words.

Next you need to define the stopword list:

    stop_words = nltk.corpus.stopwords.words('english')


