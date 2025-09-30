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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'papers'
# copyright = '2021, ashibaga'
author = 'ashibaga'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ "myst_nb", "sphinxcontrib.pseudocode", "sphinx.ext.githubpages"]

# sphinx_to_github = True
# sphinx_to_github_verbose = True
# sphinx_to_github_encoding = "utf-8"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = [".rst", ".md"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints', 'html', 'build', 'jupyter_execute']


# -- Options for HTML output -------------------------------------------------

sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'bootstrap'
html_show_copyright = False

html_theme_options = {
  'bootswatch_theme': "simplex",

  'navbar_title': "ashibaga",

  # Tab name for entire site. (Default: "Site")
  # 'navbar_site_name': "Atsushi Shibagaki",

  # A list of tuples containing pages or urls to link to.
  # Valid tuples should be in the following forms:
  #    (name, page)                 # a link to a page
  #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
  #    (name, "http://example.com", True) # arbitrary absolute url
  # Note the "1" or "True" value above as the third argument to indicate
  # an arbitrary url.
  # 'navbar_links': [
  #     ("Examples", "examples"),
  #     ("Link", "http://example.com", True),
  # ],

  # Render the next and previous page links in navbar. (Default: true)
  'navbar_sidebarrel': True,

  # Render the current pages TOC in the navbar. (Default: true)
  'navbar_pagenav': True,

  # Tab name for the current pages TOC. (Default: "Page")
  'navbar_pagenav_name': "Page",

  # Global TOC depth for "site" navbar tab. (Default: 1)
  # Switching to -1 shows all levels.
  'globaltoc_depth': 2,

  # Include hidden TOCs in Site navbar?
  #
  # Note: If this is "false", you cannot have mixed ``:hidden:`` and
  # non-hidden ``toctree`` directives in the same page, or else the build
  # will break.
  #
  # Values: "true" (default) or "false"
  'globaltoc_includehidden': "true",

  # HTML navbar class (Default: "navbar") to attach to <div> element.
  # For black navbar, do "navbar navbar-inverse"
  # 'navbar_class': "navbar navbar-inverse",

  # Fix navigation bar to top of page?
  # Values: "true" (default) or "false"
  # 'navbar_fixed_top': "true",

  # Location of link to source.
  # Options are "nav" (default), "footer" or anything else to exclude.
  'source_link_position': "fotter",

  # Bootswatch (http://bootswatch.com/) theme.
  #
  # Options are nothing (default) or the name of a valid theme
  # such as "amelia" or "cosmo".

  # Choose Bootstrap version.
  # Values: "3" (default) or "2" (in quotes)
  # 'bootstrap_version': "3",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

