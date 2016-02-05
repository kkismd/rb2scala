#!/bin/sh
for F in *.md; do
  if [ $F = 'README.md' ]; then
    continue
  fi
  echo $F...
  pandoc -f markdown_github $F --filter bin/ymltbl.py -t html5 -o build/_html/__${F%.md}.html
  pandoc -f markdown_github $F --filter bin/ymltbl.py -t html5 -s -o build/html/${F%.md}.html
done
