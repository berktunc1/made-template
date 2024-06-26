import unittest
import subprocess
import os

class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        script_path = os.path.join(os.path.dirname(__file__), "pipeline.py")
        result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Capture stdout and stderr
        output = result.stdout
        errors = result.stderr

        print("Captured Output:\n", output)
        print("Captured Errors:\n", errors)

        expected_outputs = [
            "Columns with all NaN values are dropped.",
            "Rows with any NaN values are dropped.",
            "Number of columns: 35",
            "Data pipeline executed successfully. Cleaned data stored at :memory:"
        ]

        # Check if all expected output fragments are present in the output
        for expected in expected_outputs:
            self.assertIn(expected, output, f"The expected message '{expected}' was not found in the output.")

if __name__ == "__main__":
    unittest.main()
