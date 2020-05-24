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

If you wish to add additional stop words, use the code below. Put additional words in a list format.

    New_stopwords = ["NEW_STOPWORD1", "NEW_STOPWORD2"]
    stop_words.extend(New_stopwords)

Next you need to add the text file. The second line tell the computer to read it. The last line splits a string (the text file) into a list.

    txt_file = open("text1.txt")
    txt_line = txt_file.read()
    txt_words = txt_line.split()
    
The next line of code adds a counter for the stop words.

    sw_found = 0 

Now add this:

    for check_word in txt_words:
    if not check_word.lower() in stop_words:
        appendFile = open('stopwords-removed.txt', 'a')
        appendFile.write(" "+check_word)
        appendFile.close()
    else:
        sw_found +=1
        print(check_word)

This for loop tells the computer to check each word in the text file and add all words not on the stopword list to a new text file called stopwords-removed.txt. 

Finally, the next two lines of code with print the number of stop words found and removed and print that it saved the new text file as the name given.

    print(sw_found, "stop words found and removed")
    print("Saved as 'stopwords-removed.txt'")


The full code is below:

    import nltk 
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    stop_words = nltk.corpus.stopwords.words('english')

    New_stopwords = ["NEW_STOPWORD1", "NEW_STOPWORD2"]
    stop_words.extend(New_stopwords)

    txt_file = open("text1.txt")
    txt_line = txt_file.read()
    txt_words = txt_line.split()

    sw_found = 0 

    for check_word in txt_words:
        if not check_word.lower() in stop_words:
            appendFile = open('stopwords-removed.txt', 'a')
            appendFile.write(" "+check_word)
            appendFile.close()
        else:
            sw_found +=1
            print(check_word)
    
    print(sw_found, "stop words found and removed")
    print("Saved as 'stopwords-removed.txt'")