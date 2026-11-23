# Week 7 Assignment: My Notes & The Report Builder

This repository contains the two Python programs and their data/output files for the Week 7 assignment.

## Files

- `my_notes.py` — asks the user for a note, appends it to the notes file, and displays the saved notes.
- `my_notes.txt` — sample text file used to store notes.
- `report_builder.py` — reads learner scores from the CSV file, calculates the results, and creates a text report.
- `hubs.csv` — sample learner names and scores used by the report builder.
- `report.txt` — generated report containing the learner totals and average score.

## Question 1: What happens if you change "a" to "w"?

Changing the file mode from `"a"` (append) to `"w"` (write) means the program will replace the existing contents of `my_notes.txt` each time it saves a note. Older notes will be erased instead of being kept.

## How to run

Run these commands in the repository folder:

```bash
python my_notes.py
python report_builder.py
```

To test missing-file handling, temporarily rename `hubs.csv` to `hubs_backup.csv` and run `python report_builder.py`. It should print `hubs.csv not found` without crashing. Rename the CSV file back to `hubs.csv` afterwards.
