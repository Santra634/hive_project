def create_table(tablename,col_info,sep):
    table=f'''create table if not exists {tablename} ({col_info}) row format delimited fields terminated by '{sep}' tblproperties('skip.header.line.count'='1')'''
    return table
online_sales_columns='''invoice_no bigint,stock_code string,description string,qty int,invoice_dte string,price float,cust_id float,country string,discount float,payment_method string,shipping_cost float,category string,sales_channel string,return_status string,shipment_provider string,warehouse_loc string,order_priority string'''

def insert_data(path,table_name):
    data=f'''load data local inpath '{path}' overwrite into table {table_name}'''
    return data