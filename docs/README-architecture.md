How to export `architecture.drawio` to a high-fidelity PNG

1. Open `docs/architecture.drawio` in VS Code using the Draw.io extension or open with draw.io desktop.
2. Adjust the canvas size to a large resolution (recommended width: 1800-2400 px).
3. Set background to transparent or white depending on slide design.
4. File -> Export as PNG. Recommended settings:
   - Scale: 2x or 3x (for high DPI)
   - DPI: 300
   - Include background: yes
   - Include shadow: as needed
5. Save/export to the repository path: `docs/architecture.png` (overwrite existing file).
6. Commit and push the change, or notify the Team Lead to trigger rebuild.

If you prefer automation via PowerShell (Windows):
- After exporting manually to a temporary path, run (from repo root):

```powershell
Copy-Item -Path "C:\Users\CloudEng\Downloads\architecture_export.png" -Destination "docs\architecture.png" -Force
```

When done, notify the team so we can rebuild the deck and re-commit the final PDF.