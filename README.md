This project uses machine learning to predict whether individuals will utilize free healthcare services based on health and household survey data. 
It aims to support healthcare planning and policy decisions by identifying key factors that influence treatment-seeking behavior.

## Objective
To build and deploy a predictive model that determines the likelihood of individuals utilizing free healthcare if offered, using demographic, health, and socio-economic data.

## Dataset
The dataset contains responses from **1,429 individuals** and includes features such as:
- Distance to healthcare facility
- Log-transformed asset value
- Literacy of female adult
- Mosquito net usage
- Number of illness days in a week
- Child’s age, breastfeeding duration
- Access to safe drinking water, vaccine card, etc.

  In this project, the dataset was first preprocessed by handling missing values and detecting outliers to ensure data quality. Feature scaling was applied.
  After preprocessing, feature selection was performed using correlation analysis and model-based importance scores to retain only the most relevant features.
  Among them, the Random Forest Classifier delivered the best results, achieving an accuracy of 95.76%.
  Model performance was assessed using precision, recall, F1-score, and a confusion matrix.Multiple classification algorithms—including Logistic Regression, Decision Tree, Random Forest, and XGBoost—were trained and evaluated.
  Finally, hyperparameter tuning was conducted using GridSearchCV, and the optimal configuration for the Random Forest model was found to be max_depth=15, max_features="sqrt", n_estimators=50, and random_state=50.

## Deployment
A user-friendly Flask web application was created where users can input relevant details to predict if free healthcare will be utilized.
 
