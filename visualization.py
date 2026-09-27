import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("results_analysis.csv")

subjects = [
    "Maths",
    "English",
    "Science",
    "Hindi",
    "History",
    "Geography"
]

# # =========================================================
# # 1. AVERAGE MARKS BY SUBJECT
# # =========================================================

# avg_marks = df[subjects].mean()

# sns.barplot(
#     x=avg_marks.index,
#     y=avg_marks.values
# )

# plt.xlabel("Subjects")
# plt.ylabel("Average Marks")
# plt.title("Average Marks by Subject")
# plt.xticks(rotation=45)
# plt.show()


# # =========================================================
# # 2. MAXIMUM MARKS BY SUBJECT
# # =========================================================

# max_marks = df[subjects].max()

# sns.barplot(
#     x=max_marks.index,
#     y=max_marks.values
# )

# plt.xlabel("Subjects")
# plt.ylabel("Maximum Marks")
# plt.title("Maximum Marks by Subject")
# plt.xticks(rotation=45)
# plt.show()


# # =========================================================
# # 3. PASS vs FAIL
# # =========================================================

# pass_count = (df["Results"] == 1).sum()
# fail_count = (df["Results"] == 0).sum()

# data = [pass_count, fail_count]
# labels = ["PASS", "FAIL"]

# plt.pie(
#     data,
#     labels=labels,
#     autopct="%1.1f%%",
#     explode=(0.02, 0)
# )

# plt.title("Pass vs Fail")
# plt.show()


# # =========================================================
# # 4. PERCENTAGE DISTRIBUTION
# # =========================================================

# sns.histplot(
#     data=df,
#     x="Percentage",
#     bins=10,
#     kde=True
# )

# plt.xlabel("Percentage")
# plt.ylabel("Number of Students")
# plt.title("Percentage Distribution")
# plt.show()


# # =========================================================
# # 5. SUBJECT-WISE MARK DISTRIBUTION
# # =========================================================

# sns.boxplot(
#     data=df[subjects]
# )

# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.title("Subject-wise Marks Distribution")
# plt.xticks(rotation=45)
# plt.show()


# =========================================================
# 6. CORRELATION HEATMAP
# =========================================================

correlation = df[subjects + ["Total", "Percentage"]].corr()

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()