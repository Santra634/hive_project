# 1. which payment have more transactions



def analytics_1():
    query='''select payment_method,count(*) as no_of_transaction from online_sales group by payment_method order by no_of_transaction desc'''
    return query

def analytics_2():
    query='''select warehouse_loc,Count(*) as count from online_sales group by warehouse_loc'''
    return query

import matplotlib.pyplot as plt
def plot_bar_graph(x,y,title,xaxis,yaxis):
    plt.bar(x,y,color='b')
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.show()

def analytics_3():
    query='''select country,avg(shipping_cost) as avg_shipping_cost from online_sales group by country order by avg_shipping_cost desc'''
    return query

def analytics_4():
    query='''create table if not exists transaction as select country,payment_method,count(*) as count from online_sales group by country,payment_method'''
    return query

def graph2(x_values,x_names,y1,y2,y3):
    bar_width=0.25
    plt.bar(x_values-bar_width,y1,bar_width,color='yellow',label='banktransfer')
    plt.bar(x_values,y2,bar_width,color='red',label='creditcard')
    plt.bar(x_values+bar_width,y3,bar_width,color='black',label='paypall')
    plt.xticks(x_values,x_names)
    plt.legend()
    plt.show()
