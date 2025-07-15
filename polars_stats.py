import polars as pl

dataset_files = [
    '2024_fb_ads_president_scored_anon.csv',
    '2024_fb_posts_president_scored_anon.csv',
    '2024_tw_posts_president_scored_anon.csv'
]

for file in dataset_files:
    print(f"Processing dataset: {file}")
    
    df = pl.read_csv(file)
    
    print("\nOverall Statistics:")
    
    numeric_cols = [col for col in df.columns if df[col].dtype in [pl.Float64, pl.Int64]]  
    
    for col in numeric_cols:
        count = df[col].is_null().sum()
        mean = df[col].mean()
        min_value = df[col].min()
        max_value = df[col].max()
        std_deviation = df[col].std()

        print(f"{col} - Count: {count}, Mean: {mean}, Min: {min_value}, Max: {max_value}, Std Dev: {std_deviation}")
    
    print("\nCategorical Columns Statistics:")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            unique_count = df[col].n_unique()

            most_frequent_value = df[col].mode()[0]
            most_frequent_count = df[col].value_counts().to_pandas().iloc[0, 1]

            print(f"{col} - Unique Values: {unique_count}, Most Frequent Value: {most_frequent_value}, Count: {most_frequent_count}")
    
    print("\n" + "="*50 + "\n")
