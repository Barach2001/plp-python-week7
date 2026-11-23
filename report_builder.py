"""Read learner scores from hubs.csv and create report.txt."""

import csv

CSV_FILE = "hubs.csv"
REPORT_FILE = "report.txt"
PASS_MARK = 50


def main():
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            learners = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"{CSV_FILE} not found")
        return

    if not learners:
        print("No learner records found.")
        return

    scores = [float(row["score"]) for row in learners]
    total_learners = len(scores)
    passed = sum(score >= PASS_MARK for score in scores)
    failed = total_learners - passed
    average_score = sum(scores) / total_learners

    report = (
        f"Total learners: {total_learners}\n"
        f"Passed: {passed}\n"
        f"Failed: {failed}\n"
        f"Average score: {average_score:.1f}\n"
    )

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write(report)

    print(report, end="")
    print(f"Report saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
