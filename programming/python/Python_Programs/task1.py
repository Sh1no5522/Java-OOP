from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import pandas as pd

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print("Dataset shape:", X.shape)
print("Classes:", data.target_names)
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



print("LOGISTIC REGRESSION - Hyperparameter: C")

for c_value in [0.01, 0.1, 1]:   

    lr = LogisticRegression(
        C=c_value,
        max_iter=5000,
        random_state=42
    )

    lr.fit(X_train_scaled, y_train)
    y_pred = lr.predict(X_test_scaled)

    print("C =", c_value)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print("-" * 50)

print("=" * 60)


print("DECISION TREE - Hyperparameters: max_depth, min_samples_split")

for depth in [3, 5, 10]:                 
    for split in [2, 5]:                 

        dt = DecisionTreeClassifier(
            max_depth=depth,
            min_samples_split=split,
            random_state=42
        )

        dt.fit(X_train, y_train)
        y_pred = dt.predict(X_test)

        print("max_depth =", depth,
              "| min_samples_split =", split)

        print("Accuracy:", accuracy_score(y_test, y_pred))
        print(classification_report(y_test, y_pred))
        print("-" * 50)

print("=" * 60)