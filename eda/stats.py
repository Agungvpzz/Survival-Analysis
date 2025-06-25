import pandas as pd
import numpy as np

from lifelines.statistics import multivariate_logrank_test
from scipy.stats import chi2_contingency

def get_chi2_pearson_report(df, col_target, col_groups):
    """
    return dataframe with following columns: chi2, dof, p, cramer
    """
    stats = {}
    for col_group in col_groups:
        ct = pd.crosstab(df[col_group], df[col_target])    
        chi2, p, dof, expected = chi2_contingency(ct.values)
        n = ct.values.sum()    
        cramer = np.sqrt(chi2 / (n * (min(ct.shape) - 1))) if (min(ct.shape) - 1) > 0 else np.nan
        stats[col_group] = {'chi2': chi2, 'dof': dof, 'pval': p, 'cramer': cramer}

    return pd.DataFrame(stats).T.sort_values('pval').round(4)


def get_logrank_test_report(df, col_event, col_time, col_cats: list):
    stats = []
    for col in col_cats:
        result = multivariate_logrank_test(df[col_time], df[col], df[col_event])    
        stats.append(result.summary.rename({0: col}))
    
    return pd.concat(stats).sort_values('p').round(4)