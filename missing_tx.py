import pandas as pd
import itertools

def find_combinations(values, target):
    results = []
    # Generate all combinations of all lengths
    for r in range(1, len(values) + 1):
        for combination in itertools.combinations(values, r):
            if sum(combination) == target:
                print(f"Find combination: {combination}:")
                results.append(combination)
    return results

# Read Excel file, filter rows, and extract values from a specific column
def read_and_filter_excel_column(file_path, sheet_name, column_name, filter_column, filter_value):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df[column_name] = df[column_name].replace('[\$,]', '', regex=True).astype(float)

    # Filter rows where filter_column equals filter_value
    filtered_df = df[df[filter_column] == filter_value]
    # Convert the target column to integers, handling any potential conversion errors
    #values = pd.to_numeric(filtered_df[column_name], errors='coerce').dropna().astype(int).tolist()
    values = filtered_df[column_name].dropna().tolist()
    #values = df[column_name].dropna().tolist()
    return values

# Example usage
file_path = 'Tx_logs.xlsx'  # Path to your Excel file
sheet_name = 'Sheet1'  # Sheet name
column_name = 'Amount'  # Column name or index (e.g., 'A')
filter_column = 'Status'  # Column used for filtering
filter_value = 'Cancelled'  # Value to filter rows by

values = read_and_filter_excel_column(file_path, sheet_name, column_name, filter_column, filter_value)
target = -2329297.50# The target number you want to match

print (values)
combinations = find_combinations(values, target)

print(f"Combinations of values that sum to {target}:")
for combo in combinations:
    print(combo)