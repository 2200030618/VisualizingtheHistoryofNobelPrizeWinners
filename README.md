# Visualizing the History of Nobel Prize Winners

## Overview
This project explores and analyzes the Nobel Prize dataset, covering awardees from 1901 to 2023. The dataset is sourced from the Nobel Prize API and is available in the `nobel.csv` file. The goal of this project is to answer key questions about Nobel Prize winners, including trends in award distribution, gender representation, and geographical distribution of laureates.

## Tools and Libraries Used
The project is implemented using Python and the following key libraries:
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations and handling missing values.
- **Seaborn**: For creating informative visualizations.
- **Matplotlib**: For plotting charts and graphs.

## Methods and Steps
### 1. Data Loading and Cleaning
- The dataset is loaded using Pandas.
- Date columns (`birth_date` and `death_date`) are converted to datetime format.
- Missing values in categorical columns such as `birth_city`, `birth_country`, `sex`, `organization_name`, etc., are filled with "Unknown" to maintain consistency.

### 2. Data Visualization
Several visualizations were created to analyze and interpret the data:

#### **Nobel Prizes Awarded Per Year**
- A histogram is plotted to show the number of Nobel Prizes awarded each year from 1901 to 2023.
- A Kernel Density Estimate (KDE) plot is added for smooth visualization.
  ![No_of_prizes_awarded_per_year](https://github.com/user-attachments/assets/fc93b2ba-6b3e-421e-981c-f6fa03ab1636)


#### **Distribution of Nobel Prizes by Category**
- A count plot shows the number of Nobel Prizes awarded per category (e.g., Physics, Chemistry, Peace, etc.).
  ![category](https://github.com/user-attachments/assets/957229ce-b77a-48a9-9f58-b49907376cbb)


#### **Gender Distribution of Nobel Laureates**
- A count plot visualizes the number of male and female Nobel Prize winners.
![gender_distribution](https://github.com/user-attachments/assets/e605c48f-b640-4075-8480-b3e761a7f846)

#### **Top 10 Countries with the Most Nobel Laureates**
- A bar plot is created to display the top 10 countries with the highest number of Nobel Prize winners.
  ![countries](https://github.com/user-attachments/assets/af6f0b8a-96c3-45ce-9f9c-5da458dc69a7)


#### **Gender Trends Over Time**
- A line plot is generated to track the number of male and female laureates over time, highlighting gender trends in Nobel Prize awards.
![gender_trends](https://github.com/user-attachments/assets/4d484e97-b13d-4578-ac4a-17fa54d3a9f3)

## Key Findings
- The number of Nobel Prizes awarded has varied over time, with notable fluctuations.
- Some categories, such as Physics and Medicine, have awarded more prizes compared to others.
- A significant gender disparity exists, with male laureates greatly outnumbering female laureates.
- The top 10 countries with the most Nobel laureates include the United States, United Kingdom, and Germany, indicating a concentration of awardees from these nations.
- Gender trends reveal that while female representation has increased over time, it remains significantly lower than male representation.

## Conclusion
This project provides valuable insights into Nobel Prize trends over the years. By leveraging data visualization techniques, we can uncover patterns in award distribution, gender disparities, and country-wise representation. Future improvements can include deeper analysis, such as correlations between Nobel Prize winners and educational institutions, or sentiment analysis on Nobel lectures.

## How to Use This Project
1. Clone the repository from GitHub.
2. Install the required Python libraries using:
   ```bash
   pip install pandas numpy seaborn matplotlib
   ```
3. Run the Jupyter Notebook or Python script to generate visualizations and insights.

## Author
Sirisha Penamakuri

