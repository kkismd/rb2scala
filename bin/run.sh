#!/bin/sh
for F in *.md; do
  case $F in
    "README.md" ) continue
      ;;
    "index.md" ) tocopt=""
      ;;
    * ) tocopt="--toc --toc-depth=2"
      ;;
  esac

  echo $F...
  pandoc -f markdown_github $F --filter bin/ymltbl.py -t html5 -o build/_html/__${F%.md}.html
  pandoc -f markdown_github+header_attributes $F --filter bin/ymltbl.py -t html5 -s $tocopt -c css/style.css -o build/html/${F%.md}.html
done

cp css/*.css build/html/css
