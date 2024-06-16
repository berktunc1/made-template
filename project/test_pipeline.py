import unittest
import subprocess
import os

class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        # Run the pipeline script
        script_path = os.path.join(os.path.dirname(__file__), "pipeline.py")
        result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Capture stdout and stderr
        output = result.stdout
        errors = result.stderr

        print("Captured Output:\n", output)
        print("Captured Errors:\n", errors)

        # Check if the output contains the expected print statement for CO2 data
        self.assertIn("Data pipeline executed successfully. Cleaned data stored at ../data/co2_emissions.sqlite", output,
                      "The CO2 emissions success message was not found in the output.")

        # Check if the output contains the expected print statement for Population data
        self.assertIn("Data pipeline executed successfully. Cleaned data stored at ../data/population.sqlite", output,
                      "The Population success message was not found in the output.")

if __name__ == "__main__":
    unittest.main()
