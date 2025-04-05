import os
import json

# Directories (modify these paths as needed)
input_dir = r"PATH\TO\YOUR\INPUT\FOLDER"
output_dir = r"PATH\TO\YOUR\OUTPUT\FOLDER"

# Make sure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# List of notebook filenames without extension
notebooks = ["Notebook1", "Notebook2", "Notebook3"]  # Add your notebook base names here

def fix_widget_metadata(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    widgets = data.get('metadata', {}).get('widgets')
    if widgets:
        widget_data = widgets.get('application/vnd.jupyter.widget-state+json', {})
        if 'state' not in widget_data:
            widget_data['state'] = {}
            print(f"✔️  Added empty 'state' field to: {os.path.basename(input_path)}")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Saved: {output_path}")

# Process each notebook
for name in notebooks:
    input_path = os.path.join(input_dir, name + ".ipynb")
    output_path = os.path.join(output_dir, name + ".ipynb")
    fix_widget_metadata(input_path, output_path)