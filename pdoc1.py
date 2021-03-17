# pip install docxtpl

import time

from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx") # in same directory
context =
    {'name' : "Doctor Manhattan",'title' : "manufactured god",'company_name' : "Mars Corporation"}
    {'name' : "Adrian Veidt",'title' : "self-perfected man",'company_name' : "Veidt Industries"}
    {'name' : "Rhorschach",'title' : "confirmed loser",'company_name' : "the streets, uninc."}
doc.render(context)
doc.save("generated_doc.docx")

