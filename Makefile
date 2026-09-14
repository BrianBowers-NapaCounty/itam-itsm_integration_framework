.PHONY: html linkcheck release clean
html:
	sphinx-build -b html docs _build/html
linkcheck:
	sphinx-build -b linkcheck docs _build/linkcheck
release:
	python tools/build_release.py
clean:
	rm -rf _build release
