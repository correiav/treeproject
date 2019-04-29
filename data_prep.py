# Import library 
import pandas as pd 

# Get data
trees = pd.read_csv('data/trees.csv')

# Check number of attributes (14 columns) and observations (35924 rows)
print(trees.shape) 

# Check the fisrt 5 observations - good to explore what manipulations you'll need to apply
trees.head(5)

# If you only want to check the header
trees.columns

# Change header from capital to lower case (easier to call columns by their names)
trees.columns = map(str.lower, trees.columns)
print(trees.columns)

# Select only columns: 'town' + 'condition' + 'lat' + 'long' to plot in a map
trees = trees.iloc[:, [2, 5, 12, 13]]

# Select only rows where town & condition are properly filled 
trees = trees.dropna(thresh=4)

# Check if the changes were applied
print(trees.shape)
print(trees.isnull().sum())
# Make sure latitude (lat) & longitude (lon) are floats
print(trees.dtypes)

# Save new curated file with 'xz' extension - i.e. compressed for better performance
trees.to_csv(
    'data/trees.xz',
    encoding='utf-8',
    index=False,
    compression='xz'
    )










