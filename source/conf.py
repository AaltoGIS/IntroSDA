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


# -- Project information -----------------------------------------------------

import datetime

year = int(datetime.datetime.now().year)

project = 'Introduction to Spatial Analysis'
copyright = f'{year}, Henrikki Tenkanen & Jussi Nikander, Dept. of Built Environment, Aalto University'
author = 'Henrikki Tenkanen & Jussi Nikander'

# -- Course year -------------------------------------------------------------
# Change this one value each year. The GitHub organization name, the exercise
# repository links and the Classroom50 assignment links all follow from it.
# Note: `year` above is the current calendar year (used for the copyright), and
# is not the same thing as the year of the course edition.

course_year = "2026"
classroom_course = "isda"          # Classroom50 course slug, also the repo prefix
noppe_join_code = "hnyp7f87i2rl"   # not derived from the year; update separately

course_org = f"IntroSDA-{course_year}"
_gh = f"https://github.com/{course_org}"
_cr = f"https://classroom50.org/{course_org}/{classroom_course}/assignments"

rst_epilog = f"""
.. |course-year| replace:: {course_year}
.. |course-org| replace:: {course_org}
.. |course-org-url| replace:: `{_gh}/ <{_gh}/>`__
.. |noppe-join-code| replace:: ``{noppe_join_code}``
.. |example-clone-url| replace:: `{_gh}/{classroom_course}-exercise-3-htenkanen.git <{_gh}/{classroom_course}-exercise-3-htenkanen.git>`__
"""

for _n in range(1, 6):
    rst_epilog += (
        f".. |exercise-{_n}-repo| replace:: "
        f"`Exercise {_n} in the course GitHub repository <{_gh}/Exercise-{_n}>`__\n"
        f".. |exercise-{_n}-accept| replace:: "
        f"`accepting the Classroom assignment <{_cr}/exercise-{_n}/accept>`__\n"
    )

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_togglebutton',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'myst_nb',
    #'jupyter_sphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_book_theme'

# Show todos
todo_include_todos = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = 'img/slack-icon.jpg'
html_title = ""

# Custom CSS
#html_css_files = ['custom.css']

html_theme_options = {
    # "external_links": [],
    "repository_url": "https://github.com/AaltoGIS/IntroSDA/",
    "repository_branch": "master",
    "path_to_docs": "source/",
    #"google_analytics_id": "UA-214280609-1",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        "binderhub_url": "https://notebooks.gesis.org/binder",
        "thebe": False,
        "notebook_interface": "jupyterlab",
        "collapse_navigation": False,
        # Google Colab does not provide an easy way for specifying/building/activating the conda environment
        # in a similar manner as Binder. Hence, let's not keep it. The easiest way seems to be:
        # https://github.com/jaimergp/condacolab
        # But it requires actions from the user nontheless, so atm it's a no-go.
        #"colab_url": "https://colab.research.google.com"
    },

    # Possible announcement for the page
   # "announcement": ("📢 Exercises 5 has been added to the course page. 📢"),
}

# Allow errors
execution_allow_errors = True

# Do not execute cells
jupyter_execute_notebooks = "off"
