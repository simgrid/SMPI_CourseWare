#!/bin/bash
#
# This script should be executed on a checkout of the master branch and it:
#   - creates a gh-pages directory
#   - does a check out of the gh-pages branch in that directory
#   - runs jekyll to generate content into the gh-pages directory
#   - pushes the changes to the gh-pages branch
#   - the gh-branch content is magically seen at: https://simgrid.github.io/SMPI_CourseWare/

TARGETDIR=/tmp/SMPI_CourseWare

( set -x ; /bin/rm -rf $TARGETDIR )
( set -x ;\
  cd /tmp;\
  git clone --depth 1 --branch gh-pages git@github.com:simgrid/SMPI_CourseWare.git $TARGETDIR;\
  cd $TARGETDIR;\
  git branch -u origin/gh-pages; )
( set -x ; jekyll build --source . --destination $TARGETDIR; )
( set -x; cd $TARGETDIR; git add --all .; git commit -a -m "Re-generating HTML"; git push; )
( set -x; /bin/rm -rf $TARGETDIR; )
