# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Thinqat's Blog"
copyright = "2025, Thinqat"
author = "Thinqat"
html_static_path = ["_static"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Thinqat's Blog"
html_favicon = "_static/favicon.png"
html_theme = "conestack"
html_theme_options = {
    "logo_url": "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Food/Teacup%20Without%20Handle.png",
    "logo_title": "Thinqat's Blog",
    "logo_width": "40px",
    "logo_height": "40px",
    "github_url": "https://github.com/Thinqat1985731?tab=repositories",
}
post_date_format = "%Y-%m-%d"
