PRODUTOS = [
    {"id": 1, "nome": "Teclado", "categoria": "perifericos", "preco": 150.00},
    {"id": 2, "nome": "Monitor", "categoria": "telas", "preco": 900.00},
    {"id": 3, "nome": "Mouse", "categoria": "perifericos", "preco": 80.00},
    {"id": 4, "nome": "Notebook", "categoria": "computadores", "preco": 3500.00},
    {"id": 5, "nome": "Cabo HDMI", "categoria": "acessorios", "preco": 35.00},
]

DESCONTO_MAXIMO = 0.15  
DESCONTO_CLIENTE = {"comum": 0.0, "prata": 0.05, "ouro": 0.10}
def retorna_desconto(produto, cliente):
    desconto = DESCONTO_CLIENTE[cliente]
    if produto["preco"] >= 500:
        desconto += 0.05
    if produto["categoria"] == "acessorios":
        desconto += 0.02
    return min(desconto, DESCONTO_MAXIMO)

def preco_final(produto, cliente):
    return round(produto["preco"] * (1 - retorna_desconto(produto, cliente)), 2)

def main():
    print("=== MOTOR DE DESCONTOS ===")
    cliente = input("Tipo de cliente (comum/prata/ouro): ").strip().lower()
    if cliente not in DESCONTO_CLIENTE:
        print("Cliente desconhecido: será considerado comum.")
        cliente = "comum"

    finais = {p["id"]: preco_final(p, cliente) for p in PRODUTOS}

    for produto in PRODUTOS:
        final = finais[produto["id"]]
        print(f'{produto["nome"]}: R$ {produto["preco"]:.2f} -> R$ {final:.2f}')

    total_original = sum(p["preco"] for p in PRODUTOS)
    total_final = sum(finais.values())
    print(f"Total original: R$ {total_original:.2f}")
    print(f"Total final: R$ {total_final:.2f}")
    print(f"Economia: R$ {total_original - total_final:.2f}")


if __name__ == "__main__":
    main()
