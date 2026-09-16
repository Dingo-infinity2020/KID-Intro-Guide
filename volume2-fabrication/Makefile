CH ?= ch00_overview
BUILD := build

.PHONY: full chapter clean

full:
	@mkdir -p $(BUILD)
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex

chapter:
	@mkdir -p $(BUILD)
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(CH) -output-directory=$(BUILD) "\\def\\ChapterFile{chapters/$(CH)}\\input{chapter-preview.tex}"
	xelatex -interaction=nonstopmode -halt-on-error -jobname=$(CH) -output-directory=$(BUILD) "\\def\\ChapterFile{chapters/$(CH)}\\input{chapter-preview.tex}"

clean:
	rm -rf $(BUILD)
