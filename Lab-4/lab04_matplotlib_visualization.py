

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csv_path = Path(__file__).resolve().parent / "train.csv"

# Problem 1: Load the dataset and inspect it
df = pd.read_csv(csv_path)

print("First five rows:")
print(df.head())
print("\nShape:", df.shape)
print("\nData types:")
print(df.dtypes)

numerical_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(exclude="number").columns.tolist()
print("\nNumerical attributes  :", numerical_cols)
print("Categorical attributes:", categorical_cols)
print(
    "\nUseful for visualization -> Numerical: Age, Fare | "
    "Categorical: Sex, Pclass, Survived, Embarked"
)

# Problem 2: Line plot - average fare by passenger class

avg_fare = df.groupby("Pclass")["Fare"].mean()

plt.figure(figsize=(7, 5))
plt.plot(avg_fare.index, avg_fare.values, marker="o", color="tab:blue")
plt.title("Average Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")
plt.xticks([1, 2, 3])
plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("problem2_line_plot.png", dpi=150)
plt.show()
# Interpretation: Fare drops sharply from 1st to 3rd class.


# Problem 3: Scatter plot - Age vs Fare

plt.figure(figsize=(7, 5))
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="tab:green")
plt.title("Passenger Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.savefig("problem3_scatter_plot.png", dpi=150)
plt.show()
# Interpretation: No strong relationship between age and fare; a few
# passengers paid very high fares (outliers).

# Problem 4: Bar chart - male vs female passengers

gender_counts = df["Sex"].value_counts()

plt.figure(figsize=(6, 5))
plt.bar(gender_counts.index, gender_counts.values, color=["tab:blue", "tab:pink"])
plt.title("Number of Male and Female Passengers")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.savefig("problem4_bar_chart.png", dpi=150)
plt.show()
# Interpretation: There were more male passengers than female passengers.

# Problem 5: Histogram - distribution of age

plt.figure(figsize=(7, 5))
plt.hist(df["Age"].dropna(), bins=20, color="tab:orange", edgecolor="black")
plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("problem5_histogram.png", dpi=150)
plt.show()
# Interpretation: Most passengers were aged roughly 20-40;
# there is also a small group of young children.


# Problem 6: Pie chart - survived vs did not survive

survival_counts = df["Survived"].value_counts().sort_index()  # 0, 1

plt.figure(figsize=(6, 6))
plt.pie(
    survival_counts.values,
    labels=["Did Not Survive", "Survived"],
    autopct="%1.1f%%",
    colors=["tab:red", "tab:green"],
    startangle=90,
)
plt.title("Survival Proportion of Passengers")
plt.savefig("problem6_pie_chart.png", dpi=150)
plt.show()
# Interpretation: Majority of passengers (~62%) did not survive.


# Problem 7: Two subplots - Age histogram + Pclass bar chart

class_counts = df["Pclass"].value_counts().sort_index()

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].hist(df["Age"].dropna(), bins=20, color="tab:orange", edgecolor="black")
ax[0].set_title("Distribution of Passenger Ages")
ax[0].set_xlabel("Age")
ax[0].set_ylabel("Frequency")

ax[1].bar(class_counts.index.astype(str), class_counts.values, color="tab:purple")
ax[1].set_title("Passengers by Class")
ax[1].set_xlabel("Passenger Class")
ax[1].set_ylabel("Number of Passengers")

plt.tight_layout()
plt.savefig("problem7_two_subplots.png", dpi=150)
plt.show()
# Interpretation: 3rd class has the most passengers.

# Problem 8: Three subplots - gender bar, fare histogram, survival pie

fig, ax = plt.subplots(1, 3, figsize=(16, 5))

# 1) Bar chart - passengers by gender
ax[0].bar(gender_counts.index, gender_counts.values, color=["tab:blue", "tab:pink"])
ax[0].set_title("Passengers by Gender")
ax[0].set_xlabel("Gender")
ax[0].set_ylabel("Number of Passengers")

# 2) Histogram - fare distribution
ax[1].hist(df["Fare"], bins=30, color="tab:cyan", edgecolor="black")
ax[1].set_title("Distribution of Fares")
ax[1].set_xlabel("Fare")
ax[1].set_ylabel("Frequency")

# 3) Pie chart - survival proportion
ax[2].pie(
    survival_counts.values,
    labels=["Did Not Survive", "Survived"],
    autopct="%1.1f%%",
    colors=["tab:red", "tab:green"],
    startangle=90,
)
ax[2].set_title("Survival Proportion")

fig.suptitle("Titanic Dataset Overview", fontsize=14)
plt.tight_layout()
plt.savefig("problem8_three_subplots.png", dpi=150)
plt.show()
# Interpretation: Fare is right-skewed (most paid low fares); more men
# than women; most passengers did not survive.
