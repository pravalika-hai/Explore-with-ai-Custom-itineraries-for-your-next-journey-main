import os
import glob
from docx2pdf import convert

directory = r"c:\Users\sriha\Downloads\Explore-with-ai-Custom-itineraries-for-your-next-journey-main\Explore-with-ai-Custom-itineraries-for-your-next-journey-main\Document"
docx_files = glob.glob(os.path.join(directory, "**", "*.docx"), recursive=True)

# Filter out temp files that start with ~$
docx_files = [f for f in docx_files if not os.path.basename(f).startswith("~$")]

print(f"Converting {len(docx_files)} files to PDF...")
for f in docx_files:
    print(f"Converting {f}...")
    convert(f)
print("Done!")
