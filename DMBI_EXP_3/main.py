import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
import os

# Path to your CSV files folder - Updated for new directory structure
data_folder = r'v:\All_projects\DMBI_EXP\DMBI_EXP_3\data'

# Get all CSV files
csv_files = [f for f in glob.glob(os.path.join(data_folder, "*.csv")) 
             if 'metadata' not in f and 'NIFTY50_all' not in f]

print(f"Loading {len(csv_files)} stock files for DMBI_EXP_3...")

# Load and combine all CSV files
df_list = []
for file in csv_files[:10]:  # First 10 companies for analysis
    try:
        temp_df = pd.read_csv(file)
        temp_df['Company'] = os.path.basename(file).replace('.csv', '')
        df_list.append(temp_df)
        print(f"Loaded: {os.path.basename(file)}")
    except Exception as e:
        print(f"Error loading {file}: {e}")

if df_list:
    # Combine all dataframes
    df = pd.concat(df_list, ignore_index=True)
    
    # Create a simple boxplot analysis
    plt.figure(figsize=(15, 8))
    sns.boxplot(data=df, x='Company', y='Close')
    plt.title('Stock Closing Prices Distribution by Company')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    output_path = os.path.join(r'v:\All_projects\DMBI_EXP\DMBI_EXP_3', 'boxplot_analysis.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Boxplot saved to: {output_path}")
    
    plt.show()
    
    print(f"\nDataset Summary:")
    print(f"Total records: {len(df):,}")
    print(f"Companies: {df['Company'].nunique()}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
else:
    print("No data files found to process.")
