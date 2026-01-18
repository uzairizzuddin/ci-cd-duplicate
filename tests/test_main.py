import sys
import os
import pandas as pd
import pytest

# Add the src directory to the Python path so we can import main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import load_and_process_data

def test_no_duplicates():
    """Test if duplicate rows are removed from sales.csv."""
    # Run the processing function
    load_and_process_data(filepath="data/sales.csv", output_path="data/test_processed.csv")
    
    # Load the result
    df = pd.read_csv("data/test_processed.csv")
    
    # Assert that there are 0 duplicates
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed!"
    
    # Clean up test file (optional)
    if os.path.exists("data/test_processed.csv"):
        os.remove("data/test_processed.csv")