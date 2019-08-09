import numpy as np
import pandas as pd
df=pd.DataFrame({'col1':['A','A','B',np.nan,'D','C'],
                 'col2':[2,1,9,13.11,12.2,7],
                 'col3':[0,1,9,4,2,8]
})
df['col2'].apply(str)
df['col3'].apply(int)
print(df)
print(df.sort_values(by=['col2'],na_position='first'))
