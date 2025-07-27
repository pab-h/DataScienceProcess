from os import path
from os import remove
from os import makedirs
import zipfile
import subprocess

baseDir = path.abspath(
    path.join(path.dirname(__file__), '../dataset')
)

makedirs(baseDir, exist_ok = True)

datasets = [
    {
        "name": "prf",
        "url":  "https://drive.google.com/uc?export=download&id=14qBOhrE1gioVtuXgxkCJ9kCA8YtUGXKA"
    },
    {
        "name": "life-expectancy",
        "url":  "https://www.kaggle.com/api/v1/datasets/download/kumarajarshi/life-expectancy-who"
    }
]

def download(url, outputZipPath):
    subprocess.run([
        "curl", "-L", "-o", outputZipPath, url
    ], check=True)

def extractZip(zipPath, extractTo):
    with zipfile.ZipFile(zipPath, 'r') as z:
        z.extractall(extractTo)

    remove(zipPath)

for dataset in datasets:
    
    name      = dataset['name']
    url       = dataset['url']
    outputDir = path.join(baseDir, name)
    
    makedirs(outputDir, exist_ok=True)

    zipPath = path.join(outputDir, f"{name}.zip")

    print(f"Baixando: {name}")

    try:
        download(url, zipPath)
        extractZip(zipPath, outputDir)
        print(f"Concluído: {name}")

    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar {name}: {e}")
        
    except zipfile.BadZipFile:
        print(f"Arquivo ZIP inválido para {name}.")
