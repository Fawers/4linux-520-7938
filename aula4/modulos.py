import os
import subprocess
import pprint  # pretty print


# pprint.pprint(dict(os.environ))

requirements_file = os.environ.get("REQUIREMENTS_TXT")
print(requirements_file)
processo = os.popen("date")
saida = list(processo)[0]
print(saida)
processo.close()

processo = subprocess.Popen(
    "date", stdout=subprocess.PIPE, shell=True)

processo.wait()
print(processo.pid)
print(processo.returncode)
# print(processo.stdout.read().decode().strip())

for (caminho, pastas, arquivos) in os.walk('.'):
    print(f"estamos em {caminho}")
    print(f"os arquivos são {arquivos}")
    print(f"as pastas são {pastas}")
    input("> ")



