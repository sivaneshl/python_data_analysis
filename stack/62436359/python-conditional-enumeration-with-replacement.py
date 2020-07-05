import pandas as pd
import itertools

fleet_df = pd.DataFrame({'Vehicle_ID': ['001', '002', '003'],
                         'Capacity': [5, 6, 10]})
fleet_df.set_index(['Vehicle_ID'], inplace=True)
total_demand = 55
final_df = pd.DataFrame([])
min_comb = int(total_demand/max(fleet_df['Capacity'].to_list()))
max_comb = int((2*total_demand)/min(fleet_df['Capacity'].to_list()))
for i in range(min_comb, max_comb+1):
    comb_indices = list(com for com in itertools.combinations_with_replacement(fleet_df.index, r=i))
    comb_rows = pd.DataFrame([fleet_df.loc[comb, 'Capacity'].sum() for comb in comb_indices],
                             index=comb_indices, columns=['Total Capacity'])
    final_df = final_df.append(comb_rows[(comb_rows['Total Capacity'] >= total_demand) & (comb_rows['Total Capacity'] <= 2*total_demand)])


final_df = final_df.rename_axis('Vehicle_IDs').reset_index().rename_axis('Scenarios')
print(final_df)