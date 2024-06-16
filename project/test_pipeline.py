import unittest
import subprocess
import io
import sys
import os

class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        script_path = os.path.join(os.path.dirname(__file__), "pipeline.py")
        result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        sys.stdout = sys.__stdout__

        # Get the output and check for specific print statements
        output = result.stdout
        print("Captured Output:\n", output)

        self.assertIn("Data pipeline executed successfully. Cleaned data stored at ../data/co2_emissions.sqlite", output,
                      "The CO2 emissions success message was not found in the output.")

        self.assertIn("Data pipeline executed successfully. Cleaned data stored at ../data/population.sqlite", output,
                      "The Population success message was not found in the output.")

if __name__ == "__main__":
    unittest.main()
