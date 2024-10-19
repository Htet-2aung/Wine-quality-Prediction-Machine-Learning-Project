# Wine-quality-Prediction-Machine-Learning-Project
This project focuses on analyzing the Wine Quality dataset using machine learning techniques for both classification and regression tasks. The aim is to predict wine quality based on various physicochemical properties of the wines, while addressing issues such as overfitting and feature selection.

## Dataset

- **Name**: Wine Quality
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/186/wine+quality)
- **Description**: The dataset includes several input variables (e.g., acidity, sugar content, alcohol level) and a target variable indicating the quality of the wine, rated from 0 to 10.

## Features

- **Data Exploration**: Initial data analysis and visualization to understand the dataset.
- **Data Preprocessing**: Cleaning, normalization, and preparation of data for modeling.
- **Machine Learning Models**:
  - **Classification Models**:
    - K-Nearest Neighbors (KNN)
    - Decision Tree
    - Random Forest
    - Naive Bayes
  - **Regression Models**:
    - Linear Regression
    - Lasso Regression
    - Decision Tree Regression
    - Random Forest Regression
- **Overfitting Analysis**: Strategies to identify and mitigate overfitting, including pruning and regularization.
- **Feature Selection**: Identifying key features using correlation analysis.

## Getting Started

### Prerequisites

To run this project, ensure you have the following Python packages installed:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/wine-quality-prediction.git
   cd wine-quality-prediction
   ```

2. Open the Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

3. Run the notebook cells to perform the analysis and model training.

## Results

The project includes detailed results for each model, including accuracy scores for classification and R-squared values for regression. Visualizations are provided to help interpret the results, including confusion matrices and feature importance plots.

## Future Work

- Implement hyperparameter tuning for improved model performance.
- Explore advanced algorithms like Gradient Boosting or Neural Networks.
- Incorporate additional feature engineering techniques to enhance predictions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/186/wine+quality) for providing the dataset.
- The community for the various libraries used in this project.
