



def show_pie(df, figsize=(15, 15), subplots=True, autopct = '%1.1f%%', legend=None, title=None, **argumentos_extra):
    return df.plot.pie( figsize=figsize,subplots=subplots, autopct = autopct, legend=legend, title=title, **argumentos_extra)

vu.show_pie(pie_data, title="Paro por distrito")


def show_bar( plt.rcParams["figure.figsize"] = [15, 10], index=None, ax = sns.barplot(y=None, x = None, data = None, palette=("BuGn_r")),
fig.set_size_inches(30, 30), plt.xticks(rotation=84)):
    return 
