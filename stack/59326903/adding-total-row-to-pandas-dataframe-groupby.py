import pandas as pd

df = pd.DataFrame({'case_type':['Service']*20+['chargeback']*9,
                   'claim_type':['service']*5+['local_charges']*5+['service_not_used']*5+['supplier_service']*5+['service']*8+['local_charges']})

df_out = df.groupby(by=["case_type", "claim_type"])["case_type"].count()

print(df_out)
print(type(df_out))

print(pd.concat([df_out.to_frame(),
           df_out.sum(level=0).to_frame()
                 .assign(claim_type= "total")
                 .set_index('claim_type', append=True)])
  .sort_index())


