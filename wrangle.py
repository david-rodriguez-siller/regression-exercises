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

def minmax_scaler_tvt(train, validate, test):
    # list of columns float and int dtypes
    num_cols = list(train.select_dtypes(include = ['float64', 'int64', 'complex']).columns)
    
    # min-max scaler object
    scaler = sklearn.preprocessing.MinMaxScaler()
    
    # fit scaler
    scaler.fit(train[num_cols])
    
    # scale
    train_scaled = scaler.transform(train[num_cols])
    validate_scaled = scaler.transform(validate[num_cols])
    test_scaled = scaler.transform(test[num_cols])

   # new column names
    new_column_names = [c + '_scaled' for c in num_cols]

    # add scaled columns to input dataset
    train[new_column_names] = scaler.transform(train[num_cols])
    validate[new_column_names] = scaler.transform(train[num_cols])
    test[new_column_names] = scaler.transform(train[num_cols])
    
    return train, validate, test

def standard_scaler_tvt(train, validate, test):
    # list of columns float and int dtypes
    num_cols = list(train.select_dtypes(include = ['float64', 'int64', 'complex']).columns)
    
    # standard scaler object
    scaler = sklearn.preprocessing.StandardScaler()
    
    # fit scaler
    scaler.fit(train[num_cols])
    
    # scale
    train_scaled = scaler.transform(train[num_cols])
    validate_scaled = scaler.transform(validate[num_cols])
    test_scaled = scaler.transform(test[num_cols])

    # new column names
    new_column_names = [c + '_scaled' for c in num_cols]

    # add scaled columns to input dataset
    train[new_column_names] = scaler.transform(train[num_cols])
    validate[new_column_names] = scaler.transform(train[num_cols])
    test[new_column_names] = scaler.transform(train[num_cols])
    
    return train, validate, test

def robust_scaler_tvt(train, validate, test):
    # list of columns float and int dtypes
    num_cols = list(train.select_dtypes(include = ['float64', 'int64', 'complex']).columns)
    
    # robust scaler object
    scaler = sklearn.preprocessing.RobustScaler()
    
    # fit scaler
    scaler.fit(train[num_cols])
    
    # scale
    train_scaled = scaler.transform(train[num_cols])
    validate_scaled = scaler.transform(validate[num_cols])
    test_scaled = scaler.transform(test[num_cols])

    # new column names
    new_column_names = [c + '_scaled' for c in num_cols]

    # add scaled columns to input dataset
    train[new_column_names] = scaler.transform(train[num_cols])
    validate[new_column_names] = scaler.transform(train[num_cols])
    test[new_column_names] = scaler.transform(train[num_cols])
    
    return train, validate, test

def nonlinear_scaler_tvt(train, validate, test):
    # list of columns float and int dtypes
    num_cols = list(train.select_dtypes(include = ['float64', 'int64', 'complex']).columns)
    
    # non-linear scaler object
    scaler = sklearn.preprocessing.QuantileTransformer(output_distribution = 'normal')
    
    # fit scaler
    scaler.fit(train[num_cols])
    
    # scale
    train_scaled = scaler.transform(train[num_cols])
    validate_scaled = scaler.transform(validate[num_cols])
    test_scaled = scaler.transform(test[num_cols])
    
    # new column names
    new_column_names = [c + '_scaled' for c in num_cols]

    # add scaled columns to input dataset
    train[new_column_names] = scaler.transform(train[num_cols])
    validate[new_column_names] = scaler.transform(train[num_cols])
    test[new_column_names] = scaler.transform(train[num_cols])

    return train, validate, test