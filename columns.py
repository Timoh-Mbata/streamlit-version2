import json
file = r'C:\\Users\\user\\Desktop\\streamlit\\streamlit_version2\\columns.json'
with open(file,'r') as column:
    col = json.load(column)

print(col)