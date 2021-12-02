def wrangle_zillow():
    '''
    This function pulls from the zillow database columns: 'bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet',
       'taxvaluedollarcnt', 'yearbuilt', 'taxamount' where properties are single family residential. Additionally, blank
       spaces are replaced with nan values, then those values are dropped. Finally, outliers and properties with 0
       bathrooms and less than 200 square feet are dropped.
    '''
    
    # load df with sql database dataset
    df = zillow_data()
    
    # replace blank spaces with nan's
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    # drop nan's
    df = df.dropna()
    
    # remove outliers
    z_scores = stats.zscore(df)
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < 3).all(axis = 1)
    df = df[filtered_entries]
    df = df[df['bathroomcnt'] != 0]
    df = df[df['calculatedfinishedsquarefeet'] > 200]
    
    return df