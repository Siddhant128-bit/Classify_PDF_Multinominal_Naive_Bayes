from classifier import get_input_from_pdf
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

#Getting model and vectorizer thats stored for later use 
loaded_model=pickle.load(open('Classification.model','rb'))
vectorizer=pickle.load(open('vectorizer.pickle','rb'))

#using the vectorizer and model to predict without dataset
text=get_input_from_pdf()
text=vectorizer.transform([text])
print(loaded_model.predict(text))
