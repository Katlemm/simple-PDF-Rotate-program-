import PyPDF2

fileLocation = input("Welches Dokument soll gedreht werden?\n Bitte richtigen Pfad mit dem DokumentNamen.pdf angeben\n")
fileLocation = fileLocation.replace("\\", "/")
pdfIn = open(fileLocation, 'rb') # exchange the 'original.pdf' with a name of your file 
pdfReader = PyPDF2.PdfFileReader(pdfIn)
pdfWriter = PyPDF2.PdfFileWriter()

while True:
    rotate = input("Wie möchtest du rotieren?\n1 für 90 Grad RECHTS\n2 für 90 Grad LINKS\n3 für 180 Grad\n")

    if rotate == "1":
        for pageNum in range(pdfReader.numPages):
            page = pdfReader.getPage(pageNum)
            page.rotateClockwise(90)
            pdfWriter.addPage(page)
        break
    if rotate == "2":
        for pageNum in range(pdfReader.numPages):
            page = pdfReader.getPage(pageNum)
            page.rotateCounterClockwise(90)
            pdfWriter.addPage(page)
        break
    if rotate == "3":
        for pageNum in range(pdfReader.numPages):
            page = pdfReader.getPage(pageNum)
            page.rotateClockwise(180)
            pdfWriter.addPage(page)
        break     
    
    print("Falsche Eingabe! Versuchs Nochmal")


fileName = input("Wie soll der Dateiname sein? Nicht .pdf vergessen!\n")

pdfOut = open(fileName, 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()

#input("Welches Dokument soll gedreht werden?\n Bitte richtigen Namen mit .pdf angeben\n")