# -*- coding: utf-8 -*-
"""Quality Agregation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wk-wKccesbx4COnRa7CbJRdkPD-o6yI6
"""

import pandas as pd
import numpy as np
from collections import Counter, defaultdict

"""# Quality Control"""

#Remove any worker's vote if it is more than one standard deviation outside of the mean
def remove_bad_workers(df):
  means = defaultdict(float)
  std = defaultdict(float)
  group =  df.groupby(by=['zpid']).std()
  for i, std_i in zip(group.index, group['answerPrice']):
    std[i] = std_i

  group =  df.groupby(by=['zpid']).mean()
  for i, mean_i in zip(group.index, group['answerPrice']):
    means[i] = mean_i

  new_df = pd.DataFrame(columns= df.columns)
  for _, row in df.iterrows():
    zpid = row['zpid']
    if row['answerPrice'] > means[zpid] + std[zpid] or row['answerPrice'] < means[zpid] - std[zpid]:
      continue
    new_df = new_df.append(row)
  new_df.to_csv('QC1_output.csv')
  return new_df

#Assign weights to workers based on thier reciprical average distance to the mean crowd price
def weigh_workers(df):
  within_mean = defaultdict(int)
  votes = defaultdict(int)
  means = defaultdict(float)

  group =  df.groupby(by=['zpid']).mean()
  for i, mean_i in zip(group.index, group['answerPrice']):
    means[i] = mean_i
  for _, row in df.iterrows():
    zpid = row['zpid']
    within_mean[row['workerId']] += abs(row['answerPrice'] - means[zpid])
    votes[row['workerId']] += 1

  quality = defaultdict(float)
  csv = []
  for id in votes:
    quality[id] = 1 / (within_mean[id] / votes[id])
    csv.append((id, quality[id]))
  df_csv = pd.DataFrame(csv, columns=['workerId', 'quality'])
  df_csv.to_csv('QC2_output.csv')
  return quality

"""# Aggregation"""

#Find the true label of each house as voted by workers (true label is mean guess)
def find_crowd_price(df):
  mean_price = defaultdict(float)
  votes = defaultdict(int)

  for _, row in df.iterrows():
    mean_price[row['zpid']] += float(row['answerPrice'])
    votes[row['zpid']] += 1

  for zpid in mean_price:
    mean_price[zpid] = mean_price[zpid] / votes[zpid]

  csv = []
  for id in mean_price:
    csv.append((id, mean_price[id]))
  out = pd.DataFrame(csv, columns=['zpid', 'crowd_price'])
  out.to_csv('AG1_output.csv')

#Find the true label of each house based on weight of workers (as weighted average)
def get_weighted_prices(df, quality):
  price = defaultdict(float)
  weight = defaultdict(float)

  for _, row in df.iterrows():
    zpid, worker_id = row['zpid'], row['workerId']
    price[zpid] += quality[worker_id] * row['answerPrice']
    weight[zpid] += quality[worker_id]

  final_prices = []
  for zpid in price:
    final_prices.append((zpid, price[zpid]/ (weight[zpid] + 0.001)))
  weighted_df = pd.DataFrame(final_prices, columns=['zpid', 'crowd_price'])
  weighted_df.to_csv('AG2_output.csv')
  return weighted_df

#Main
def main():
    df_input = pd.read_csv('/content/QC_input.csv')

    #Quality control
    QC1 = remove_bad_workers(df_input)
    QC2 = weigh_workers(df_input)

    AG1 = find_crowd_price(QC1)
    AG2 = get_weighted_prices(df_input, weight)
    #remove_bad rows -> QC1 -> mean aggregation -> AG1
    #weight workers -> QC2 (worker_id, quality) -> weighted average aggreagtion -> AG2

if __name__ == '__main__':
    main()
