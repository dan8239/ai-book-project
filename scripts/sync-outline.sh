#!/bin/bash
# Sync Google Sheet outline to CSV for version control
# Run this at end of session: ./scripts/sync-outline.sh

SHEET_ID="1N8DdsXJxRHvBXT1OhOviCNYx9wbZg1XJWgqIBlJihqc"
OUTPUT_FILE="structure/outline.csv"

echo "Exporting Google Sheet to CSV..."

# Use Google Sheets export URL (public or shared sheets)
curl -sL "https://docs.google.com/spreadsheets/d/${SHEET_ID}/export?format=csv" -o "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "✓ Exported to $OUTPUT_FILE"

    # Show what changed
    git diff --stat "$OUTPUT_FILE" 2>/dev/null

    echo ""
    echo "To commit: git add $OUTPUT_FILE && git commit -m 'Update outline'"
else
    echo "✗ Export failed. Make sure sheet is shared (Anyone with link can view)"
fi
