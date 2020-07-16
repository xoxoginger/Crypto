import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

fn = r'C:/Users/hui/Desktop/diffs1.csv'
df = pd.read_csv(fn, sep='\s+', header=None, names=['Times', 'Difference'], parse_dates=['Times'])
df.plot(x='Times', y='Difference', rot=0, figsize=(12, 8), grid=True, marker='o')
plt.savefig('1.png')
plt.close()

fn = r'C:/Users/hui/Desktop/diffs2.csv'
df = pd.read_csv(fn, sep='\s+', header=None, names=['Times', 'Difference'], parse_dates=['Times'])
df.plot(x='Times', y='Difference', rot=0, figsize=(12, 8), grid=True, marker='o')
plt.savefig('2.png')
plt.close()

fn = r'C:/Users/hui/Desktop/diffs3.csv'
df = pd.read_csv(fn, sep='\s+', header=None, names=['Times', 'Difference'], parse_dates=['Times'])
df.plot(x='Times', y='Difference', rot=0, figsize=(12, 8), grid=True, marker='o')
plt.savefig('3.png')
