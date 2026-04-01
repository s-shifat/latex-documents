# Makefile for LaTeX report with biblatex + biber

# Main document name (without extension)
MAIN = main

# Default target
all: $(MAIN).pdf

# Build PDF with proper LaTeX -> Biber -> LaTeX -> LaTeX sequence
$(MAIN).pdf: $(MAIN).tex $(MAIN).bcf references.bib
	pdflatex $(MAIN)
	biber $(MAIN)
	pdflatex $(MAIN)
	pdflatex $(MAIN)

# bcf file is created by the first LaTeX run
$(MAIN).bcf: $(MAIN).tex
	pdflatex $(MAIN)

# Convenience target
pdf: all

# Clean auxiliary files
clean:
	rm -f \
		$(MAIN).aux \
		$(MAIN).bbl \
		$(MAIN).bcf \
		$(MAIN).blg \
		$(MAIN).log \
		$(MAIN).run.xml \
		$(MAIN).toc \
		$(MAIN).out \
		$(MAIN).lof \
		$(MAIN).lot \
		$(MAIN).fls \
		$(MAIN).fdb_latexmk

# Clean everything including the PDF
cleanall: clean
	rm -f $(MAIN).pdf

.PHONY: all pdf clean cleanall

