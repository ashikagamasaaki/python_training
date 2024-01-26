# 51.
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
mean_column_A = np.mean(df['A'])
print(mean_column_A)

# 52.
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# 53.
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = [a['href'] for a in soup.find_all('a', href=True)]
print(links)

# 54.
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# 55.
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 56.
from nltk.tokenize import word_tokenize

text = "Natural language processing is a subfield of artificial intelligence."
tokens = word_tokenize(text)
print(tokens)

# 57.
import cv2

image = cv2.imread('example_image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 58.
from PIL import Image

image = Image.open('example_image.jpg')
resized_image = image.resize((300, 200))
resized_image.save('resized_image.jpg')

# 59. (Flaskアプリケーションをapp.pyに保存)
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_flask():
#     return 'Hello, Flask!'
#
# if __name__ == '__main__':
#     app.run()

# 60. (Djangoプロジェクトとアプリケーションを作成)
# django-admin startproject mysite
# cd mysite
# python manage.py startapp myapp
# (myapp/views.pyに以下のコードを追加)
# from django.http import HttpResponse
#
# def hello_django(request):
#     return HttpResponse('Hello, Django!')
# (mysite/urls.pyに以下のコードを追加)
# from django.urls import path
# from myapp.views import hello_django
#
# urlpatterns = [
#     path('', hello_django, name='hello_django'),
# ]
# (mysite/settings.pyでINSTALLED_APPSに'myapp'を追加)
# python manage.py runserver