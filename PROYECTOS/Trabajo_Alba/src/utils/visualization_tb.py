



def show_pie(df, figsize=(15, 15), subplots=True, autopct = '%1.1f%%', legend=None, title=None, **argumentos_extra):
    return df.plot.pie( figsize=figsize,subplots=subplots, autopct = autopct, legend=legend, title=title, **argumentos_extra)


def show_bar(df, figsize=(15, 15), subplots=True, autopct = '%1.1f%%', legend=None, title=None, **argumentos_extra):
    return df.plot.bar( figsize=figsize,subplots=subplots, autopct = autopct, legend=legend, title=title, **argumentos_extra)



