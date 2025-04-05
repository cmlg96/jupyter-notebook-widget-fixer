# 🛠️ Jupyter Widget Metadata Fixer

A lightweight Python script to **repair broken Jupyter Notebooks** that throw widget-related metadata errors during rendering or conversion.

> 💡 Especially useful for fixing errors like:
>
> ```
> Invalid Notebook: the 'state' key is missing from 'metadata.widgets'
> ```

---

## 🚀 What It Does

This script scans `.ipynb` files and checks for incomplete widget metadata. If the `state` key is missing under `metadata.widgets`, it automatically adds an empty `state` to prevent issues with:

- `nbconvert` errors
- Jupyter Notebook rendering failures
- Broken interactive widgets (`ipywidgets`)

---

## 🧩 Why It Matters

Many notebooks that include widgets get corrupted when saved or exported, especially via external tools or cloud editors. This script ensures they're **safe to render and convert again** — no more manual JSON editing.

---

## ⚙️ How to Use

1. **Clone or download** this repository.
2. Edit the script:
   - Set your **input folder** (where your `.ipynb` files are)
   - Set your **output folder** (where fixed files will be saved)
   - List the notebook filenames to process
3. Run the script:

```bash
python fix_widgets.py
