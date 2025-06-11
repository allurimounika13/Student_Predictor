import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/eamcet_college_data_cleaned.csv")

def predict_colleges(rank, category, gender):
    """
    Predict suitable colleges for a student based on rank, category, and gender.

    Parameters:
    - rank (int): EAMCET rank of the student
    - category (str): Category (e.g., OC, BC_A, SC, ST, etc.)
    - gender (str): Gender (BOYS or GIRLS)

    Returns:
    - DataFrame of matching colleges
    """
    # Format column name based on input
    col = f"{category.upper()} {gender.upper()}"
    
    # If column doesn't exist (invalid input), return empty DataFrame
    if col not in df.columns:
        print(f"⚠️ Category-gender combination '{col}' not found in dataset.")
        return pd.DataFrame(columns=["INSTITUTE NAME", "BRANCH NAME", col, "TUITION FEE", "AFFILIATED"])

    # Filter colleges where student's rank is eligible
    eligible_df = df[df[col] >= rank]

    # Sort by cutoff rank (ascending)
    sorted_df = eligible_df.sort_values(by=col)

    # Return selected columns
    return sorted_df[["INSTITUTE NAME", "BRANCH NAME", col, "TUITION FEE", "AFFILIATED"]]
