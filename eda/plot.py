import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class PlotlyEDA:

	@staticmethod
	def plot_bar_corr(df, col_target, **layouts):
		"""
		Return fig_bar_corr, fig_grouped_bar_corr
		"""

		# Create correlation data
		df_corr = pd.get_dummies(df, prefix_sep=' | ').drop(columns=col_target).corrwith(df[col_target])
		df_corr = df_corr.round(3).reset_index(name='corr')
		df_corr['variable'] = df_corr['index'].map(lambda x: x.split(' | ')[0])
		df_corr['std'] = df_corr.groupby('variable')['corr'].transform('std')
		df_corr = df_corr.sort_values(['std', 'corr'], ascending=False)

		variables = df_corr['variable'].unique()
		colors = px.colors.qualitative.Plotly
		colors = (colors * (1 + int(len(variables) / len(colors))))[:len(variables)]
		colormap = dict(zip(variables, colors))
		df_corr['color'] = df_corr['variable'].map(colormap)

		# Create continuous bar
		fig_bar = px.bar(
			df_corr.sort_values('corr'),
			x='index',
			y='corr',
			color='corr',		
			text_auto=True,
			height=600,
			title=f'Correlation of Features with {col_target.title()}'
		)
		fig_bar.update_layout(
			yaxis_title='Correlation', barcornerradius=15, xaxis_title=None
		)

		# Create group bar
		bars = []
		for idx, data in df_corr.iterrows():
			name = data['index'] if '|' not in data['index'] else data['index'].split(' | ')[1]	
			name_corr = f"{name} | {round(data['corr'], 2)}"	
			
			bar = go.Bar(
				x=[data['index']], 
				y=[data['corr']], 
				name=f"{name} | {round(data['corr'], 2)}", 
				marker_color=data['color'],
				text=data['corr'],
				hovertemplate=f'{data["variable"]}<br>{name_corr}<extra></extra>'
			)	
			if name == data['variable']:
				bar['legendgroup'] = 'Continuous Variable'
				bar['legendgrouptitle_text'] = 'Continuous Variable'
			else:
				bar['legendgroup'] = data['variable']
				bar['legendgrouptitle_text'] = data['variable']		 
			
			bars.append(bar)
		
		fig_gbar = go.Figure(bars)		
		fig_gbar.update_layout(
            height=600,
			yaxis_title='Correlation', 
			barcornerradius=15,
			xaxis_title=None,
			legend_title='Value | Pearson Correlation',
			title_text=f'Correlation of Features with {col_target.title()}'
		)		

		return fig_bar.update_layout(**layouts), fig_gbar.update_layout(**layouts)
		
	
	@staticmethod
	def plot_bar_event_time_distribution(df, col_event, col_time, use_percent=False, **layouts):	
		event_counts = df.groupby([col_time, col_event]).size().unstack()
		event_counts = event_counts.melt(ignore_index=False).reset_index()
		nbins = event_counts[col_time].nunique()
		
		fig = px.histogram(
			event_counts, 
			y='value', 
			x=col_time, 
			color=col_event, 
			barnorm='percent' if use_percent else None,
			nbins=nbins, 
			text_auto=True
		)
		fig.update_layout(
			legend_traceorder='reversed', 
			barcornerradius=15, 
			bargap=0.1,
			hovermode='x',
			title_text=f"{col_event.title()} Distribution Across Different {col_time.title()}",
			yaxis_title="Percent" if use_percent else "Counts"
		)
		fig.update_traces(hovertemplate=None)

		return fig.update_layout(**layouts)


	@staticmethod
	def plot_event_composition(df, col_event, kind='pie', **layouts):
		"""
		kind: 'pie' or 'bar'
		"""
		counts = df[col_event].value_counts().reset_index()	
		counts['percentage'] = (counts['count'] / df.shape[0] * 100)
		counts['variable'] = col_event
		
		if kind == 'bar':
			fig = px.bar(
				counts,
				y='count',
				x='variable',
				color=col_event,
				title=f"{col_event.title()} Composition",
				text='percentage',
				text_auto=True
			).update_layout(	
				yaxis=dict(title='', showticklabels=False, range=[0, df.shape[0]]),
				xaxis=dict(title='', showticklabels=False),
				legend=dict(x=0.5, xanchor='center', y=0, orientation='h', title=''),
				height=450
			).update_traces(hovertemplate='%{text}%')
		else:
			fig = px.pie(counts, names=col_event, values='count', hole=0.4)
			fig.update_layout(
				legend=dict(x=0.5, xanchor='center', y=0.1, orientation='h', traceorder='reversed'),
				title_text=f"{col_event.title()} Composition"
			).update_traces(hovertemplate='%{value}')
		
		return fig.update_layout(**layouts)


	@staticmethod
	def plot_bar_event_categorical_composition(
		df,
		col_target:str, 
		col_groups:list, 
		chi2stats, 
		value_target=None, 
		order_target:list=None, 
		opacities:list=None, 
		horizontal:bool=False,
		**layouts
	):	
		colors = px.colors.DEFAULT_PLOTLY_COLORS * len(col_groups)
		fig = go.Figure()
		
		for idx, col_group in enumerate(col_groups):
			ct = pd.crosstab(df[col_group], df[col_target])
			ct.columns = ct.columns.map(str) # avoid bug with boolean name
			ct.index = ct.index.map(str) # avoid bug with boolean name			
			sorted_values = ct.sum(axis=1).sort_values(ascending=False)
			ct = ct.loc[sorted_values.index]
			
			chi2 = chi2stats.loc[col_group, 'chi2']
			p = chi2stats.loc[col_group, 'pval']
			
			if order_target is not None:
				order_target = [f'{x}' for x in order_target] # avoid bug with boolean type
				ct = ct.loc[:, order_target]
				color_opacity = [idx/len(order_target) for idx, _ in enumerate(order_target, 1)][::-1]
			else:
				sorted_target = ct.sum().rank(pct=True).sort_values()[::-1]
				ct = ct.loc[:, sorted_target.index]
				color_opacity = sorted_target.to_list()

			if opacities is not None:
				color_opacity = opacities
							
			for value in ct.index:
				x_name = f'{col_group} | {value}'
				val_counts = ct.loc[value]
							
				hovertext = val_counts.index
				hovertext = [f"{val_counts.index.name.title()}: {ht}" for ht in hovertext]
				x, y = [x_name] * val_counts.shape[0], val_counts			
				if horizontal is True:
					x, y = y, x
				
				group_title = f"{col_group} | {round(chi2, 1)} | {round(p, 3)}"

				name = f"{value}"
				if value_target is not None:
					pct_target = (val_counts[f"{value_target}"] / val_counts.sum()) * 100			  
					name = f"{value} ({round(pct_target, 1)}% {col_target}-{value_target})"
				
				hovertemplate = f"Variable: {col_group}<br>"
				hovertemplate += f"Value: {value}<br>"
				hovertemplate += "%{hovertext}<br>"
				if horizontal is True:
					hovertemplate += "Count: %{x}<br><extra></extra>"
				else:
					hovertemplate += "Count: %{y}<br><extra></extra>"
				
				bar = go.Bar(x=x, y=y, name=name)
				bar.update(dict(
					orientation= 'h' if horizontal else 'v',
					marker_color=colors[idx],
					marker_opacity=color_opacity,
					text=val_counts.values,
					hovertext=hovertext,
					hovertemplate=hovertemplate,
					legendgroup=col_group,
					legendgrouptitle_text=group_title
				))
				fig.add_trace(bar)

		fig.update_layout(
			title=f"{col_target.title()} Composition Across Categorical Variables",
			barmode='stack', 
			height=600, 
			legend_groupclick="toggleitem",
			legend_title='Variable | Chi2 | P-value',				
		)
		
		return fig.update_layout(**layouts)