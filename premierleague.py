import csv

# Define the Premier League table data
premier_league_table = [
    ['Pos', 'Team', 'Pl', 'W', 'D', 'L', 'F', 'A', 'GD', 'Pts'],
    [1, 'Manchester City', 38, 28, 7, 3, 96, 34, 62, 91],
    [2, 'Arsenal', 38, 28, 5, 5, 91, 29, 62, 89],
    [3, 'Liverpool', 38, 24, 10, 4, 86, 41, 45, 82],
    [4, 'Aston Villa', 38, 20, 8, 10, 76, 61, 15, 68],
    [5, 'Tottenham Hotspur', 38, 20, 6, 12, 74, 61, 13, 66],
    [6, 'Chelsea', 38, 18, 9, 11, 77, 63, 14, 63],
    [7, 'Newcastle United', 38, 18, 6, 14, 85, 62, 23, 60],
    [8, 'Manchester United', 38, 18, 6, 14, 57, 58, -1, 60],
    [9, 'West Ham United', 38, 14, 10, 14, 60, 74, -14, 52],
    [10, 'Crystal Palace', 38, 13, 10, 15, 57, 58, -1, 49],
    [11, 'Brighton and Hove Albion', 38, 12, 12, 14, 55, 62, -7, 48],
    [12, 'Bournemouth', 38, 13, 9, 16, 54, 67, -13, 48],
    [13, 'Fulham', 38, 13, 8, 17, 55, 61, -6, 47],
    [14, 'Wolverhampton Wanderers', 38, 13, 7, 18, 50, 65, -15, 46],
    [15, 'Everton', 38, 13, 9, 16, 40, 51, -11, 40],
    [16, 'Brentford', 38, 10, 9, 19, 56, 65, -9, 39],
    [17, 'Nottingham Forest', 38, 9, 9, 20, 49, 67, -18, 32],
    [18, 'Luton Town', 38, 6, 8, 24, 52, 85, -33, 26],
    [19, 'Burnley', 38, 5, 9, 24, 41, 78, -37, 24],
    [20, 'Sheffield United', 38, 3, 7, 28, 35, 104, -69, 16]
]

# Specify the file path
file_path = 'premier_league_2023_24.csv'

# Write data to CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(premier_league_table)

print(f'CSV file {file_path} has been created successfully.')