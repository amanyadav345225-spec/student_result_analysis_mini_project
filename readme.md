
# Student Result Analysis 📊

A Python-based project to analyze student academic performance using data processing, statistical analysis, data visualization, and machine learning classification.

The project explores subject-wise marks, overall performance, pass/fail distribution, and uses Logistic Regression and K-Nearest Neighbors (KNN) to classify students as Pass or Fail.

## 📌 Project Objectives

- Calculate total marks and percentage.
- Analyze pass/fail status.
- Identify average and maximum marks by subject.
- Explore subject-wise performance and marks distribution.
- Visualize percentage distribution and correlations.
- Build and evaluate machine learning classification models.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab
- Git & GitHub

## 📊 Data Analysis and Visualization

The project includes the following analyses:

- Average marks by subject
- Maximum marks by subject
- Pass/fail distribution
- Percentage distribution
- Subject-wise marks distribution using box plots
- Correlation analysis of numerical columns

Visualizations are saved in the `plots/` directory.

## 🤖 Machine Learning Models

Two classification algorithms are implemented to predict student pass/fail status using six subject marks.

### Models Implemented

1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**

### Input Features

- Hindi
- English
- Science
- Maths
- History
- Geography

### Target Variable

`Pass_Fail`

- `0` — Fail
- `1` — Pass

### Model Evaluation

The models are evaluated using a train-test split, accuracy score, and confusion matrix.

| Model | Test Accuracy |
|---|---:|
| Logistic Regression | 100% |
| KNN (k = 5) | 99% |

*Note: These accuracy scores are based on the current test split and should be verified against the final model evaluation. Since pass/fail status is derived from student marks, high accuracy does not necessarily indicate generalization to new datasets.*

## 📁 Project Structure

```text
student_result_analysis_mini_project/
│
├── data_processing.py
├── visualization.py
├── logistic_and_KNN_model.py
├── results.csv
├── results_analysis.csv
├── readme.md
├── description about project
│
└── plots/
    ├── AVG_MARKS_BAR.png
    ├── MAX_MARKS_BAR.png
    ├── numerical_col_correlation.png
    ├── pass_fail_pie.png
    ├── percentage_distribution_histogram.png
    └── subjects box plot.png
```

## 🚀 How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

3. Run the data processing script:

   ```bash
   python data_processing.py
   ```

4. Generate visualizations:

   ```bash
   python visualization.py
   ```

5. Run the machine learning models:

   ```bash
   python logistic_and_KNN_model.py
   ```

*Make sure the dataset paths in the scripts match your local project folder.*

## 🎯 Key Learning Outcomes

- Data cleaning and preprocessing using Pandas
- Numerical analysis using NumPy
- Data visualization using Matplotlib and Seaborn
- Classification using Logistic Regression and KNN
- Model evaluation using accuracy scores and confusion matrices
- Version control and project management using Git and GitHub

## 👨‍💻 Author

Aman Yadav
