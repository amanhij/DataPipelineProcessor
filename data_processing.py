import pandas as pd

def collect_and_preprocess_data(url):
    """
    Collects and preprocesses data from a given URL.
    
    Parameters:
    url (str): The URL of the dataset.
    
    Returns:
    pd.DataFrame: The cleaned and preprocessed DataFrame.
    """
    
    # Step 1: Collect data
    data = pd.read_csv(url)
    
    # Step 2: Basic preprocessing
    data.dropna(inplace=True)  # Removing missing values
    data.drop_duplicates(inplace=True)  # Removing duplicates
    
    # Assuming the dataset has a 'date' column that needs formatting
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], errors='coerce')
        data.dropna(subset=['date'], inplace=True)  # Remove rows where date conversion failed
    
    # Save the cleaned data to a CSV file
    clean_filename = url.split('/')[-1].replace('.csv', '_cleaned.csv')
    data.to_csv(clean_filename, index=False)
    
    return data

# Example usage with sample dataset URLs
data_urls = [
    'https://example.com/jhu_covid19_cases_deaths.csv',  # Placeholder
    'https://example.com/owid_covid19_vaccinations.csv'  # Placeholder
]

cleaned_dataframes = []

for url in data_urls:
    cleaned_data = collect_and_preprocess_data(url)
    cleaned_dataframes.append(cleaned_data)
    print(f"{url} - Data collection and preprocessing complete.")

# Display the first few rows of each dataset for verification
for df in cleaned_dataframes:
    print(df.head())
