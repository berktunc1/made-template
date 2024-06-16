import unittest
import subprocess
import io
import sys

class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        # Capture the output during the execution of the script
        captured_output = io.StringIO()
        sys.stdout = captured_output

        subprocess.run(["python", "pipeline.py"], check=True)
        
        sys.stdout = sys.__stdout__

        # Get the output and check for specific print statement
        output = captured_output.getvalue()
        print("Captured Output:\n", output)

      
        self.assertIn("Data pipeline executed successfully. Cleaned data stored at ../data/co2_emissions.sqlite", output,
                      "The CO2 emissions success message was not found in the output.")

        self.assertIn("Data pipeline executed successfully. Cleaned data stored at ../data/population.sqlite", output,
                      "The Population success message was not found in the output.")

if __name__ == "__main__":
    unittest.main()
