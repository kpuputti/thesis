TEX=pdflatex
BIBTEX=bibtex
DOC=thesis.tex
DOC_FILES=aalto-thesis.sty
SOURCES=sources.bib
BIBDOC=thesis
OUTPUT=thesis.pdf

$(OUTPUT): $(DOC) $(DOC_FILES) $(SOURCES)
	$(TEX) $(DOC)
	$(BIBTEX) $(BIBDOC)
	$(TEX) $(DOC)
	$(TEX) $(DOC)

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg
