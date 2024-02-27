import jinja2
import pdfkit
##import aspose.words as aw
##from weasyprint import HTML
#def generarpdf():
  #  doc = aw.Document("nuevohtml.html")
   # doc.save("Output.pdf")
 #  HTML('nuevohtml.html').write_pdf('ejemplo.pdf')
    
    
def crear_pdf(ruta_template,info,rutacss=''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    # Agregar estilo para orientación horizontal
    html = '<style>@page { size: landscape; }</style>' + html

    option = {
        'page-size': 'letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'enconding': 'UTF-8'
    }

    print(html)

    f = open('nuevohtml.html', 'w')
    f.write(html)
    f.close()
    
    #config=pdfkit.configuration(wkhtmltopdf='D:/wkhtmltopdf/bin/wkhtmltopdf')
    #ruta_salida='C:/Users/gabriel/Desktop/ejemplo certificado/prueba.pdf'
    #pdfkit.from_string(html,ruta_salida,css=rutacss,options=option,configuration=config)
    
if __name__=="__main__":
    ruta_template='D:/ejemplo certificado/template.html'
    info={"nombreAlumno":"gabriel sánchez","cursoTomado":"prueba niño","nombreAcademia":"gabware"}
    crear_pdf(ruta_template,info)
    ##generarpdf()