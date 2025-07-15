import pandas as pd

dataset_files = [
    '2024_fb_ads_president_scored_anon.csv',
    '2024_fb_posts_president_scored_anon.csv',
    '2024_tw_posts_president_scored_anon.csv'
]

for file in dataset_files:
    print(f"Processing dataset: {file}")
    
    df = pd.read_csv(file, encoding='utf-8')
    
    print("\nOverall Statistics:")
    numeric_summary = df.describe().T 
    
    for col in numeric_summary.index:
        count = numeric_summary.at[col, 'count']
        mean = numeric_summary.at[col, 'mean']
        min_value = numeric_summary.at[col, 'min']
        max_value = numeric_summary.at[col, 'max']
        std_deviation = numeric_summary.at[col, 'std']
        
        print(f"{col} - Count: {count}, Mean: {mean}, Min: {min_value}, Max: {max_value}, Std Dev: {std_deviation}")
    
    print("\nCategorical Columns Statistics:")
    for col in df.select_dtypes(include=['object']).columns:
        unique_count = df[col].nunique()
        
    
        most_frequent_value = df[col].mode()[0] 
        most_frequent_count = df[col].value_counts().iloc[0]  
        
        print(f"{col} - Unique Values: {unique_count}, Most Frequent Value: {most_frequent_value}, Count: {most_frequent_count}")
    
    print("\n" + "="*50 + "\n")
