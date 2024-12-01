#!/bin/bash

REPORT_DIR="static_analysis_reports"
mkdir -p $REPORT_DIR

bandit -r web_server/ -f html -o $REPORT_DIR/bandit_report.html
bandit -r web_server/ -f json -o $REPORT_DIR/bandit_report.json

echo "Bandit analysis completed. Reports saved in $REPORT_DIR."
