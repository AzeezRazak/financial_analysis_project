# main.py

from models.report_analyzer import ReportAnalyzer

def main():
    config = {'directory_path': '/path/to/reports/'}
    analyzer = ReportAnalyzer(storage_type='local', config=config)
    analysis = analyzer.analyze_latest_report()
    print(analysis)

if __name__ == "__main__":
    main()
