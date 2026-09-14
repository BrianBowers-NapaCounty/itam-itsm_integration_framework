from pathlib import Path
project = "Capybara Framework"
author = "Team Capybara"
copyright = "2026, Team Capybara"
version = "1.0"
release = "1.0.0-rc3"
extensions = ["myst_parser", "sphinx.ext.autosectionlabel"]
autosectionlabel_prefix_document = True
source_suffix = {".rst":"restructuredtext", ".md":"markdown"}
root_doc = "index"
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "tasklist", "attrs_block", "attrs_inline"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_legacy_original_source/**", "_legacy_downloads/**", "_audit/**"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["capybara.css", "rc3-additions.css"]
html_logo = "_static/capybara-logo.png"
html_favicon = "_static/favicon.ico"
html_show_sourcelink = True
html_copy_source = True
html_title = "Capybara – Original Edition 1.0.0"
html_theme_options = {"logo_only": False, "navigation_depth": 4, "collapse_navigation": False}
epub_title = project
epub_author = author
epub_show_urls = "footnote"
latex_engine = "xelatex"
latex_documents = [("index", "capybara-framework.tex", "Capybara Framework", author, "manual")]
latex_elements = {"papersize":"letterpaper", "pointsize":"10pt"}


# ---------------------------------------------------------------------
# CAPYBARA_RC3_LATEX_EMPTY_TABLE_GUARD
#
# Sphinx 8.2.x LaTeXFootnoteVisitor.depart_table() assumes every table
# contains a tbody and calls next(node.findall(nodes.tbody)) without a
# default. Header-only tables can legitimately lack tbody, causing
# StopIteration during RTD's PDF build.
#
# Preserve the table and supply an empty tbody before the built-in
# transform handles it.
# ---------------------------------------------------------------------

try:
    from docutils import nodes as _capybara_docutils_nodes
    from sphinx.builders.latex.transforms import (
        LaTeXFootnoteVisitor as _CapybaraLaTeXFootnoteVisitor,
    )

    _capybara_original_depart_table = (
        _CapybaraLaTeXFootnoteVisitor.depart_table
    )

    def _capybara_safe_depart_table(self, node):

        tbody = next(
            node.findall(_capybara_docutils_nodes.tbody),
            None,
        )

        if tbody is None:

            tgroup = next(
                node.findall(_capybara_docutils_nodes.tgroup),
                None,
            )

            if tgroup is not None:
                tgroup += _capybara_docutils_nodes.tbody()
            else:
                # No normal table structure exists. There is nowhere
                # appropriate to place table footnotes.
                self.table_footnotes = []
                return

        return _capybara_original_depart_table(self, node)

    _CapybaraLaTeXFootnoteVisitor.depart_table = (
        _capybara_safe_depart_table
    )

except Exception:
    # HTML/EPUB builds must not be affected if the LaTeX builder is
    # unavailable in another Sphinx environment.
    pass

