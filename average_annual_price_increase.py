import csv
from statistics import mean 

with open('data-shopify.csv', 'r') as f:
  reader = csv.reader(f)
  values = list(reader)

def calculate_average_annual_increase_per_item (rows):

  price = rows[0][2]
  prev_year = ''
  prices = []

  for row in rows:

    year = row[4].split('-')[0]
    price = float(row[3])

    if prev_year == '': 

      prev_year = year
      prices.append(price)
    elif year != prev_year:

      prev_year = year
      prices.append(price)

  percent_increases = []

  for i in range(1, len(prices)):

    percent_increases.append((prices[i] - prices[i-1])/prices[i-1])

  return mean(percent_increases)
    
average_annual_increases_for_all_items = []
current_product_id = values[1][0]
current_set = []

for value in values[1:]:

  if value[0] != current_product_id: 
    average_annual_increases_for_all_items.append(calculate_average_annual_increase_per_item(current_set))
    current_set.clear()
    current_product_id = value[0]
  else:

    current_set.append(value)

print(mean(average_annual_increases_for_all_items) * 100)