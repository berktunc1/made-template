#!/bin/bash
cd "$(dirname "$0")"

# Run the unit tests
echo "Running test_pipeline.py..."
python -m unittest test_pipeline.py

TEST_EXIT_STATUS=$?

if [ $TEST_EXIT_STATUS -eq 0 ]; then
  echo "All tests passed!"
else
  echo "Some tests failed. Please check the output above for details."
fi



exit $TEST_EXIT_STATUS