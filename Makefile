.PHONY: pdf clean

pdf:
	bash ./scripts/build_latest.sh

clean:
	find docs -type f \( -name '*.aux' -o -name '*.log' -o -name '*.out' -o -name '*.toc' -o -name '*.synctex.gz' \) -delete
