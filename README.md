# Data Splitter & Excel Formatter

## 📌 Overview
This project automates the process of splitting a dataset into multiple Excel files based on a category (such as company or client), applying formatting to improve readability and consistency.

## 🎯 Problem
In many business scenarios, large datasets need to be shared with multiple stakeholders. Manually filtering and exporting Excel files for each group is time-consuming, repetitive, and prone to errors.

## ✅ Solution
This script solves the problem by:
- Allowing the user to select a file from a folder
- Automatically splitting the dataset by a selected column (e.g., "Company Name")
- Generating one Excel file per group
- Applying consistent formatting (headers, borders, table structure, column width)

## ⚙️ Tech Stack
- Python
- Polars (fast dataframe processing)
- XlsxWriter (Excel formatting)

## 📂 Project Structure
```
project-folder/
│
├── data/              # Sample or anonymized datasets
├── output/            # Generated Excel files
├── src/
│   └── main.py        # Main script
├── README.md
└── requirements.txt
```

## 📁 Sample Output
An example of generated Excel files is included in the `output/` folder for demonstration purposes.

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python src/main.py
```

3. Select a file by typing its number in the terminal.

## 📊 Features
- Interactive file selection from a folder
- Automatic dataset segmentation
- Excel file generation per group
- Styled header (color + bold)
- Borders applied to all cells
- Auto-adjusted column width
- Structured table format
- Safe file naming (invalid characters handled)

## 🔒 Data Privacy
No real or sensitive data is included in this repository.
All examples are anonymized or synthetic, ensuring compliance with data protection practices.

## 💡 Business Impact
- Reduces manual work in report generation
- Improves consistency across outputs
- Scales easily for large datasets
- Minimizes risk of human error

## 🔧 Possible Improvements
- Add a graphical user interface (GUI)
- Integrate logging for audit and tracking
- Support more file formats
- Connect with BI tools (e.g., Power BI)

## 👤 Author
Pedro Henrique Degan