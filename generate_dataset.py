import numpy as np
import pandas as pd
from pathlib import Path


def gerar_dataset_csv(destino: Path, quantidade: int = 1000) -> pd.DataFrame:
    """Gera um dataset sintético de falhas em máquinas e salva em CSV."""

    np.random.seed(42)

    temperatura = np.random.normal(70, 10, quantidade)
    vibracao = np.random.normal(3, 1, quantidade)
    corrente = np.random.normal(12, 2, quantidade)
    pressao = np.random.normal(6, 0.8, quantidade)
    horas_operacao = np.random.randint(100, 5000, quantidade)
    ciclos = np.random.randint(1000, 50000, quantidade)

    falha = (
        (temperatura > 85)
        | (vibracao > 4.5)
        | (corrente > 16)
        | (pressao > 7.5)
        | (horas_operacao > 4000)
    ).astype(int)

    dados = pd.DataFrame(
        {
            "temperatura": np.round(temperatura, 2),
            "vibracao": np.round(vibracao, 2),
            "corrente": np.round(corrente, 2),
            "pressao": np.round(pressao, 2),
            "horas_operacao": horas_operacao,
            "ciclos": ciclos,
            "falha": falha,
        }
    )

    destino.parent.mkdir(parents=True, exist_ok=True)

    dados.to_csv(destino, index=False)

    return dados


if __name__ == "__main__":
    destino_csv = Path("data") / "dados_maquina.csv"

    dados = gerar_dataset_csv(
        destino_csv,
        quantidade=1000
    )

    print("Dataset criado com sucesso!")
    print(f"Quantidade de registros: {len(dados)}")

    print("\nPrimeiros registros:")
    print(dados.head())

    print("\nQuantidade de máquinas com falha:")
    print(dados["falha"].value_counts())