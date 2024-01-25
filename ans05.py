# 41.
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
print(df)

# 42.
selected_column = df['Age']
new_df = pd.DataFrame({'Age': selected_column})
print(new_df)

# 43.
df_no_missing = df.dropna()
print(df_no_missing)

# 44.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 15, 20]
plt.scatter(x, y)
plt.show()

# 45.
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.show()

# 46.
import seaborn as sns

sns.boxplot(x='Age', data=df)
plt.show()

# 47.
import requests

url = 'https://www.example.com'
response = requests.get(url)
print(response.text)

# 48.
from bs4 import BeautifulSoup

html = '<html><body><p>Hello, <b>world</b>!</p></body></html>'
soup = BeautifulSoup(html, 'html.parser')
bold_text = soup.find('b').text
print(bold_text)

# 49.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# 50.
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(4,)),
    layers.Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()