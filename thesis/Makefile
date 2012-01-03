TEX=pdflatex
BIBTEX=bibtex
DOC=thesis.tex
SOURCES=sources.bib
BIBDOC=thesis

all: $(DOC) $(SOURCES)
	$(TEX) $(DOC)
	$(BIBTEX) $(BIBDOC)
	$(TEX) $(DOC)
	$(TEX) $(DOC)

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg
