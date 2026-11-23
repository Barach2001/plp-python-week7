"""Read learner scores from hubs.csv and create report.txt."""

import csv

try:
    with open("hubs.csv", "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

total = 0
passed = 0

for row in rows:
    # CSV values are text, so convert the score to an integer.
    score = int(row["score"])
    total += score
    if score >= 50:
        passed += 1

failed = len(rows) - passed
average = round(total / len(rows), 1) if rows else 0.0

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(failed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")
