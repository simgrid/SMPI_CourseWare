#!/bin/bash

( set -x ; /bin/rm -rf ./gh-pages )
( set -x ; git clone https://github.com/simgrid/SMPI_CourseWare.git gh-pages; cd gh-pages; git checkout gh-pages; git branch -u origin/gh-pages; cd ..)
( set -x ; jekyll build --source ./site --destination ./gh-pages)
( set -x; cd gh-pages; git add --all .; git commit -a; git push; cd ..)
( set -x; /bin/rm -rf ./gh-pages )
