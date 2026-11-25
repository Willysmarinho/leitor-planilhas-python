"""Lê uma planilha (CSV) de vendas e gera uma nova planilha com o total por produto."""
import csv
import sys
from collections import defaultdict


def ler_planilha(caminho):
    with open(caminho, newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def total_por_produto(linhas):
    totais = defaultdict(float)
    for linha in linhas:
        totais[linha["produto"]] += int(linha["quantidade"]) * float(linha["preco"])
    return dict(totais)


def salvar_planilha(totais, caminho):
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["produto", "total"])
        for produto, total in sorted(totais.items()):
            escritor.writerow([produto, f"{total:.2f}"])


if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else "vendas.csv"
    saida = sys.argv[2] if len(sys.argv) > 2 else "total_por_produto.csv"
    totais = total_por_produto(ler_planilha(entrada))
    salvar_planilha(totais, saida)
    for produto, total in sorted(totais.items()):
        print(f"{produto}: R$ {total:.2f}")
    print(f"Planilha gerada: {saida}")
