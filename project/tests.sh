#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Run the unit tests
echo "Running test_pipeline.py..."
python -m unittest test_pipeline.py

# Capture the exit status of the test
TEST_EXIT_STATUS=$?

# Check if tests passed or failed
if [ $TEST_EXIT_STATUS -eq 0 ]; then
  echo "All tests passed!"
else
  echo "Some tests failed. Please check the output above for details."
fi

# Exit with the test exit status
exit $TEST_EXIT_STATUS
