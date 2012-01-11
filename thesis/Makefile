TEX=pdflatex
BIBTEX=bibtex
DOC=thesis.tex
DOC_FILES=*.sty *.tex *.bib gitinfo.py images/*
BIBDOC=thesis
OUTPUT=thesis.pdf

$(OUTPUT): $(DOC) $(DOC_FILES)
	python gitinfo.py > gitinfo.tex
	$(TEX) $(DOC)
	$(BIBTEX) $(BIBDOC)
	$(TEX) $(DOC)
	$(TEX) $(DOC)

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg
