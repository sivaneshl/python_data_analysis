import pandas as pd

df = pd.DataFrame([['6f8c31653edb8c83e1a739408b5ff750',1,'4244733e06e7ecb4970a6e2683c13e61',
                   '48436dade18ac8b2bce089ec2a041202','2017-08-07 18:55:08', 58.9, 16.17, 'cool_stuff',
                   58.0, 598.0, 4.0, 650.0, 28.0, 9.0, 14.0, 'cool_stuff', '30407a72ad8b3f4df4d15369126b20c9',
                   'delivered', '2017-08-01 18:38:42', '2017-08-01 18:55:08', '2017-08-02 19:07:36',
                   '2017-08-09 21:26:33', '2017-08-25 00:00:00', 27277, 'volta redonda', 'SP',
                   'e7c828d22c0682c1565252deefbe334d', 83070, 'sao jose dos pinhais', 'PR'],
                   ['6f8c31653edb8c83e1a739408b5ff750', 1, '4244733e06e7ecb4970a6e2683c13e61',
                    '48436dade18ac8b2bce089ec2a041202', '2017-08-07 18:55:08', 58.9, 16.17, 'cool_stuff',
                    58.0, 598.0, 4.0, 650.0, 28.0, 9.0, 14.0, 'cool_stuff', '30407a72ad8b3f4df4d15369126b20c9',
                    'delivered', '2017-08-01 18:38:42', '2017-08-01 18:55:08', '2017-08-02 19:07:36',
                    '2017-08-09 21:26:33', '2017-08-25 00:00:00', 27277, 'volta redonda', 'SP',
                    'e7c828d22c0682c1565252deefbe334d', 83070, 'sao jose dos pinhais', 'PR'],
                   ['6f8c31653edb8c83e1a739408b5ff750', 1, '4244733e06e7ecb4970a6e2683c13e61',
                    '48436dade18ac8b2bce089ec2a041202', '2017-08-07 18:55:08', 58.9, 16.17, 'cool_stuff',
                    58.0, 598.0, 4.0, 650.0, 28.0, 9.0, 14.0, 'cool_stuff', '30407a72ad8b3f4df4d15369126b20c9',
                    'delivered', '2017-08-01 18:38:42', '2017-08-01 18:55:08', '2017-08-02 19:07:36',
                    '2017-08-09 21:26:33', '2017-08-25 00:00:00', 27277, 'sao jose dos pinhais', 'SP',
                    'e7c828d22c0682c1565252deefbe334d', 83070, 'volta redonda', 'PR']
                   ],
                  columns=
                  ['order_id','order_item_id','product_id','seller_id','shipping_limit_date','price','freight_value',
                   'product_category_name','product_name_lenght','product_description_lenght','product_photos_qty',
                   'product_weight_g','product_length_cm','product_height_cm','product_width_cm','product_category_name_english',
                   'customer_id','order_status','order_purchase_timestamp','order_approved_at','order_delivered_carrier_date',
                   'order_delivered_customer_date','order_estimated_delivery_date','seller_zip_code_prefix','seller_city',
                   'seller_state','customer_unique_id','customer_zip_code_prefix','customer_city','customer_state'])

print(df[['seller_city','customer_city']])
print(df.groupby((df['seller_city'] + '-' + df['customer_city'])).size())