# Fix Kindle Clipings and Convert them to Markdown

This tool fixes redundant clippings by checking page and location overlap. 
In the case of overlap, last clipping is only saved.

The tool also converts to markdown format, so you can easily upload to Notion or
wherever you want.

# Sample Usage

`python kindle.py -i clippings.txt -o clean.md`

Here is an sample output:

```
# Clips

- Page 13 loc 194-208 

    In studying world history, I also traced a number of intellectual traditions...
```
