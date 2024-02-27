from xhtml2pdf import pisa
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sourceHtml = open(os.path.join(base_dir, 'D:/ejemplo certificado/nuevohtml.html')).read()
outputFilename = "test.pdf"
def convertHtmlToPdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")
    pisaStatus = pisa.CreatePDF(
            sourceHtml,
            dest=resultFile)
    resultFile.close()
    return pisaStatus.err
if __name__=="__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)