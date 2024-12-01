#!/bin/bash

REPORT_DIR="static_analysis_reports"
mkdir -p $REPORT_DIR
flawfinder --columns web_server/ > $REPORT_DIR/static_analysis_report.txt
echo "Flawfinder analysis completed. Report saved in $REPORT_DIR/static_analysis_report.txt"
