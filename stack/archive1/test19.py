import pandas as pd
import numpy as np
import re

partenaire=pd.DataFrame([['some false address 12345',12],
                         ['whatever other address 67890 here',45],
                         ['and more 34567 here',43],
                         ['and even more 54321 then',54]],
                        columns=['Adresse','basecodeclub'])

partenaire['topcodeclub'] = ''
for id, i in enumerate(partenaire.Adresse):
    i = str(i)
    r1 = re.findall(r"\d{5}",i)
    print(r1, partenaire.basecodeclub[id], r1[0][:2])
    partenaire['topcodeclub'] = 'True' if int(r1[0][:2])==partenaire.basecodeclub[id] else 'False'

print(partenaire)