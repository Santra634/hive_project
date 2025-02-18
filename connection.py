from pyhive import hive
import hive_fns
import analytics
import numpy as np

try:
    c = hive.connect(host='localhost', database='batch89').cursor()
    print('connection established...')
    data_path='/home/santra/data/hive/online_sales_dataset.csv'

    try:
        c.execute(hive_fns.create_table('online_sales', hive_fns.online_sales_columns, sep=','))
        c.execute(hive_fns.insert_data(data_path,'online_sales'))
        print('table created...')

        try:
            c.execute(analytics.analytics_1())
            print(f'no. of transaction for each payment method: {c.fetchall()}')
        except Exception as e:
            print(f'error in analytics_1... {e}')

        try:
            c.execute(analytics.analytics_3())
            avg = c.fetchall()
            print(f'avg shipping cost in each country: {avg}')
        except Exception as e:
            print(f'error in analytics_3... {e}')

    except Exception as e:
        print(f'error in table creation... : {e}')

    c.execute(analytics.analytics_2())
    result = c.fetchall()
    print(f'no of orders in warehouse: {result}')
    x_values = []
    y_values = []
    for i in result:
     if i[0] != '':
      x_values.append(i[0])
      y_values.append(i[1])
    # analytics.plot_bar_graph(x_values,y_values,'orders in each warehouse','warehouse_loc','count')

    print('count of payment methods used in each country:')
    c.execute(analytics.analytics_4())
    c.execute('select distinct country from transaction')
    x_names=c.fetchall()
    print(x_names)
    c.execute('select * from transaction')
    x_values=np.arange(1,len(x_names)+1)
    y_values=c.fetchall()
    bt=[]
    cc=[]
    pp=[]
    for i in y_values:
        if i[1]=='Bank Transfer':
            bt.append(i[2])
        elif i[1]=='Credit Card':
            cc.append(i[2])
        elif i[1]=='paypall':
            pp.append(i[2])
    print(bt)
    print(cc)
    print(pp)

    analytics.graph2(x_values,x_names,bt,cc,pp)


except Exception as e:
    print(f'error in connection: {e}')


