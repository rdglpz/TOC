# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OOTOC'
copyright = '2024, S. Ivvan Valdez'
author = 'S. Ivvan Valdez'
release = 'V.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_automodapi.automodapi']

autodoc_member_order = 'groupwise'
# toc_object_entries_show_parents = 'all'
templates_path = ['_templates']
exclude_patterns = []


# extensions = ['sphinx_automodapi.automodapi',
#               'sphinx_automodapi.smart_resolver']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'cloud'
html_static_path = ['_static']

# ADDITIONAL_PREAMBLE = """
# \setcounter{tocdepth}{3}
# """

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',
# Additional stuff for the LaTeX preamble.
'preamble': '\setcounter{tocdepth}{5}'

#'preamble': ADDITIONAL_PREAMBLE
}


