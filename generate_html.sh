#!/bin/bash
#
# This script should be executed on a checkout of the master branch and it:
#   - creates a gh-pages directory
#   - does a check out of the gh-pages branch in that directory
#   - runs jekyll to generate content into the gh-pages directory
#   - pushes the changes to the gh-pages branch
#   - the gh-branch content is magically seen at: https://simgrid.github.io/SMPI_CourseWare/

( set -x ; /bin/rm -rf ./gh-pages )
( set -x ; git clone https://github.com/simgrid/SMPI_CourseWare.git gh-pages; cd gh-pages; git checkout gh-pages; git branch -u origin/gh-pages; cd ..)
( set -x ; jekyll build --source ./site --destination ./gh-pages)
( set -x; cd gh-pages; git add --all .; git commit -a; git push; cd ..)
( set -x; /bin/rm -rf ./gh-pages )
