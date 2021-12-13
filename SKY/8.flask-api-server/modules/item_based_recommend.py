def item_based_recommend():
    import pandas as pd
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    query = input("회사명 입력: ")  
    
    
    df = pd.read_csv('/Users/sky/class_python/6.Recommendation/saramin_jobkorea_sjy_real.csv', index_col=0)
    df.reset_index(inplace=True)
    
    company = df['company'].tolist()
    category = df['category']
    category = category.to_list()
    
    tfidf =  TfidfVectorizer(max_features=100)
    b = tfidf.fit_transform(category)
    
    tfidf_df = pd.DataFrame(b.toarray(), columns=sorted(tfidf.vocabulary_))
    tfidf_df.index = company
    
    from sklearn.metrics.pairwise import cosine_similarity
    sim_table2 = cosine_similarity(tfidf_df, tfidf_df)
    
    company2idx = {}
    for i, c in enumerate(df['company']): 
        company2idx[i] = c
        
    

    idx2company = {}
    for i, c in company2idx.items(): idx2company[c] = i

    idx = idx2company[query]
    
    
    sim_scores = [(i, c) for i, c in enumerate(sim_table2[idx]) if i != idx]
    sim_scores = sorted(sim_scores, key= lambda x: x[1], reverse=True)
    sim_scores = [(company2idx[i], score) for i, score in sim_scores[0:10]]
    
    
    return(sim_scores)
    
if __name__ == "__main__":
    sim_scores = item_based_recommend()
    print(sim_scores)