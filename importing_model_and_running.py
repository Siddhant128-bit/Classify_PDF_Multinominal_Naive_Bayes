from classifier import get_input_from_pdf
from Dataset_Generator import get_topics
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

#Getting model and vectorizer thats stored for later use 
loaded_model=pickle.load(open('Classification.model','rb'))
vectorizer=pickle.load(open('vectorizer.pickle','rb'))

#using the vectorizer and model to predict without dataset
choice=int(input('Enter 1 to input pdf \n 2 to input text: '))
if choice==1:
    text=get_input_from_pdf()
else: 
    text=input('\n\nEnter your text: ')


text=vectorizer.transform([text])
topics=get_topics()
print(topics[loaded_model.predict(text)[0]])
