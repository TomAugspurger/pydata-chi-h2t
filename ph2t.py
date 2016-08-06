import pandas as pd
from IPython.display import HTML


def side_by_side(df1, df2, name1='', name2=''):
    if isinstance(df1, pd.Series):
        df1 = df1.to_frame(name=df1.name)
    if isinstance(df2, pd.Series):
        df2 = df2.to_frame(name=df2.name)
    inline = 'style="display: float; max-width:50%" class="table"'
    q = '''
    <div class="table-responsive col-md-6">{}</div>
    <div class="table-responsive col-md-6">{}</div>
    '''.format(df1.style.set_table_attributes(inline)
                  .set_caption(name1).render(),
               df2.style.set_table_attributes(inline)
                  .set_caption(name2).render())
    return HTML(q)
