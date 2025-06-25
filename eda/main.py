import pandas as pd
from .plot import PlotlyEDA
from .stats import get_chi2_pearson_report


def get_main_eda(df, col_event, col_time, col_groups=None, **layouts):
	columns = df.columns.drop(col_time)	
	chi2_stats = None
	fig_event_cat_dist = None
	
	if col_groups:
		chi2_stats = get_chi2_pearson_report(df, col_event, col_groups)		
		fig_event_cat_dist = PlotlyEDA.plot_bar_event_categorical_composition(
			df, col_event, chi2_stats.index, chi2_stats, True, **layouts
		)		
			
	fig_bars = PlotlyEDA.plot_bar_corr(df[columns], col_event, **layouts)
	fig_event_composition = PlotlyEDA.plot_event_composition(df, col_event)	
	
	return {		
		'fig_bar_corr': fig_bars[0],
		'fig_bar_corr_grouped': fig_bars[1],
		'fig_event_composition': fig_event_composition.update_layout(**layouts),
		'fig_bar_event_categorical_composition': fig_event_cat_dist,
		'chi2_stats': chi2_stats
	}