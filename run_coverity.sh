#!/bin/bash

COVERITY_TOOL_PATH="/opt/coverity/bin"
BUILD_OUTPUT_DIR="coverity_build"
ANALYSIS_OUTPUT_DIR="coverity_analysis"
PROJECT_NAME="website_monitoring"

rm -rf $BUILD_OUTPUT_DIR $ANALYSIS_OUTPUT_DIR

$COVERITY_TOOL_PATH/cov-build --dir $BUILD_OUTPUT_DIR docker-compose build

$COVERITY_TOOL_PATH/cov-analyze --dir $BUILD_OUTPUT_DIR

$COVERITY_TOOL_PATH/cov-format-errors --dir $BUILD_OUTPUT_DIR --html-output $ANALYSIS_OUTPUT_DIR

echo "Coverity analysis completed. Reports are available in the $ANALYSIS_OUTPUT_DIR directory."
