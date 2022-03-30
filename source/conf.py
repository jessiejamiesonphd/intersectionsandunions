# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

mathjax_path="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"

# -- Project information -----------------------------------------------------

project = 'Intersections and Unions'
copyright = '2022, Jessie D. Jamieson, PhD'
author = 'jessiejamiesonphd'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
"ablog",
"sphinx.ext.intersphinx",
"sphinx.ext.mathjax",
"sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["README.md", "Pipfile", "Pipfile.lock", "Makefile", "make.bat", "logo.gif", "conf.py"]

blog_post_pattern = "posts/*.rst"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# LaTeX options

latex_engine = 'pdflatex'
latex_elements = {
    'fontpkg': r'''
\\setmainfont{DejaVu Serif}
\\setsansfont{DejaVu Sans}
\\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\\usepackage[titles]{tocloft}
\\usepackage{amssymb}
\\usepackage{amsmath}
\\cftsetpnumwidth {1.25cm}\\cftsetrmarg{1.5cm}
\\setlength{\\cftchapnumwidth}{0.75cm}
\\setlength{\\cftsecindent}{\\cftchapnumwidth}
\\setlength{\\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\\footnotesize\\raggedright\\printindex'
}
latex_show_urls = 'footnote'