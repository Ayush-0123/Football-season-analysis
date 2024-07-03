import csv

# Define the Premier League table data
premier_league_table = [
    ['Pos', 'Name', 'Pld', 'W', 'D', 'L', 'Goals', '+/-', 'Pts'],
    [1, 'Man City', 38, 32, 2, 4, '95:23', 72, 98],
    [2, 'Liverpool', 38, 30, 7, 1, '89:22', 67, 97],
    [3, 'Chelsea', 38, 21, 9, 8, '63:39', 24, 72],
    [4, 'Spurs', 38, 23, 2, 13, '67:39', 28, 71],
    [5, 'Arsenal', 38, 21, 7, 10, '73:51', 22, 70],
    [6, 'Man Utd', 38, 19, 9, 10, '65:54', 11, 66],
    [7, 'Wolves', 38, 16, 9, 13, '47:46', 1, 57],
    [8, 'Everton', 38, 15, 9, 14, '54:46', 8, 54],
    [9, 'Leicester', 38, 15, 7, 16, '51:48', 3, 52],
    [10, 'West Ham', 38, 15, 7, 16, '52:55', -3, 52],
    [11, 'Watford', 38, 14, 8, 16, '52:59', -7, 50],
    [12, 'Crystal Palace', 38, 14, 7, 17, '51:53', -2, 49],
    [13, 'Newcastle', 38, 12, 9, 17, '42:48', -6, 45],
    [14, 'Bournemouth', 38, 13, 6, 19, '56:70', -14, 45],
    [15, 'Burnley', 38, 11, 7, 20, '45:68', -23, 40],
    [16, 'Southampton', 38, 9, 12, 17, '45:65', -20, 39],
    [17, 'Brighton', 38, 9, 9, 20, '35:60', -25, 36],
    [18, 'Cardiff', 38, 10, 4, 24, '34:69', -35, 34],
    [19, 'Fulham', 38, 7, 5, 26, '34:81', -47, 26],
    [20, 'Huddersfield', 38, 3, 7, 28, '22:76', -54, 16]
]

# Specify the file path
file_path = 'premier_league_2023_24.csv'

# Write data to CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(premier_league_table)

print(f'CSV file {file_path} has been created successfully.')
