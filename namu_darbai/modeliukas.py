# Load necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import plotly.express as px

# Load data
data_path = 'C:/Users/astap/downloads/Student_performance_data _.csv'
df = pd.read_csv(data_path)

# Data exploration
df.info()
df.hist(figsize=(20, 10), bins=7, color='lightblue')
plt.show()

# Identify categorical and numeric columns
categoric_columns = [col for col in df.columns if df[col].dtype == 'object']
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
if 'StudentID' in numeric_columns:
    numeric_columns.remove('StudentID')

# Convert 'GradeClass' to categorical if needed
if df['GradeClass'].dtype != 'object' and df['GradeClass'].nunique() > 5:
    print("Converting 'GradeClass' to categorical values")
    df['GradeClass'] = pd.qcut(df['GradeClass'], q=4, labels=False)

# Label encoding for categorical variables
label_encoder = LabelEncoder()
for col in categoric_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Standardize numerical features
scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Correlation matrix
plt.figure(figsize=(16, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title('Correlation Matrix of Features')
plt.show()

# Define features (X) and target (y)
X = df.drop(columns=['GradeClass', 'StudentID', 'Age', 'GPA'])  # Removed 'GPA'
y = df['GradeClass']

# Ensure target `y` is categorical for classification
if y.dtype != 'int' and y.dtype != 'category':
    y = LabelEncoder().fit_transform(y)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=42)

# Model training with various classifiers
classification_models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
}

model_names = []
accuracies = []
f1_scores = []
precisions = []
recalls = []

# Train and evaluate each model
for name, clf in classification_models.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)

    model_names.append(name)
    accuracies.append(accuracy)
    f1_scores.append(f1)
    precisions.append(precision)
    recalls.append(recall)

    print(f"{name} accuracy: {accuracy:.2f}, F1 score: {f1:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}")

# Identify the best model based on F1 Score
best_index = f1_scores.index(max(f1_scores))
best_model_name = model_names[best_index]
best_model = classification_models[best_model_name]
print(f"The best model is: {best_model_name} with an F1 Score of {f1_scores[best_index]:.2f}")

# Plot Feature Importance for the best model
plt.figure(figsize=(10, 6))
if hasattr(best_model, "feature_importances_"):
    importances = best_model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.title("Feature Importance")
    plt.bar(range(X.shape[1]), importances[indices], align="center")
    plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
    plt.xlim([-1, X.shape[1]])
    plt.show()
elif hasattr(best_model, "coef_"):
    importances = np.abs(best_model.coef_[0])
    indices = np.argsort(importances)[::-1]

    plt.title("Feature Importance")
    plt.bar(range(X.shape[1]), importances[indices], align="center")
    plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
    plt.xlim([-1, X.shape[1]])
    plt.show()
else:
    print(f"Feature importance not available for {best_model_name}.")

# Plot model metrics
df_models = pd.DataFrame({
    'Model': model_names,
    'Accuracy': accuracies,
    'F1 Score': f1_scores,
    'Precision': precisions,
    'Recall': recalls
})

# Plot model metrics
fig = px.bar(df_models, x='Model', y=['Accuracy', 'F1 Score', 'Precision', 'Recall'],
             title='Model Evaluation Metrics', barmode='group')
fig.show()

# Plot Learning Curves for each model separately
for name, clf in classification_models.items():
    plt.figure(figsize=(10, 6))

    train_sizes, train_scores, test_scores = learning_curve(clf, X_train, y_train, cv=5,
                                                            scoring='accuracy', n_jobs=-1,
                                                            train_sizes=np.linspace(0.2, 1.0, 10))

    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)

    plt.plot(train_sizes, train_scores_mean, label='Training Score')
    plt.plot(train_sizes, test_scores_mean, label='Cross-Validation Score', linestyle='--')

    plt.xlabel("Training Size")
    plt.ylabel("Score")
    plt.title(f"Learning Curve for {name}")
    plt.legend(loc="best")
    plt.grid()
    plt.show()

# Train the best model on full training data and evaluate
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

# Calculate and plot the confusion matrix
score = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted Values')
plt.ylabel('Actual Values')
plt.title(f'Confusion Matrix\nAccuracy Score: {score:.2f}')
plt.show()

# Feature Importance for Random Forest specifically
if best_model_name == "Random Forest":
    plt.figure(figsize=(10, 6))
    importances = best_model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.title("Feature Importance - Random Forest")
    plt.bar(range(X.shape[1]), importances[indices], align="center")
    plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
    plt.xlim([-1, X.shape[1]])
    plt.show()
