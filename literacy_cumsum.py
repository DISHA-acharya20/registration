import numpy as np
import pandas as pd

# Sample Data: Literacy rates by quarter for multiple years
# Rows = Years, Columns = Quarters (Q1, Q2, Q3, Q4)
literacy_data = np.array([
    [2.5, 1.5, 2.0, 1.8],  # Year 2022
    [2.2, 1.8, 2.1, 2.0],  # Year 2023
    [2.3, 2.1, 2.2, 1.9],  # Year 2024
])

print("=" * 60)
print("ORIGINAL LITERACY RATES DATA")
print("=" * 60)
df_original = pd.DataFrame(
    literacy_data,
    index=['Year 2022', 'Year 2023', 'Year 2024'],
    columns=['Q1', 'Q2', 'Q3', 'Q4']
)
print(df_original)

print("\n" + "=" * 60)
print("CUMULATIVE SUM - AXIS=1 (ACROSS COLUMNS/QUARTERS)")
print("=" * 60)
print("axis=1 means operation applies horizontally (left to right)")
print("This calculates cumulative sum for each year by quarter\n")

# Calculate cumulative sum along axis 1 (quarters for each year)
cumsum_axis1 = np.cumsum(literacy_data, axis=1)

df_cumsum_axis1 = pd.DataFrame(
    cumsum_axis1,
    index=['Year 2022', 'Year 2023', 'Year 2024'],
    columns=['Q1', 'Q2', 'Q3', 'Q4']
)
print(df_cumsum_axis1)

print("\n" + "=" * 60)
print("CUMULATIVE SUM - AXIS=0 (ACROSS ROWS/YEARS)")
print("=" * 60)
print("axis=0 means operation applies vertically (top to bottom)")
print("This calculates cumulative sum for each quarter across years\n")

# Calculate cumulative sum along axis 0 (years for each quarter)
cumsum_axis0 = np.cumsum(literacy_data, axis=0)

df_cumsum_axis0 = pd.DataFrame(
    cumsum_axis0,
    index=['Year 2022', 'Year 2023', 'Year 2024'],
    columns=['Q1', 'Q2', 'Q3', 'Q4']
)
print(df_cumsum_axis0)

print("\n" + "=" * 60)
print("FINDING QUARTERS WITH CUMULATIVE SUM >= 8")
print("=" * 60)
print("\nFor AXIS=1 (By quarters within each year):")
print("-" * 60)

quarters_axis1 = np.where(cumsum_axis1 >= 8)
print(f"Found {len(quarters_axis1[0])} quarters with cumsum >= 8")

if len(quarters_axis1[0]) > 0:
    print("\nDetails:")
    for year_idx, quarter_idx in zip(quarters_axis1[0], quarters_axis1[1]):
        year = ['Year 2022', 'Year 2023', 'Year 2024'][year_idx]
        quarter = ['Q1', 'Q2', 'Q3', 'Q4'][quarter_idx]
        value = cumsum_axis1[year_idx, quarter_idx]
        print(f"  {year} - {quarter}: Cumulative Sum = {value:.2f}")
else:
    print("  No quarters found with cumsum >= 8")

print("\n" + "-" * 60)
print("For AXIS=0 (By quarters across all years):")
print("-" * 60)

quarters_axis0 = np.where(cumsum_axis0 >= 8)
print(f"Found {len(quarters_axis0[0])} quarters with cumsum >= 8")

if len(quarters_axis0[0]) > 0:
    print("\nDetails:")
    for year_idx, quarter_idx in zip(quarters_axis0[0], quarters_axis0[1]):
        year = ['Year 2022', 'Year 2023', 'Year 2024'][year_idx]
        quarter = ['Q1', 'Q2', 'Q3', 'Q4'][quarter_idx]
        value = cumsum_axis0[year_idx, quarter_idx]
        print(f"  {year} - {quarter}: Cumulative Sum = {value:.2f}")
else:
    print("  No quarters found with cumsum >= 8")

print("\n" + "=" * 60)
print("KEY TAKEAWAY: UNDERSTANDING AXIS PARAMETER")
print("=" * 60)
print("""
axis=0:  Vertical operation (downward ↓) - processes ROWS
         Use when you want cumulative sum across YEARS for each QUARTER

axis=1:  Horizontal operation (rightward →) - processes COLUMNS  
         Use when you want cumulative sum across QUARTERS within each YEAR
""")
