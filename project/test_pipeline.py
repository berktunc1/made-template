import os
import unittest
import subprocess

class TestPipeline(unittest.TestCase):

    def setUp(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), "../data")
        self.co2_db_path = os.path.join(self.data_dir, "co2_emissions.sqlite")
        self.population_db_path = os.path.join(self.data_dir, "population.sqlite")

        os.makedirs(self.data_dir, exist_ok=True)

        if os.path.exists(self.co2_db_path):
            os.remove(self.co2_db_path)
        if os.path.exists(self.population_db_path):
            os.remove(self.population_db_path)

    def test_pipeline(self):
        print("Running data pipeline script...")
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), "pipeline.py")], check=True)
        print("Data pipeline script executed.")

        co2_exists = os.path.exists(self.co2_db_path)
        population_exists = os.path.exists(self.population_db_path)
        
        if co2_exists:
            print(f"Dataset exists: {self.co2_db_path}")
        else:
            print(f"Dataset does not exist: {self.co2_db_path}")
        
        if population_exists:
            print(f"Dataset exists: {self.population_db_path}")
        else:
            print(f"Dataset does not exist: {self.population_db_path}")

        self.assertTrue(co2_exists, "CO2 emissions database file does not exist.")
        self.assertTrue(population_exists, "Population database file does not exist.")

if __name__ == "__main__":
    unittest.main()