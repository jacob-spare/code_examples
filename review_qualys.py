import csv
import sys
from collections import Counter

def review_qualys_csv(file_path):
    severity_counts = Counter()
    vulnerabilities = []

    try:
        with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
            # Skip Qualys header metadata lines if present (usually starts with title/info)
            reader = csv.DictReader(f)
            
            for row in reader:
                # Standard Qualys CSV column names often include 'Severity', 'IP', 'QID', 'Title'
                sev = row.get('Severity', 'Unknown')
                severity_counts[sev] += 1
                vulnerabilities.append({
                    'IP': row.get('IP', 'N/A'),
                    'QID': row.get('QID', 'N/A'),
                    'Severity': sev,
                    'Title': row.get('Title', 'N/A')
                })

        print("=== Qualys Scan Review Summary ===")
        print(f"Total Detections Found: {sum(severity_counts.values())}\n")
        print("Breakdown by Severity:")
        for sev, count in sorted(severity_counts.items(), reverse=True):
            print(f"  Severity {sev}: {count} issues")

        print("\nTop 5 Critical/High Vulnerabilities:")
        high_crit = [v for v in vulnerabilities if v['Severity'] in ['4', '5']]
        for v in high_crit[:5]:
            print(f"  - IP: {v['IP']} | QID: {v['QID']} | Severity: {v['Severity']} | {v['Title']}")

    except Exception as e:
        print(f"Error reading report: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python review_qualys.py <path_to_qualys_report.csv>")
        sys.exit(1)
        
    report_file = sys.argv[1]
    review_qualys_csv(report_file)
