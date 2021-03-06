# run bibtex2html

import subprocess
import os

def call_fail(l):
    if subprocess.call(l) != 0:
        print "{} failed".format(" ".join(l))
        exit(1)

bibtex2html_command = ["bibtex2html", "-d",
                       "-nokeys", "--no-abstract",
                       "-nodoc", "-noheader",
                       "-nofooter", "-nokeywords", "soundinessrefs.bib"]

def get_pub_html():
    # run bibtex2html
    # need this env var for mac
    os.putenv("TMPDIR",".")
    call_fail(bibtex2html_command)
    # read in generated HTML
    with open("soundinessrefs.html", "r") as p:
        data = p.read()
    # delete generated file
    os.remove("soundinessrefs.html")
    return data

pubs = get_pub_html()

header = """<!DOCTYPE html>
<html>

  <head>
    <meta charset='utf-8' />
    <meta http-equiv="X-UA-Compatible" content="chrome=1" />
    <meta name="description" content="Soundiness home page : " />

    <link rel="stylesheet" type="text/css" media="screen" href="stylesheets/stylesheet.css">

    <title>Soundiness home page</title>
    <style>
      table,td,tr { border-style:none;}
    </style>
  </head>

  <body>
    <!-- HEADER -->
    <div id="header_wrap" class="outer">
        <header class="inner">
          <a id="forkme_banner" href="https://github.com/soundiness">View on GitHub</a>

          <h1 id="project_title">Soundiness home page</h1>
          <h2 id="project_tagline"></h2>

        </header>
    </div>

    <!-- MAIN CONTENT -->
    <div id="main_content_wrap" class="outer">
      <section id="main_content" class="inner">
      <h1>Soundiness bibliography</h1>

      <p>This is an initial bibliography of papers related to the theme of soundiness.  We aim to list papers that either (1) measure the unsoundness of whole-program analyses in some way, (2) give solutions to analyzing "hard" language features, or (3) measure the utility of soundness in a particular context.  If you have further suggestions for references, submit an <a href="https://github.com/soundiness/soundiness.github.io/issues">issue</a> or a <a href="https://github.com/soundiness/soundiness.github.io/pulls">pull request</a>.</p><hr/>
"""

footer = """
      </section>
    </div>

    <!-- FOOTER  -->
    <div id="footer_wrap" class="outer">
      <footer class="inner">
        <p>Published with <a href="http://pages.github.com">GitHub Pages</a></p>
      </footer>
    </div>

    

  </body>
</html>
"""

page = header + pubs + footer

with open("biblio.html", "w") as output:
    output.write(page)

