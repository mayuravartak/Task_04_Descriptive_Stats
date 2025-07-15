import csv 
import math

dataset_files = [
    'C:/Mayura/Research_Analyst/period_03/2024_fb_ads_president_scored_anon.csv',
    'C:/Mayura/Research_Analyst/period_03/2024_fb_posts_president_scored_anon.csv',
    'C:/Mayura/Research_Analyst/period_03/2024_tw_posts_president_scored_anon.csv'
]

all_data = {}
for file in dataset_files:
    with open(file, 'r', encoding='utf-8') as f:  
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            data.append(row)
        all_data[file] = data

#Compute
def std_dev(values, mean):
    return math.sqrt(sum((x - mean) ** 2 for x in values) / len(values)) if len(values) > 1 else 0

for file in dataset_files:
    print(f"Processing dataset: {file}")
    
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader) 
        
        numeric_columns = {}
        categorical_columns = {}

        for row in data:
            for col in row:
                try:
                    value = float(row[col])
                    if col not in numeric_columns:
                        numeric_columns[col] = []
                    numeric_columns[col].append(value)
                except ValueError:
                    if col not in categorical_columns:
                        categorical_columns[col] = {}
                    value = row[col]
                    categorical_columns[col][value] = categorical_columns[col].get(value, 0) + 1
        
        print("Overall Statistics:")

        for col, values in numeric_columns.items():
            count = len(values)
            mean = sum(values) / count
            min_value = min(values)
            max_value = max(values)
            std_deviation = std_dev(values, mean)
            print(f"{col} - Count: {count}, Mean: {mean}, Min: {min_value}, Max: {max_value}, Std Dev: {std_deviation}")

        for col, value_counts in categorical_columns.items():
            unique_values = len(value_counts)
            most_frequent_value = max(value_counts, key=value_counts.get)
            most_frequent_count = value_counts[most_frequent_value]
            print(f"{col} - Unique Values: {unique_values}, Most Frequent Value: {most_frequent_value}, Count: {most_frequent_count}")
            
    print("\n")