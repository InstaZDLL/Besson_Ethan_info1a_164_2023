import os

os.system("pip install tqdm")
from tqdm import tqdm

dependencies = ["pip", "flask", "python-dotenv", "mysql-connector-python"]

print("Installing dependencies...")
os.system("python.exe -m pip install --upgrade pip")

for dependency in tqdm(dependencies):
    os.system(f"pip install {dependency}")

print("Installation terminée " + "\U00002705")
