def collaborative_recommend(datapath):
    from surprise import SVD
    from surprise.model_selection import cross_validate
    from surprise import Reader
    from surprise import Dataset
    import pandas as pd
    import numpy as np
    
    df = pd.read_csv(datapath, index_col=0)
    reader = Reader(rating_scale=(0,1))
    data = Dataset.load_from_df(df[['memberid', 'company_Index', 'value']], reader)
    
    #SVD
    model = SVD()
    # 교차검증
    cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, n_jobs=4, verbose=True)
    
    from surprise.model_selection import train_test_split
    train_set, test_set = train_test_split(data, test_size=1.0)
    
    model.fit(train_set)
    predictions = model.test(test_set)
    
    predict = model.predict('sky', 8)
    return (predict)
    
if __name__ == "__main__":
    predict = collaborative_recommend('/Users/sky/class_python/6.Recommendation/company_member.csv')
    print(predict)
