from PyPDF2 import PdfMerger   


merger=PdfMerger()
merger.append("firstpdf.pdf")
merger.append("secondpdf.pdf")
merger.write("mergerpdffiles.pdf") 

#merge pdf files into pages
merger2=PdfMerger()
merger.append("firstpdf.pdf")
merger.merge(2,"secondpdf.pdf")  # added the second pdf file to the third page of the first pdf file
merger.write("mergerpdffiles2.pdf") 
