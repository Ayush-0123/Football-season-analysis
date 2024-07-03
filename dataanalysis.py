import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
file_path = 'premier_league_2023_24.csv'
df = pd.read_csv(file_path)

# Fix the Goals column, split it into GF (Goals For) and GA (Goals Against)
df[['GF', 'GA']] = df['Goals'].str.split(':', expand=True).astype(int)

# Drop the original Goals column as we now have GF and GA
df.drop(columns=['Goals'], inplace=True)

# Display the first few rows of the dataframe
print(df.head())

# Summary statistics for numerical columns
print(df.describe())

# Check data types and missing values
print(df.info())

# Group by 'Pos' and calculate average values for numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns
average_stats = df.groupby('Pos')[numeric_cols].mean()
print(average_stats)

# Calculate win percentage for each team
df['Win_Percentage'] = (df['W'] / df['Pld']) * 100

# Example 1: Stacked bar plot of wins, draws, and losses by team
plt.figure(figsize=(12, 8))
df.set_index('Name')[['W', 'D', 'L']].plot(kind='bar', stacked=True, color=['green', 'gray', 'red'])
plt.title('Wins, Draws, and Losses by Team')
plt.xlabel('Team')
plt.ylabel('Matches')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.show()

# Example 2: Pairplot for key performance indicators
sns.pairplot(df[['GF', 'GA', 'Pts', 'Win_Percentage']], kind='reg', diag_kind='kde', markers='+', plot_kws={'line_kws':{'color':'red'}})
plt.suptitle('Pairplot of Goals For, Goals Against, Points, and Win Percentage', y=1.02)
plt.show()

# Example 3: Heatmap of correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
plt.title('Correlation Matrix of Premier League Statistics')
plt.show()

# Example 4: Bar plot of points by team
plt.figure(figsize=(10, 6))
sns.barplot(x='Pts', y='Name', data=df.sort_values(by='Pts', ascending=False), palette='viridis')
plt.title('Points by Team in Premier League 2023-24 Season')
plt.xlabel('Points')
plt.ylabel('Team')
plt.show()

# Example 5: Scatter plot of goals scored vs goals conceded
plt.figure(figsize=(8, 6))
sns.scatterplot(x='GF', y='GA', data=df, hue='Name', palette='Set2', s=100)
plt.title('Goals For vs Goals Against')
plt.xlabel('Goals For (GF)')
plt.ylabel('Goals Against (GA)')
plt.show()

# Example 6: Box plot of wins by team
plt.figure(figsize=(10, 6))
sns.boxplot(x='W', y='Name', data=df.sort_values(by='W', ascending=False), palette='Pastel1')
plt.title('Wins by Team in Premier League 2023-24 Season')
plt.xlabel('Wins')
plt.ylabel('Team')
plt.show()
