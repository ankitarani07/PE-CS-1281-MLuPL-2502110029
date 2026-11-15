IT10: Standard · README & TidyInstead of manually dragging files around to tidy your repo, write a quick Python scaffolding script that acts as an automated broom to sweep your workshop and enforce the sensible layout (src/, data/, reports/).   Pythonimport os
import shutil
from pathlib import Path

def tidy_workshop():
    """Automates the repo sweep and creates a sensible layout."""
    folders = ["src", "data", "reports"]
    
    # Create sensible layout
    for folder in folders:
        Path(folder).mkdir(exist_ok=True)
        
    # Example: Move all .py files to src/ automatically
    for file in Path('.').glob('*.py'):
        if file.name != "tidy.py": # Don't move the script currently running
            shutil.move(str(file), f"src/{file.name}")
            
    print("Workshop swept. Dead code should be deleted via `git rm`.")

if __name__ == "__main__":
    tidy_workshop()
    The "Operator's Manual" README format:
Rather than a standard README, format it like a piece of industrial equipment documentation:

Markdown
# 🏭 The Batch Inspector (v1.0)
**Purpose:** Automates the parsing, sorting, and reporting of shop floor diameter logs.

## 🗂️ Sensible Layout
- `/src`: The engine (Python logic).
- `/data`: The raw materials (Requires `sample_input.txt` to run immediately).
- `/reports`: The finished goods (Output `.csv` and `.txt` files).

## 🧹 Maintenance
All experimental dead code has been swept from this repository to maintain a clean workshop[cite: 8].
    
