import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import patsy
from matplotlib import pyplot as plt
​
​'''
We'll use statsmodels to fit some (Ordinary Least Squares) linear models using random data.

First make a response y of 200 random numbers. 
Then generate 20 random features in an X to predict with. Fit a linear model and check the summary() output.

Check out the model's R-squared and Adj. R-squared. 
Repeat the feature generation and model fitting process with 40, 60, 80, and 100 features. 
What happens with R-squared and Adj. R-squared?
'''

rsquared = []
rsquared_adj = []

# Y is 200 observations of random
# X is N number of feature variables that is also random
for i in range(1,101): # number of feature variables
    df = pd.DataFrame(np.random.uniform(0,1,size=(200, i+1)))
    
    lm = smf.ols('df[0] ~ df.iloc[:,1:]', data = df)
    fit_lm = lm.fit()
    
​
    rsquared.append(fit_lm.rsquared)
    rsquared_adj.append(fit_lm.rsquared_adj)
    
plt.plot(range(1,101),rsquared, label = 'R-Squared')
plt.plot(range(1,101), rsquared_adj, 'r', label = 'Adj. R-Squared')
​
plt.legend()
plt.show()

# moral of the story: as number of features go up, R_Squared will always get better, but Adj.R_Squared will stay bad
