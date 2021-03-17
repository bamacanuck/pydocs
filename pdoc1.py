# pip install docxtpl

import time

from docxtpl import DocxTemplate

doc = DocxTemplate("my_word_template.docx")
context = { 'company_name' : "World Company" }
doc.render(context)
doc.save("generated_doc.docx")

