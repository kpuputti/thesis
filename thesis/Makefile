TEX=pdflatex
BIBTEX=bibtex
DOC=thesis.tex
DOC_FILES=aalto-thesis.sty introduction.tex research-question.tex methods.tex results.tex discussion.tex test.tex gitinfo.py
SOURCES=sources.bib
BIBDOC=thesis
OUTPUT=thesis.pdf

$(OUTPUT): $(DOC) $(DOC_FILES) $(SOURCES)
	python gitinfo.py > gitinfo.tex
	$(TEX) $(DOC)
	$(BIBTEX) $(BIBDOC)
	$(TEX) $(DOC)
	$(TEX) $(DOC)

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg
