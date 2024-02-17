from PyPDF2 import PdfReader
import re
import streamlit as st

pdf_path = 'Quiz1.pdf'

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    full_text += page.extract_text() + '\n'


# pattern = re.compile(r'(\d+)\.\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nANS:\s*([ABCD])', re.DOTALL)

pattern = re.compile(r'(\d+)\.\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)\nANS:\s*([ABCD])', re.DOTALL)

matches = pattern.findall(full_text)

data = {}

for match in matches:
    # data['question_number'] = match[0]
    data[match[1].strip()] = {}
    data[match[1].strip()]['options'] = {
        'A': match[2].strip(),
        'B': match[3].strip(),
        'C': match[4].strip(),
        'D': match[5].strip(),
    }
    data[match[1].strip()]['answer'] = match[6]

for i,n in enumerate(data):
    st.write(n)
    options = []
    for m in data[n]['options']:
        if m != 'answer':
            options.append(data[n]['options'][m])
       
    final = st.radio(key=i,label='options',options = options)
    
    if final == data[n]['options'][data[n]['answer']]:
        st.write(':green[correct]')