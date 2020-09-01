



def show_pie(df, figsize=(15, 15), subplots=True, autopct = '%1.1f%%', legend=None, title=None, **argumentos_extra):
    return df.plot.pie( figsize=figsize,subplots=subplots, autopct = autopct, legend=legend, title=title, **argumentos_extra)



def show_bar(df, title, x, y, palette, plt, sns, figsize=[20, 10], xticks_rotation=None):
    plt.rcParams["figure.figsize"] =figsize
    if  xticks_rotation is not None:
        plt.xticks(rotation=xticks_rotation)

    ax = sns.barplot(y= y, x = x, data = df ,palette=palette)
    ax.set_title(title)
