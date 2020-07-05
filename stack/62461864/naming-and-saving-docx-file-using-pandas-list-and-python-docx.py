from docx import Document
import pandas as pd

df = pd.read_excel(open('test.xlsx','rb'))
for name in df.Names:
    print(name)
    document = Document()
    document.save(str(name)+'.docx')