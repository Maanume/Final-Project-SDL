import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 #stop_words = set(stopwords.words('english'))
stop_words = nltk.corpus.stopwords.words('english')
#stopwords.append('employment')
New_stopwords = ["employment", "post-war"]
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
