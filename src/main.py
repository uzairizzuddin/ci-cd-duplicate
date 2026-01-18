import pandas as pd
import os

def load_and_process_data(filepath="data/sales.csv", output_path="data/processed_sales.csv"):
    # Check if file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found.")

    # Load the dataset
    df = pd.read_csv(filepath)
    print(f"Original dataset shape: {df.shape}")

    # Remove duplicate rows
    df = df.drop_duplicates()
    print(f"Dataset shape after removing duplicates: {df.shape}")

    # Save the processed dataset
    df.to_csv(output_path, index=False)
    print(f"Processed dataset saved to {output_path}")
    
    return df

if __name__ == "__main__":
    load_and_process_data()