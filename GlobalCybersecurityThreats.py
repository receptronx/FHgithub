import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_cybersecurity_data(file_path):
    """
    Performs simple analysis on the Global Cybersecurity Threats dataset.

    Args:
        file_path (str): The path to the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}\n")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return

    # --- 1. Basic Data Exploration ---
    print("--- 1. Basic Data Exploration ---")
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    print("\nDataset Information:")
    df.info()

    print("\nDescriptive Statistics for numerical columns:")
    print(df.describe())

    print("\nMissing values per column:")
    print(df.isnull().sum())

    # --- 2. Simple Analysis ---
    print("\n--- 2. Simple Analysis ---")

    print("\nTop 10 Threat Types:")
    print(df['Threat Type'].value_counts().head(10))

    print("\nTop 10 Attack Vectors:")
    print(df['Attack Vector'].value_counts().head(10))

    print("\nTop 10 Affected Industries:")
    print(df['Affected Industry'].value_counts().head(10))

    print("\nSeverity Level Distribution:")
    print(df['Severity Level'].value_counts())

    print("\nAverage Financial Impact ($M) by Threat Type:")
    print(df.groupby('Threat Type')['Financial Impact ($M)'].mean().sort_values(ascending=False).head(10))

    print("\nTotal Data Breached (GB) per Year:")
    print(df.groupby('Year')['Data Breached (GB)'].sum().sort_index())

    print("\nAverage Response Time (Hours) by Severity Level:")
    print(df.groupby('Severity Level')['Response Time (Hours)'].mean().sort_values())

    # --- 3. Basic Visualizations (Optional) ---
    print("\n--- 3. Basic Visualizations (Plots will be displayed) ---")

    # Set style for plots
    sns.set_style("whitegrid")

    # Plot 1: Threat Type Distribution
    plt.figure(figsize=(12, 7))
    sns.countplot(y='Threat Type', data=df, order=df['Threat Type'].value_counts().index[:10], palette='viridis')
    plt.title('Top 10 Most Frequent Threat Types (2015-2024)')
    plt.xlabel('Number of Incidents')
    plt.ylabel('Threat Type')
    plt.tight_layout()
    plt.show()

    # Plot 2: Financial Impact by Year
    plt.figure(figsize=(10, 6))
    financial_impact_yearly = df.groupby('Year')['Financial Impact ($M)'].sum()
    sns.lineplot(x=financial_impact_yearly.index, y=financial_impact_yearly.values, marker='o', color='red')
    plt.title('Total Financial Impact ($M) by Year (2015-2024)')
    plt.xlabel('Year')
    plt.ylabel('Total Financial Impact ($M)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot 3: Severity Level Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Severity Level', data=df, order=['Low', 'Medium', 'High', 'Critical'], palette='cividis')
    plt.title('Distribution of Severity Levels')
    plt.xlabel('Severity Level')
    plt.ylabel('Number of Incidents')
    plt.tight_layout()
    plt.show()

    print("\nAnalysis complete. Check the console for printed output and new windows for plots.")

if __name__ == "__main__":
    # Define the path to your dataset
    dataset_file = '/home/ubuntu/FHgithub/Global_Cybersecurity_Threats_2015-2024.csv'
    analyze_cybersecurity_data(dataset_file)