from feature import *
from base import *

def create_unique_hdf(use_columns,features,filename,test=False):
    df = get_data(data='all', columns=use_columns)
    ori_col = list(df.columns)
    begin = datetime.datetime.now()
    for x in features:
        df_add_unique(df, x)
    df = df[df.click_id.notnull()][[x for x in df.columns if x not in ori_col]]
    print(df.columns)
    df.to_hdf('./feature/unique.h5', filename, complevel=5)
    end = datetime.datetime.now()
    print((end - begin).total_seconds() // 60, '{} unique features Done'.format(filename))
    print('-'*100)
    
        
        
if __name__=='__main__':
    base_feature = ['app','ip', 'device', 'os', 'channel']
    features = []
    for i in range(0,5):
        for j in range(0,5):
            if i!=j:
                features.append([[base_feature[i]],base_feature[j]])
                features.append([['day', base_feature[i]],base_feature[j]])
    create_unique_hdf(['app', 'ip', 'device', 'os', 'channel', 'click_id', 'day', 'hour' ,'in_test_hh'], features, '1')

    #--------------------------------------------------------------------------------------------------------------------------
    base_feature = ['app','ip', 'device', 'os', 'channel']
    features = []
    for k in range(0,5):
        for i in range(0,5):
            for j in range(i+1,5):
                if i!=j and j!=k and i!=k:
                    features.append([[base_feature[i],base_feature[j]],base_feature[k]])
                    features.append([['day', base_feature[i],base_feature[j]],base_feature[k]])
    print(features)
    create_unique_hdf(['app', 'ip', 'device', 'os', 'channel', 'click_id', 'day', 'hour' ,'in_test_hh'], features, '2')
    #--------------------------------------------------------------------------------------------------------------------------
 
