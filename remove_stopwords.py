import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = nltk.corpus.stopwords.words('english')
# if desired, add more words for the stopword list.
New_stopwords = ["hon.", "member", "mr."]
stop_words.extend(New_stopwords)

# below add the text file you would like to run through the program.
txt_file = open("text1.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()

sw_found = 0 

# below create name for file containing words not removed with stop words.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        appendFile = open('stopwords-removed.txt', 'a')
        appendFile.write(" "+check_word)
        appendFile.close()
    else:
        sw_found +=1
        print(check_word)
print(sw_found, "stop words found and removed")
# add name of file from above in this line
print("Saved as 'stopwords-removed.txt'")
