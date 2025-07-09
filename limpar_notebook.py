import nbformat
import os

entrada = "notebook.ipynb"   # <- altere aqui se o nome for outro
saida = "notebook_limpo.ipynb"

# Verifica se o arquivo existe
if not os.path.exists(entrada):
    print(f"❌ Arquivo '{entrada}' não encontrado.")
    exit()

try:
    # Lê o notebook
    with open(entrada, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Limpa metadados do notebook
    for chave in ["colab", "accelerator", "kernelspec", "widgets"]:
        nb.metadata.pop(chave, None)

    # Limpa metadados de cada célula
    for cell in nb.cells:
        cell.metadata = {}

    # Salva novo notebook limpo
    with open(saida, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"✅ Notebook limpo salvo como: {saida}")

except Exception as e:
    print(f"❌ Erro ao processar o notebook: {e}")

