import pandas as pd


lines= [[1006,1006,1006,1006,1006],
        [96,96,98,98,97],
        [90,89,92,92,90],
        [87,88,89,88,88],
        [87,87,89,88,88]]

ref=pd.DataFrame(lines, columns=[317.00, 319.00, 321.00, 323.00, 325.00])
print(ref)
finalref = pd.DataFrame(ref.mean().to_dict(),index=[ref.index.values[-1]])
print(finalref)

