# converttomd.py - Markdown Conversion

```python
import os

source_folder = "D:\Jobs\Kenya\Frank\July\G[GroupNumber].[GroupMemberNumber]B[BANNER_ID][YourName]\ToDoApp"  # <-- Update this to your actual folder
output_folder = os.path.join(source_folder, "md_output")
os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    if file_name.endswith(".py"):
        py_path = os.path.join(source_folder, file_name)
        md_file_name = file_name.replace(".py", ".md")
        md_path = os.path.join(output_folder, md_file_name)

        try:
            with open(py_path, "r", encoding="utf-8") as py_file:
                code = py_file.read()
        except UnicodeDecodeError:
            with open(py_path, "r", encoding="latin-1") as py_file:
                code = py_file.read()

        md_content = f"# {file_name} - Markdown Conversion\n\n```python\n{code}\n```"

        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)

        print(f"✅ Converted: {file_name} → {md_path}")

```