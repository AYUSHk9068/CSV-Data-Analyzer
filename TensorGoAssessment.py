import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'C:/Users/ayush/OneDrive/Desktop/tensorgoassesement/Data-Science-Jobs.csv'
data = pd.read_csv(file_path)
print("Data Preview:")
print(data.head())
salary = data['Company Rating']
if 'Company Rating' not in data.columns:
    raise ValueError("The 'Company Rating' column is not present in the CSV file.")
salary1 = data['Position']
mean = salary.mean()
median = salary.median()
mode = salary.mode()[0]
std_dev = salary.std()
cor_coe = data['Position'].corr(data['Company Rating'])
print("Statistics Analysis:")
print()
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
print("Correlation Coefficient:", cor_coe)
print()
plt.figure(figsize=(8, 5))
sns.histplot(data['Company Rating'], kde=True)  
plt.title('Histogram of Company Rating')
plt.xlabel('Company Rating')
plt.ylabel('Frequency')
plt.savefig('CompanyRatingHistogram.png')  
plt.show()  
plt.figure(figsize=(8, 5))
sns.histplot(data['Position'], kde=True)  
plt.title('Histogram of Positon')
plt.xlabel('Position')
plt.ylabel('Frequency')
plt.savefig('PositionHistogram.png')  
plt.show()  
plt.figure(figsize=(8,5))
sns.scatterplot(x=data['Company Rating'], y=data['Position'])  
plt.title('Scatter Plot: Company Rating vs Position')
plt.xlabel('Company Rating')
plt.ylabel('Position')
plt.savefig('scatter_plot.png')  
plt.show()  
data['Position'] = pd.to_datetime(data['Position'])  
plt.figure(figsize=(8, 5))
sns.lineplot(x=data['Company Rating'], y=data['value'])  
plt.title('Line Plot: Company Rating Over Position')
plt.xlabel('Company Rating')
plt.ylabel('Position')
plt.savefig('line_plot.png')  
plt.show()  
def answer_question(question):
    question = question.lower()
    if 'mean' in question:
        column = question.split('mean of ')[-1]
        if column in data.columns:
            mean_value = mean()
            return f"The mean of the {column} column is found."
        else:
            return f"The mean of the {column} column is {mean}."
    
    elif 'median' in question:
        column = question.split('median of ')[-1]
        if column in data.columns:
            median_value = data[column].median()
            return f"The median of the '{column}' column is found."
        else:
            return f"The median of the {column} column is {median}."
    
    elif 'mode' in question:
        column = question.split('mode of ')[-1]
        if column in data.columns:
            mode_value = data[column].mode().iloc[0]
            return f"The mode of the {column} column is found."
        else:
            return f"The mode of the {column} column is {mode}."
    
    elif 'standard deviation' in question:
        column = question.split('standard deviation of ')[-1]
        if column in data.columns:
            std_dev_value = data[column].std()
            return f"The standard deviation of the {column} column is found"
        else:
            return f"The standard deviation of the {column} column is {std_dev}.."
    
    elif 'correlation' in question:
        columns = question.split('correlation between ')[-1].split(' and ')
        if len(columns) == 2 and columns[0] in data.columns and columns[1] in data.columns:
            correlation_value = data[columns[0]].corr(data[columns[1]])
            return f"The correlation between {columns[0]} and {columns[1]} is {cor_coe}."
        else:
            return f"The Correlation Coefficient of the Company Rating and Position column is {cor_coe}"
    
    else:
        return "Sorry, I don't understand the question."

questions = [
    "What is the mean of Company Rating ",
    "What is the median of Company Rating ",
    "What is the mode of Company Rating",
    "What is the standard deviation of Company Rating",
    "What is the correlation between Company Rating and Position "
]
for q in questions:
    print(f"Question: {q}")
    print("Answer:", answer_question(q))
    print()
