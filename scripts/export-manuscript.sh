#!/bin/bash
# Export manuscript to docx/epub/pdf, stripping notes
# Usage: ./scripts/export-manuscript.sh [format]
# Formats: docx (default), epub, pdf

set -e

FORMAT="${1:-docx}"
OUTPUT="manuscript.${FORMAT}"
TEMP=$(mktemp)

# Strip blockquote lines (notes) and clean up excess blank lines
sed '/^>/d' manuscript.md | cat -s > "$TEMP"

# Convert with pandoc
REFDOC=""
if [ -f reference.docx ] && [ "$FORMAT" = "docx" ]; then
  REFDOC="--reference-doc=reference.docx"
fi

pandoc "$TEMP" \
  -f markdown \
  -o "$OUTPUT" \
  --resource-path=. \
  --toc \
  --toc-depth=1 \
  --top-level-division=chapter \
  $REFDOC

rm "$TEMP"
echo "Exported to $OUTPUT"
