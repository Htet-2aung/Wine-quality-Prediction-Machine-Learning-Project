# -*- coding: utf-8 -*-
"""ML-Midterm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o01aFYNEYW41EPyx_FDCP5yAIhVWxIsN

# Question 1 : Model Training for both regression and classification

**Dataset : Wine Quality**

**URL : https://archive.ics.uci.edu/dataset/186/wine+quality**

**Method for classification**

*   Decision Tree
*   Random Forests
*   KNN
*   Naive Bayes
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('winequality-red.csv')
df.head()

df.shape

sns.heatmap(df.isnull())

sns.heatmap(df.corr(), vmin = 0, vmax = 0.5)

df = df.drop_duplicates()
df.shape

num_columns = len(df.columns)
cols = 3  # Number of columns for the subplots
rows = (num_columns + cols - 1) // cols  # Calculate number of rows needed

plt.figure(figsize=(15, 5 * rows))  # Adjust the height based on the number of rows

for i, column in enumerate(df.columns):
    plt.subplot(rows, cols, i + 1)  # Create a subplot for each column
    sns.histplot(data=df, x=column, kde=True, bins=30, color='#DDA0DD')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

plt.figure(figsize=(18, 6 * rows))  # Here we increase the figure height and width

for i, column in enumerate(df.columns[:-1]):
    plt.subplot(rows, cols, i + 1)
    sns.scatterplot(data=df, x=column, y='quality', hue='quality', size='quality', sizes=(50, 300), alpha=0.7, legend=False)
    plt.title(f'Scatter Plot of {column} vs Quality')
    plt.xlabel(column)
    plt.ylabel('Quality')
    plt.grid(True)

plt.tight_layout(pad=3.0)  # Adjust layout to prevent overlap and add padding
plt.show()

"""**Do sweeter wines receive better ratings?**"""

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='residual sugar', y='quality', hue='quality',
                palette='viridis', size='quality', sizes=(50, 300), alpha=0.7, legend='full')

plt.title('Scatter Plot of Residual Sugar vs Quality', fontsize=16)
plt.xlabel('Residual Sugar', fontsize=14)
plt.ylabel('Quality', fontsize=14)

plt.grid(True)

# Show the plot
plt.legend(title='Quality', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
plt.show()

mean_sugar = df['residual sugar'].mean()
meanofhighsugar = df[df['residual sugar'] > mean_sugar].quality.mean()
meanoflowsugar = df[df['residual sugar'] < mean_sugar].quality.mean()

print("Average quality of wines with low sugar", meanoflowsugar)
print("Average quality of wines with high sugar", meanofhighsugar)

plt.bar(x = ['High Sugar', 'Low Sugar'], height = [meanofhighsugar, meanoflowsugar])
plt.ylim((5,6))

mean_acidity = df['fixed acidity'].mean()
meanofhighalc = df[df['fixed acidity'] > mean_acidity].quality.mean()
meanoflowalc = df[df['fixed acidity'] < mean_acidity].quality.mean()

print("Average quality of wines with low acidity", meanoflowalc)
print("Average quality of wines with high acidity", meanofhighalc)

plt.bar(x = ['High Acidity', 'Low Acidity'], height = [meanofhighalc, meanoflowalc])
plt.ylim((5, 6))
plt.show()

"""Which wines are produced more? (according to quality)

"""

df['quality'].value_counts().sort_index().plot(kind='bar', xlabel='Quality', ylabel='quantity')

#Converting data to binary classification

df["quality"] = np.where(df["quality"] >= 7, 1, 0)
df.quality.value_counts()

#Model Creation and Training

models = ['KNN Classifier', 'Decision Tree', 'Random forest', 'Naive Bayes']
score =[]

df.head()

"""**Splitting Data**"""

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(df.drop('quality', axis = 1), df['quality'], test_size = 0.2, random_state=42)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

"""**Scaling data**"""

Y_train.value_counts()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

"""

> KNN Classification

"""

from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors = 13)
knn_model.fit(scaled_X_train, Y_train)

knn_pred = knn_model.predict(scaled_X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print(classification_report(Y_test, knn_pred))
#print(confusion_matrix(Y_test, knn_pred))
print(accuracy_score(Y_test, knn_pred))

score.append(accuracy_score(Y_test, knn_pred))
print(score)
#print(np.mean(score))

"""

> **Decision Tree**

"""

#Decision Tree Classifier Model Training

from sklearn.tree import DecisionTreeClassifier
model_dtree = DecisionTreeClassifier()
model_dtree.fit(scaled_X_train, Y_train)
dtree_pred = model_dtree.predict(scaled_X_test)
print(classification_report(Y_test, dtree_pred))


score.append(accuracy_score(Y_test, dtree_pred))
print(score)
#print(np.mean(score))

#Feature Importance of Decision Tree Classifier Model

plt.figure(figsize = (10, 5))
plt.bar(df.columns[:-1], model_dtree.feature_importances_)
plt.title('Feature Importance')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(rotation = 45)
plt.show()

"""

> **Random Forest**

"""

#Model training of Random Forest Classifier Method

from sklearn.ensemble import RandomForestClassifier

random_forest_classifier = RandomForestClassifier(max_features = 3, n_estimators = 169, bootstrap = True)
random_forest_classifier.fit(scaled_X_train, Y_train)
rfc_pred = random_forest_classifier.predict(scaled_X_test)
print(classification_report(Y_test, rfc_pred))

score.append(accuracy_score(Y_test, rfc_pred))
print(score)
#print(np.mean(score))

from sklearn.naive_bayes import GaussianNB

# Naive Bayes Classification
naive_bayes_model = GaussianNB()
naive_bayes_model.fit(scaled_X_train, Y_train)
nb_pred = naive_bayes_model.predict(scaled_X_test)

print(classification_report(Y_test, nb_pred))
#print(confusion_matrix(Y_test, nb_pred))
print(accuracy_score(Y_test, nb_pred))

score.append(accuracy_score(Y_test, nb_pred))
print(score)

print(score)
plt.figure(figsize=(10, 6))
plt.bar(models, score, color='skyblue')

# Add labels and title
plt.xlabel("Models")
plt.ylabel("Accuracy Score")
plt.title("Model Accuracy")

# Display the plot
plt.ylim(0, 1)  # Set y-axis limits for better visualization
plt.show()

highest_score_index = np.argmax(score)  # Here we get the index of the highest score
highest_score_model = models[highest_score_index]  # Get the corresponding model name from the models dictionary
highest_score_value = score[highest_score_index]  # Get the highest score value

# Print the highest score model and its score
print(f"The model with the highest score is: {highest_score_model} with an accuracy of {highest_score_value:.2f}")

"""**Regression Model**

For regression model for this dataset we use the following models

*   Linear Regression
*   Lasso Regression
*   Decision Tree Regression
*   Random Forest Regression


"""

score_reg = []
models_reg = ['Linear Regression', 'Lasso Regression', 'Decision Tree Regression', 'Random Forest Regression']

"""

> **Linear Regression**

"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

linear_regression_model = LinearRegression()

linear_regression_model.fit(X_train, Y_train)

linear_regression_predictions = linear_regression_model.predict(X_test)

# Evaluation of the model
mse = mean_squared_error(Y_test, linear_regression_predictions)
r2 = r2_score(Y_test, linear_regression_predictions)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

score_reg.append(r2)

"""

> **Lasso Regression**

"""

from sklearn.linear_model import Lasso

lasso_regression_model = Lasso(alpha=0.1)  # You can adjust the alpha parameter

lasso_regression_model.fit(X_train, Y_train)

lasso_regression_predictions = lasso_regression_model.predict(X_test)


mse = mean_squared_error(Y_test, lasso_regression_predictions)
r2 = r2_score(Y_test, lasso_regression_predictions)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

score_reg.append(r2)

"""

> **Decision Tree Regression**

"""

from sklearn.tree import DecisionTreeRegressor

# Decision Tree Regression Model Training
decision_tree_regression_model = DecisionTreeRegressor()
decision_tree_regression_model.fit(X_train, Y_train)
decision_tree_regression_predictions = decision_tree_regression_model.predict(X_test)

# Evaluation of the decison tree regression model
mse = mean_squared_error(Y_test, decision_tree_regression_predictions)
r2 = r2_score(Y_test, decision_tree_regression_predictions)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

score_reg.append(r2)

"""

> **Random Forest Regression**

"""

from sklearn.ensemble import RandomForestRegressor

# Random Forest Regression Model Training
random_forest_regression_model = RandomForestRegressor()
random_forest_regression_model.fit(X_train, Y_train)
random_forest_regression_predictions = random_forest_regression_model.predict(X_test)

# Evaluation of the random forest regression model
mse = mean_squared_error(Y_test, random_forest_regression_predictions)
r2 = r2_score(Y_test, random_forest_regression_predictions)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

score_reg.append(r2)

"""**Comparison of each regression model**"""

plt.figure(figsize=(10, 6))
plt.bar(models_reg, score_reg, color='skyblue')

# Add labels and title
plt.xlabel("Regression Models")
plt.ylabel("R-squared Score")
plt.title("Regression Model Performance")

# Display the plot
plt.ylim(0, 1)  # Set y-axis limits for better visualization
plt.show()

highest_score_index_reg = np.argmax(score_reg)  # Here we get the index of the highest score
highest_score_model_reg = models_reg[highest_score_index_reg]  # Get the corresponding model name from the models dictionary
highest_score_value_reg = score_reg[highest_score_index_reg]  # Get the highest score value

# Print the highest score model and its score
print(f"The regression model with the highest R-squared is: {highest_score_model_reg} with an R-squared of {highest_score_value_reg:.2f}")

"""# Question 2 : Overfitting and Solutions"""

# Decision Tree with potential overfitting
model_dtree_overfit = DecisionTreeClassifier()
model_dtree_overfit.fit(X_train, Y_train)
dtree_pred_overfit = model_dtree_overfit.predict(X_test)
print("Decision Tree (Potential Overfitting):")
print(classification_report(Y_test, dtree_pred_overfit))
print("Accuracy:", accuracy_score(Y_test, dtree_pred_overfit))

# Decision Tree with Pruning to prevent overfitting
model_dtree_pruned = DecisionTreeClassifier(max_depth=5, min_samples_leaf=5)
model_dtree_pruned.fit(X_train, Y_train)
dtree_pred_pruned = model_dtree_pruned.predict(X_test)
print("\nDecision Tree (Pruned):")
print(classification_report(Y_test, dtree_pred_pruned))
print("Accuracy:", accuracy_score(Y_test, dtree_pred_pruned))

# Random Forest with potential overfitting
random_forest_classifier_overfit = RandomForestClassifier(n_estimators=1000)
random_forest_classifier_overfit.fit(X_train, Y_train)
rfc_pred_overfit = random_forest_classifier_overfit.predict(X_test)
print("\nRandom Forest (Potential Overfitting):")
print(classification_report(Y_test, rfc_pred_overfit))
print("Accuracy:", accuracy_score(Y_test, rfc_pred_overfit))

# Random Forest with Regularization to prevent overfitting
random_forest_classifier_regularized = RandomForestClassifier(n_estimators=100, max_features=3, max_depth=5)
random_forest_classifier_regularized.fit(X_train, Y_train)
rfc_pred_regularized = random_forest_classifier_regularized.predict(X_test)
print("\nRandom Forest (Regularized):")
print(classification_report(Y_test, rfc_pred_regularized))
print("Accuracy:", accuracy_score(Y_test, rfc_pred_regularized))

from sklearn.metrics import ConfusionMatrixDisplay
data = pd.read_csv("winequality-red.csv")
data.head()

# Feature selection (assuming 'quality' is the target variable)
X = data.drop('quality', axis=1)
Y = data['quality']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Decision Tree with potential overfitting
model_dtree_overfit = DecisionTreeClassifier()
model_dtree_overfit.fit(X_train, Y_train)
dtree_pred_overfit = model_dtree_overfit.predict(X_test)

# Decision Tree with Pruning
model_dtree_pruned = DecisionTreeClassifier(max_depth=5, min_samples_leaf=5)
model_dtree_pruned.fit(X_train, Y_train)
dtree_pred_pruned = model_dtree_pruned.predict(X_test)

# Random Forest with potential overfitting
random_forest_classifier_overfit = RandomForestClassifier(n_estimators=1000)
random_forest_classifier_overfit.fit(X_train, Y_train)
rfc_pred_overfit = random_forest_classifier_overfit.predict(X_test)

# Random Forest with Regularization
random_forest_classifier_regularized = RandomForestClassifier(n_estimators=100, max_features=3, max_depth=5)
random_forest_classifier_regularized.fit(X_train, Y_train)
rfc_pred_regularized = random_forest_classifier_regularized.predict(X_test)

# Visualization of results
models = ['DTree Overfit', 'DTree Pruned', 'RFC Overfit', 'RFC Regularized']
accuracies = [
    accuracy_score(Y_test, dtree_pred_overfit),
    accuracy_score(Y_test, dtree_pred_pruned),
    accuracy_score(Y_test, rfc_pred_overfit),
    accuracy_score(Y_test, rfc_pred_regularized)
]

# Bar chart for accuracy comparison
plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, color=['red', 'green', 'orange', 'blue'])
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison on Wine Quality Dataset')
plt.ylim(0, 1)  # Set y-axis limits for better visualization
plt.show()

# Confusion Matrix Visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes = axes.flatten()

# Decision Tree Overfit
cm_overfit = confusion_matrix(Y_test, dtree_pred_overfit)
ConfusionMatrixDisplay(cm_overfit).plot(ax=axes[0], cmap='Blues')
axes[0].set_title('Decision Tree (Potential Overfitting)')

# Decision Tree Pruned
cm_pruned = confusion_matrix(Y_test, dtree_pred_pruned)
ConfusionMatrixDisplay(cm_pruned).plot(ax=axes[1], cmap='Greens')
axes[1].set_title('Decision Tree (Pruned)')

# Random Forest Overfit
cm_rfc_overfit = confusion_matrix(Y_test, rfc_pred_overfit)
ConfusionMatrixDisplay(cm_rfc_overfit).plot(ax=axes[2], cmap='Oranges')
axes[2].set_title('Random Forest (Potential Overfitting)')

# Random Forest Regularized
cm_rfc_regularized = confusion_matrix(Y_test, rfc_pred_regularized)
ConfusionMatrixDisplay(cm_rfc_regularized).plot(ax=axes[3], cmap='Purples')
axes[3].set_title('Random Forest (Regularized)')

plt.tight_layout()
plt.show()

"""# Question 3 : Feature selection and correlation analysis"""

# Correlation analysis
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Wine Quality Features')
plt.show()

# Identify features highly correlated with 'quality'
correlation_with_quality = correlation_matrix['quality'].sort_values(ascending=False)
print("Correlation with Quality:")
print(correlation_with_quality)

# Select features with a correlation above a certain threshold (e.g., 0.2)
selected_features = correlation_with_quality[abs(correlation_with_quality) > 0.2].index.tolist()
print("\nSelected Features:")
print(selected_features)

# Create a new dataset with only the selected features
df_selected = df[selected_features]

# Split the data into training and testing sets using the selected features
X_train_selected, X_test_selected, Y_train_selected, Y_test_selected = train_test_split(
    df_selected.drop('quality', axis=1), df_selected['quality'], test_size=0.2, random_state=42
)

# Training models using the selected features (example with Random Forest)
random_forest_classifier_selected = RandomForestClassifier()
random_forest_classifier_selected.fit(X_train_selected, Y_train_selected)
rfc_pred_selected = random_forest_classifier_selected.predict(X_test_selected)
print("\nRandom Forest with Selected Features:")
print(classification_report(Y_test_selected, rfc_pred_selected))
print("Accuracy:", accuracy_score(Y_test_selected, rfc_pred_selected))

# Training and evaluating Decision Tree with selected features
decision_tree_classifier = DecisionTreeClassifier()
decision_tree_classifier.fit(X_train_selected, Y_train_selected)
dt_pred_selected = decision_tree_classifier.predict(X_test_selected)

print("\nDecision Tree with Selected Features:")
print(classification_report(Y_test_selected, dt_pred_selected))
print("Accuracy:", accuracy_score(Y_test_selected, dt_pred_selected))

# Training and evaluating Linear Regression (for regression task)
linear_regression_model = LinearRegression()
linear_regression_model.fit(X_train_selected, Y_train_selected)
lin_pred_selected = linear_regression_model.predict(X_test_selected)

print("\nLinear Regression with Selected Features:")
print("Mean Squared Error:", mean_squared_error(Y_test_selected, lin_pred_selected))
print("R-squared:", r2_score(Y_test_selected, lin_pred_selected))