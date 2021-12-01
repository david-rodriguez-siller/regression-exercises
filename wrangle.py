def wrangle_zillow():
    '''
    This function pulls from the zillow database columns: 'bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet',
       'taxvaluedollarcnt', 'yearbuilt', 'taxamount' where properties are single family residential. 
    '''
    
    # load df with sql database dataset
    df = zillow_data()
    
    # replace blank spaces with nan's
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    # drop nan's
    df = df.dropna()
    
    return df