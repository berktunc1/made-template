import os
import unittest
import subprocess

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.co2_db_path = "../data/co2_emissions.sqlite"
        self.population_db_path = "../data/population.sqlite"

        if os.path.exists(self.co2_db_path):
            os.remove(self.co2_db_path)
        if os.path.exists(self.population_db_path):
            os.remove(self.population_db_path)

    def test_pipeline(self):
        def test_pipeline(self):
        print("Running data pipeline script...")
        result = subprocess.run(["python", os.path.join(os.path.dirname(__file__), "pipeline.py")], capture_output=True, text=True)
        print("Data pipeline script executed.")

        co2_message = f"Simulating storing data in SQLite database at: {self.co2_db_path}"
        population_message = f"Simulating storing data in SQLite database at: {self.population_db_path}"

        self.assertIn(co2_message, result.stdout, f"Expected message not found: {co2_message}")
        self.assertIn(population_message, result.stdout, f"Expected message not found: {population_message}")


if __name__ == "__main__":
    unittest.main()
