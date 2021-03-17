# pip install docxtpl

import time

from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx") # in same directory
context = { 'name' : "Doctor Manhattan",'title' : "manufactured god",'company_name' : "Veidt Industries" }
doc.render(context)
doc.save("generated_doc.docx")

