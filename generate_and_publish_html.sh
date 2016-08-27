#!/bin/bash
#
# This script should be executed on a checkout of the master branch and it:
#   - creates a gh-pages directory
#   - does a check out of the gh-pages branch in that directory
#   - runs jekyll to generate content into the gh-pages directory
#   - pushes the changes to the gh-pages branch
#   - the gh-branch content is magically seen at: https://simgrid.github.io/SMPI_CourseWare/

( set -x ; /bin/rm -rf /tmp/gh-pages )
( set -x ;\
  cd /tmp;\
  git clone --depth 1 --branch gh-pages git@github.com:simgrid/SMPI_CourseWare.git SMPI_CourseWare;\
  cd SMPI_CourseWare;\
  git branch -u origin/gh-pages; )
( set -x ; jekyll build --source . --destination /tmp/SMPI_CourseWare; )
( set -x; cd /tmp/SMPI_CourseWare; git add --all .; git commit -a -m "Re-generating HTML"; git push; )
( set -x; /bin/rm -rf /tmp/gh-pages; )
