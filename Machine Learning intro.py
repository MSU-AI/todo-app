# Machine Learning intro.py

## 1. What is Machine Learning?
"""
Imagine you're teaching a child to recognize different types of fruits.
    You show them apples, bananas, oranges, and so on, and over time, 
    they start to understand the characteristics of each fruit - 
    color, shape, size, taste. Now, when you show them a fruit they've 
    never seen before, they can often guess what it is based on those characteristics.

Machine Learning (ML) works in a similar way. 
    It's a branch of artificial intelligence (AI) that focuses on the use of 
    data and algorithms to imitate the way humans learn.
    In essence, ML algorithms use a set of data samples to make predictions 
    or decisions without being explicitly programmed to do so.
    
    For example, 
    it can be trained to recognize the characteristics of different types of fruits.
    
    In our case trained to predict and suggest tasks based on the user's schedule 
    and predicted time to complete that task and the due date of the task.
"""

## 2. Introduction to Scikit-learn

"""
Now that we understand what machine learning is, 
    let's talk about one of its libraries in Python - Scikit-learn.

Scikit-learn is like a toolbox full of machine learning tools. 

You'd use Scikit-learn for tasks like classification, regression, clustering.
    It provides various tools for model fitting, data preprocessing, model selection and 
    evaluation, making it a library for both supervised and unsupervised machine learning.

Scikit-learn is built on top of NumPy, SciPy, and Matplotlib,
"""

## 3. Basic Code Example Using Scikit-learn

"""
Let's look at an example of how Scikit-learn can be used. 
    We'll use the Linear Regression model as an example:
    Run the code below to see the output.
"""

# Import the necessary libraries
from sklearn import linear_model
# pip install -U scikit-learn
import matplotlib.pyplot as plt
# pip install -U matplotlib

# Create a Linear Regression object
# Basically, we're creating a Linear Regression model: https://youtu.be/nk2CQITm_eo?si=uciJQKH6HVuyshdt
# Linear regression is a statistical method used to model and analyze the relationship 
# between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.
reg = linear_model.LinearRegression()

# Define the data points
# Basically, we're creating a dataset
# Features are the independent variables
# Target variable is the dependent variable
x = [[i, i] for i in range(10)]  # Features
y = [i for i in range(10)]  # Target variable

# Fit the model to the data
# Basically, we're training the model
reg.fit(x, y)

# Generate additional data points
# Basically, we're creating more data points
x_new = [[i, i+1] for i in range(10)]  # Features
y_new = [i+1 for i in range(10)]  # Target variable

# Generate additional data points
# Basically, we're creating even more data points
x_newer = [[i, i-1] for i in range(10)]  # Features
y_newer = [i-1 for i in range(10)]  # Target variable


# Plot the original data points
# We're plotting the original data points
plt.scatter([i[0] for i in x], y, color='black')

# Plot the additional data points
# We're plotting the additional data points
plt.scatter([i[0] for i in x_new], y_new, color='red')
plt.scatter([i[0] for i in x_newer], y_newer, color='green')

# Plot the regression line
# We're plotting the regression line
plt.plot([i[0] for i in x], reg.predict(x), color='blue', linewidth=3)

# Add labels and title
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('#3. Linear Regression')

# Show the plot
plt.show()

"""
In this code snippet, we first import the necessary library. 
    We then create an object of the Linear Regression model. 
    We fit this model on some data (x,y). 
    Finally, we print out the coefficients of the fitted model.
"""

## 4. Conclusion

"""
Helpful Sources:
(1) What is Machine Learning? | YouTube. https://www.youtube.com/watch?v=ukzFI9rgwfU&ab_channel=Simplilearn
(2) What is Machine Learning? | IBM. https://www.ibm.com/topics/machine-learning.
(3) An introduction to machine learning with scikit-learn. https://scikit-learn.org/stable/tutorial/basic/tutorial.html.
(4) Introduction to Scikit-Learn (sklearn) in Python • datagy. https://datagy.io/python-scikit-learn-introduction/.
(5) Introduction to Scikit learn in 6 minutes - YouTube. https://www.youtube.com/watch?v=oFa8NvTLkKE&ab_channel=TimesPro.
(6) Python SciKit Learn Tutorial | DigitalOcean. https://www.digitalocean.com/community/tutorials/python-scikit-learn-tutorial.
(7) scikit-learn Tutorials — scikit-learn 1.3.1 documentation. https://scikit-learn.org/stable/tutorial/index.html.
(8) INTRODUCTION TO SCIKIT-LEARN - GitHub Pages. https://tdmdal.github.io/sklearn-workshop/introtosklearn.pdf.
(9) How To Build a Machine Learning Classifier in Python with Scikit-learn. https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn.
(10) What Is Machine Learning? Definition, Types, and Examples. https://www.coursera.org/articles/what-is-machine-learning.
(11) What is machine learning? | Microsoft Azure. https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-machine-learning-platform/.
(12) Machine learning - Wikipedia. https://en.wikipedia.org/wiki/Machine_learning.
"""

# 5. Bonus: Examlpe of a Real World Example using Clustering (K-Means Clustering)

"""
This code demonstrates how machine learning can be used to group data into clusters. 
    Specifically, it takes a dataset of customer transactions and groups the customers 
    into clusters based on their transaction history. This can be useful for businesses 
    that want to identify groups of customers with similar purchasing behavior and tailor 
    their marketing strategies accordingly. Note that this is just an example and not necessarily 
    the best or only way to solve this problem.
    Run the code below to see the output.
"""

# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Generate customer transaction data
# This would typically be read from a database or file like a CSV
data = {
    'Customer ID': list(range(1, 101)),
    'Amount Spent': np.random.randint(0, 100, size=100),
    'Items Purchased': np.random.randint(1, 20, size=100)
}

# Create a DataFrame
# Making a table
# Dataframe: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
df = pd.DataFrame(data)

# Extract the features
# Features are the independent variables
# Target variable is the dependent variable
X = df.iloc[:, 1:].values

# Scale the features
# Making the features have the same scale
scaler = StandardScaler()
# StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
X = scaler.fit_transform(X)

# Create a KMeans object
# KMeans model: https://youtu.be/4b5d3muPQmA?si=8f2f9f9f9f9f9f9f
kmeans = KMeans(n_clusters=4)

# Fit the model using the customer transaction data
kmeans.fit(X)

# Add the cluster labels to the original data
df['Cluster'] = kmeans.labels_

# Calculate the correlation within each cluster

# Group the data by cluster and calculate the correlation between Amount Spent and Items Purchased 
# Ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
correlations = df.groupby('Cluster')['Amount Spent', 'Items Purchased'].corr().iloc[0::2, -1]
avg_items = df.groupby('Cluster')['Items Purchased'].mean()
avg_spent = df.groupby('Cluster')['Amount Spent'].mean()

# Convert the indices to a flat index
# Flat Index: https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_flat_index.html
correlations.index = correlations.index.to_flat_index()
avg_items.index = avg_items.index.to_flat_index()
avg_spent.index = avg_spent.index.to_flat_index()

# Combine the correlations, average items purchased, and average amount spent into a single table
# Concat: https://pandas.pydata.org/docs/reference/api/pandas.concat.html
table = pd.concat([correlations, avg_items, avg_spent], axis=1)
table.columns = ['Correlation', 'Avg Items Purchased', 'Avg Amount Spent']

# Print the table
print(table)

# Plot the clusters
plt.scatter(df['Amount Spent'], df['Items Purchased'], c=df['Cluster'], cmap='viridis')
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='*')
# Annotate: https://matplotlib.org/stable/users/explain/text/annotations.html#plotting-guide-annotation
for i, centroid in enumerate(centroids):
    plt.annotate(f"   {i}", (centroid[0], centroid[1]), fontsize=12, fontweight='bold', color='red')
plt.xlabel('Amount Spent')
plt.ylabel('Items Purchased')
plt.title('#5. Customer Segmentation using K-means clustering')
plt.show()