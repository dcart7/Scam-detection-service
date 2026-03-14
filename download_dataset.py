import kagglehub
import os

dataset_path = kagglehub.dataset_download("divanshu22/scam-dataset")

os.makedirs("data", exist_ok=True)

print("Path to dataset files:", dataset_path)