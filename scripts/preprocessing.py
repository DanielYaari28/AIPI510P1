import pandas as pd

# Load raw College Scorecard data
file_path = "Most-Recent-Cohorts-Institution.csv"
df = pd.read_csv(file_path, low_memory=False)

# Filter univ.

# Keep bachelor's-degree institutions with at least
# 2,000 undergraduate students
eligible = df[
    (df["PREDDEG"] == 3) &
    (df["UGDS"] >= 2000)
].copy()


# Select variables

project_cols = [
    "UNITID",
    "INSTNM",
    "STABBR",
    "CONTROL",
    "UGDS",

    # Student Success
    "C150_4",
    "RET_FT4",

    # Affordability
    "NPT4_PUB",
    "NPT4_PRIV",
    "DEBT_MDN",
    "COSTT4_A",

    # Outcomes
    "MD_EARN_WNE_P10",

    # Accessibility
    "PCTPELL",

    # Context
    "ADM_RATE"
]

project_df = eligible[project_cols].copy()


# Create a net-price variable

# Public schools report NPT4_PUB and private schools
# report NPT4_PRIV, so combine them into one column
project_df["NET_PRICE"] = (
    project_df["NPT4_PUB"]
    .fillna(project_df["NPT4_PRIV"])
)


# Convert numeric columns

numeric_cols = [
    "C150_4",
    "RET_FT4",
    "NET_PRICE",
    "DEBT_MDN",
    "COSTT4_A",
    "MD_EARN_WNE_P10",
    "PCTPELL",
    "ADM_RATE"
]

for col in numeric_cols:
    project_df[col] = pd.to_numeric(
        project_df[col],
        errors="coerce"
    )


# Save cleaned dataset

project_df.to_csv(
    "data/cleaned_college_data.csv",
    index=False
)

print("Preprocessing complete.")
print("Final dataset shape:", project_df.shape)
