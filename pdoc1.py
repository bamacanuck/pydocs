# pip install docxtpl

import time

from docxtpl import DocxTemplate

doc = DocxTemplate("my_word_template.docx")
context = { 'name' : "Doctor Manhattan",'title' : "manufactured god",'company_name' : "Veidt Industries" }
doc.render(context)
doc.save("generated_doc.docx")

