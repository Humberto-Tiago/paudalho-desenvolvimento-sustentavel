"""
Atividades Extensionistas - Tecnologia Aplicada à Inclusão Digital
Projeto: Impulsionando o Desenvolvimento Sustentável de Paudalho
ODS 08 - Trabalho decente e crescimento econômico
ODS 09 - Indústria, inovação e infraestrutura

Este script analisa o panorama socioeconômico atual do município de
Paudalho/PE, utilizando dados públicos reais, com foco em emprego,
renda, estrutura produtiva (composição do PIB) e ambiente de negócios.
A análise busca identificar pontos de atenção e subsidiar propostas de
ação alinhadas aos ODS 8 e 9.

Autor: Humberto Tiago Constantino de Oliveira
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def formatar_br(valor, decimais=2, prefixo=""):
    """Formata um número no padrão brasileiro (ponto para milhar e
    vírgula para decimal). Ex: 1150000000.0 -> '1.150.000.000,00'."""
    texto = f"{valor:,.{decimais}f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{prefixo}{texto}"


# ---------------------------------------------------------------------------
# 1. Dados utilizados (com fonte, ano de referência e link de origem)
# ---------------------------------------------------------------------------
# Todos os valores abaixo foram extraídos de fontes públicas e oficiais.
# Cada indicador traz: valor, ano de referência e fonte/link.

dados_gerais = {
    "Indicador": [
        "População estimada",
        "PIB municipal (R$)",
        "PIB per capita (R$)",
        "Empregos formais (carteira assinada)",
        "Remuneração média formal (R$)",
        "Empresas ativas",
        "IDHM (Índice de Desenvolvimento Humano Municipal)",
    ],
    "Valor": [
        59924,
        1150000000,
        20329.67,
        9200,
        2500,
        2987,
        0.639,
    ],
    "Ano de referência": [
        2025,
        2023,
        2023,
        "recente (~2023/2024)",
        "recente (~2023/2024)",
        2026,
        2010,
    ],
    "Fonte": [
        "IBGE Cidades - Panorama",
        "IBGE Cidades - Panorama",
        "IBGE Cidades - Panorama",
        "Caravela.info (com base em dados do Ministério do Trabalho/CAGED)",
        "Caravela.info (com base em dados do Ministério do Trabalho/CAGED)",
        "Empresaqui.com.br (base de CNPJs ativos)",
        "IBGE Cidades - Panorama",
    ],
    "Link": [
        "https://cidades.ibge.gov.br/brasil/pe/paudalho/panorama",
        "https://cidades.ibge.gov.br/brasil/pe/paudalho/panorama",
        "https://cidades.ibge.gov.br/brasil/pe/paudalho/panorama",
        "https://www.caravela.info/regional/paudalho---pe",
        "https://www.caravela.info/regional/paudalho---pe",
        "https://www.empresaqui.com.br/listas-de-empresas/PE/PAUDALHO",
        "https://cidades.ibge.gov.br/brasil/pe/paudalho/panorama",
    ],
}

df_geral = pd.DataFrame(dados_gerais)

# Composição setorial do PIB de Paudalho (ano de referência: 2021)
# Fonte: Caravela.info, com base em dados do IBGE (Contas Regionais)
# Link: https://www.caravela.info/regional/paudalho---pe
composicao_pib = {
    "Setor": ["Agropecuária", "Administração pública", "Serviços", "Indústria"],
    "Participacao_pct": [40.7, 29.8, 23.2, 6.3],
}
df_setores = pd.DataFrame(composicao_pib)

# Valores de referência (médias estaduais) para comparação
# Fonte: IBGE Cidades / Caravela.info - Pernambuco
referencia_pe = {
    "Indicador": ["PIB per capita (R$)", "Remuneração média formal (R$)"],
    "Paudalho": [20329.67, 2500],
    "Pernambuco (estado)": [29900, 3700],
}
df_referencia = pd.DataFrame(referencia_pe)


# ---------------------------------------------------------------------------
# 2. Funções de análise
# ---------------------------------------------------------------------------

def exibir_dados_utilizados():
    print("=" * 70)
    print("DADOS UTILIZADOS NA ANÁLISE (com fonte e ano de referência)")
    print("=" * 70)
    for _, row in df_geral.iterrows():
        valor = row["Valor"]
        if isinstance(valor, float) and valor < 1:
            # IDHM e índices entre 0 e 1 mantêm o formato original
            valor_fmt = formatar_br(valor, decimais=3)
        else:
            valor_fmt = formatar_br(valor, decimais=0)
        print(f"- {row['Indicador']}: {valor_fmt} "
              f"(ref. {row['Ano de referência']}) - Fonte: {row['Fonte']}")
    print()


def analisar_trabalho_e_renda(df_geral, df_referencia):
    """ODS 8 - Trabalho decente e crescimento econômico."""
    print("=" * 70)
    print("ANÁLISE - TRABALHO DECENTE E CRESCIMENTO ECONÔMICO (ODS 8)")
    print("=" * 70)

    pib_paudalho = df_referencia.loc[
        df_referencia["Indicador"] == "PIB per capita (R$)", "Paudalho"
    ].values[0]
    pib_pe = df_referencia.loc[
        df_referencia["Indicador"] == "PIB per capita (R$)", "Pernambuco (estado)"
    ].values[0]
    diferenca_pib = (pib_paudalho / pib_pe - 1) * 100

    print(f"PIB per capita de Paudalho: {formatar_br(pib_paudalho, prefixo='R$ ')}")
    print(f"PIB per capita médio de Pernambuco: {formatar_br(pib_pe, prefixo='R$ ')}")
    print(f"=> Paudalho está {abs(diferenca_pib):.1f}% "
          f"{'acima' if diferenca_pib > 0 else 'abaixo'} da média estadual.")
    print()

    remuneracao_paudalho = df_referencia.loc[
        df_referencia["Indicador"] == "Remuneração média formal (R$)", "Paudalho"
    ].values[0]
    remuneracao_pe = df_referencia.loc[
        df_referencia["Indicador"] == "Remuneração média formal (R$)",
        "Pernambuco (estado)",
    ].values[0]
    diferenca_remuneracao = (remuneracao_paudalho / remuneracao_pe - 1) * 100

    print(f"Remuneração média formal em Paudalho: "
          f"{formatar_br(remuneracao_paudalho, prefixo='R$ ')}")
    print(f"Remuneração média formal em Pernambuco: "
          f"{formatar_br(remuneracao_pe, prefixo='R$ ')}")
    print(f"=> Paudalho está {abs(diferenca_remuneracao):.1f}% "
          f"{'acima' if diferenca_remuneracao > 0 else 'abaixo'} da média estadual.")
    print()

    empregos = df_geral.loc[
        df_geral["Indicador"] == "Empregos formais (carteira assinada)", "Valor"
    ].values[0]
    populacao = df_geral.loc[
        df_geral["Indicador"] == "População estimada", "Valor"
    ].values[0]
    taxa_formalizacao = empregos / populacao * 100

    print(f"Empregos formais: {empregos:,.0f}")
    print(f"População estimada: {populacao:,.0f}")
    print(f"=> Aproximadamente {taxa_formalizacao:.1f}% da população do "
          f"município possui vínculo formal de trabalho.")
    print()


def analisar_industria_infraestrutura(df_setores):
    """ODS 9 - Indústria, inovação e infraestrutura."""
    print("=" * 70)
    print("ANÁLISE - INDÚSTRIA, INOVAÇÃO E INFRAESTRUTURA (ODS 9)")
    print("=" * 70)

    participacao_industria = df_setores.loc[
        df_setores["Setor"] == "Indústria", "Participacao_pct"
    ].values[0]

    setor_predominante = df_setores.sort_values(
        "Participacao_pct", ascending=False
    ).iloc[0]

    print(f"Participação da indústria no PIB municipal: "
          f"{participacao_industria:.1f}%")
    print(f"Setor com maior participação no PIB: "
          f"{setor_predominante['Setor']} ({setor_predominante['Participacao_pct']:.1f}%)")
    print()
    print("=> A baixa participação da indústria no PIB (apenas "
          f"{participacao_industria:.1f}%) indica espaço significativo "
          "para políticas de incentivo à industrialização e inovação, "
          "em linha com o ODS 9.")
    print()


def propor_acoes(df_setores, df_referencia):
    """Gera propostas de ação com base nos indicadores analisados."""
    print("=" * 70)
    print("PROPOSTAS DE AÇÃO (com base nos dados analisados)")
    print("=" * 70)

    acoes = []

    participacao_industria = df_setores.loc[
        df_setores["Setor"] == "Indústria", "Participacao_pct"
    ].values[0]
    if participacao_industria < 15:
        acoes.append(
            "Criar incentivos fiscais e linhas de crédito municipais para "
            "atrair e desenvolver pequenas e médias indústrias locais, "
            "diversificando a economia hoje concentrada na agropecuária "
            "(ODS 9)."
        )

    remuneracao_paudalho = df_referencia.loc[
        df_referencia["Indicador"] == "Remuneração média formal (R$)", "Paudalho"
    ].values[0]
    remuneracao_pe = df_referencia.loc[
        df_referencia["Indicador"] == "Remuneração média formal (R$)",
        "Pernambuco (estado)",
    ].values[0]
    if remuneracao_paudalho < remuneracao_pe:
        acoes.append(
            "Promover programas de qualificação profissional voltados a "
            "setores com maior remuneração média, buscando reduzir a "
            "diferença salarial em relação à média estadual (ODS 8)."
        )

    acoes.append(
        "Implementar um painel público de indicadores socioeconômicos do "
        "município (emprego, PIB setorial, novas empresas), atualizado "
        "periodicamente, para acompanhamento pela população e gestores "
        "públicos (ODS 9 - inovação e transparência)."
    )

    acoes.append(
        "Fomentar parcerias entre o poder público local e instituições de "
        "ensino para projetos de extensão e inovação aplicados aos "
        "principais desafios identificados (ODS 8 e 9)."
    )

    for i, acao in enumerate(acoes, start=1):
        print(f"{i}. {acao}")
    print()


# ---------------------------------------------------------------------------
# 3. Geração de gráficos (dark mode, rótulos, médias e anotações)
# ---------------------------------------------------------------------------

# Paleta de cores para dark mode
COR_FUNDO      = "#1C1C2E"
COR_PAINEL     = "#2A2A3E"
COR_TEXTO      = "#E0E0F0"
COR_GRADE      = "#3A3A5A"
COR_DESTAQUE   = "#E94560"   # Paudalho
COR_COMPARACAO = "#4E9AF1"   # Pernambuco / média
COR_ALERTA     = "#F5A623"   # anotações de atenção
CORES_SETORES  = ["#4CAF50", "#9E9E9E", "#4E9AF1", "#E94560"]


def _aplicar_dark_mode(fig, ax):
    """Aplica o tema dark mode em uma figura e eixo."""
    fig.patch.set_facecolor(COR_FUNDO)
    ax.set_facecolor(COR_PAINEL)
    ax.tick_params(colors=COR_TEXTO, labelsize=10)
    ax.xaxis.label.set_color(COR_TEXTO)
    ax.yaxis.label.set_color(COR_TEXTO)
    ax.title.set_color(COR_TEXTO)
    for spine in ax.spines.values():
        spine.set_edgecolor(COR_GRADE)
    ax.grid(axis="y", color=COR_GRADE, linestyle="--", linewidth=0.7, alpha=0.6)
    ax.set_axisbelow(True)


def _rotulo_br(ax, barras, prefixo="", decimais=0):
    """Adiciona rótulos no padrão BR em cima de cada barra."""
    for barra in barras:
        altura = barra.get_height()
        texto = formatar_br(altura, decimais=decimais, prefixo=prefixo)
        ax.annotate(
            texto,
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center", va="bottom",
            color=COR_TEXTO, fontsize=9, fontweight="bold",
        )


def gerar_graficos(df_setores, df_referencia, pasta_saida="graficos"):
    os.makedirs(pasta_saida, exist_ok=True)

    # ------------------------------------------------------------------
    # Gráfico 1 — Composição do PIB por setor (barras horizontais)
    # ------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(9, 5))
    _aplicar_dark_mode(fig, ax)

    setores = df_setores["Setor"]
    valores = df_setores["Participacao_pct"]
    barras = ax.barh(setores, valores, color=CORES_SETORES,
                     edgecolor=COR_FUNDO, linewidth=0.5, height=0.55)

    # Rótulos dentro/fora das barras
    for barra, val in zip(barras, valores):
        ax.text(
            val + 0.5, barra.get_y() + barra.get_height() / 2,
            formatar_br(val, decimais=1) + "%",
            va="center", color=COR_TEXTO, fontsize=10, fontweight="bold",
        )

    # Anotação de atenção na indústria
    idx_industria = list(setores).index("Indústria")
    ax.annotate(
        "⚠ Baixa participação industrial\n→ potencial para ODS 9",
        xy=(valores.iloc[idx_industria], idx_industria),
        xytext=(20, -1.2),
        textcoords=("offset points", "data"),
        color=COR_ALERTA, fontsize=8.5,
        arrowprops=dict(arrowstyle="->", color=COR_ALERTA, lw=1.2),
    )

    ax.set_xlabel("Participação no PIB (%)", color=COR_TEXTO)
    ax.set_title("Composição do PIB de Paudalho/PE por setor\n"
                 "Fonte: Caravela.info / IBGE (2021)", color=COR_TEXTO,
                 fontsize=12, pad=14)
    ax.set_xlim(0, 55)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, "composicao_pib_setores.png"),
                dpi=150, facecolor=COR_FUNDO)
    plt.close()

    # ------------------------------------------------------------------
    # Gráfico 2 — PIB per capita: Paudalho x Pernambuco
    # ------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 5))
    _aplicar_dark_mode(fig, ax)

    linha = df_referencia[df_referencia["Indicador"] == "PIB per capita (R$)"]
    v_paudalho = linha["Paudalho"].values[0]
    v_pe       = linha["Pernambuco (estado)"].values[0]
    rotulos    = ["Paudalho", "Pernambuco\n(estado)"]
    valores_b  = [v_paudalho, v_pe]
    cores_b    = [COR_DESTAQUE, COR_COMPARACAO]

    barras = ax.bar(rotulos, valores_b, color=cores_b,
                    edgecolor=COR_FUNDO, linewidth=0.5, width=0.45)
    _rotulo_br(ax, barras, prefixo="R$ ")

    # Linha da média estadual
    ax.axhline(v_pe, color=COR_COMPARACAO, linestyle="--",
               linewidth=1.2, alpha=0.6)
    ax.text(1.48, v_pe + 300,
            f"Média PE: {formatar_br(v_pe, prefixo='R$ ')}",
            color=COR_COMPARACAO, fontsize=8.5, ha="right")

    # Anotação de diferença
    diferenca = (v_paudalho / v_pe - 1) * 100
    ax.annotate(
        f"⚠ {abs(diferenca):.1f}% abaixo\nda média estadual",
        xy=(0, v_paudalho),
        xytext=(0.35, v_paudalho + 2000),
        color=COR_ALERTA, fontsize=9,
        arrowprops=dict(arrowstyle="->", color=COR_ALERTA, lw=1.2),
    )

    ax.set_ylabel("R$ (reais)", color=COR_TEXTO)
    ax.set_title("PIB per capita: Paudalho x Pernambuco\n"
                 "Fonte: IBGE Cidades (2023)", color=COR_TEXTO,
                 fontsize=12, pad=14)
    ax.set_ylim(0, v_pe * 1.35)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, "pib_per_capita_comparativo.png"),
                dpi=150, facecolor=COR_FUNDO)
    plt.close()

    # ------------------------------------------------------------------
    # Gráfico 3 — Remuneração média formal: Paudalho x Pernambuco
    # ------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 5))
    _aplicar_dark_mode(fig, ax)

    linha = df_referencia[
        df_referencia["Indicador"] == "Remuneração média formal (R$)"
    ]
    v_paudalho = linha["Paudalho"].values[0]
    v_pe       = linha["Pernambuco (estado)"].values[0]
    valores_b  = [v_paudalho, v_pe]

    barras = ax.bar(rotulos, valores_b, color=cores_b,
                    edgecolor=COR_FUNDO, linewidth=0.5, width=0.45)
    _rotulo_br(ax, barras, prefixo="R$ ")

    # Linha da média estadual
    ax.axhline(v_pe, color=COR_COMPARACAO, linestyle="--",
               linewidth=1.2, alpha=0.6)
    ax.text(1.48, v_pe + 60,
            f"Média PE: {formatar_br(v_pe, prefixo='R$ ')}",
            color=COR_COMPARACAO, fontsize=8.5, ha="right")

    # Anotação de diferença
    diferenca = (v_paudalho / v_pe - 1) * 100
    ax.annotate(
        f"⚠ {abs(diferenca):.1f}% abaixo\nda média estadual",
        xy=(0, v_paudalho),
        xytext=(0.35, v_paudalho + 400),
        color=COR_ALERTA, fontsize=9,
        arrowprops=dict(arrowstyle="->", color=COR_ALERTA, lw=1.2),
    )

    ax.set_ylabel("R$ (reais)", color=COR_TEXTO)
    ax.set_title("Remuneração média formal: Paudalho x Pernambuco\n"
                 "Fonte: Caravela.info / Ministério do Trabalho",
                 color=COR_TEXTO, fontsize=12, pad=14)
    ax.set_ylim(0, v_pe * 1.35)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, "remuneracao_comparativo.png"),
                dpi=150, facecolor=COR_FUNDO)
    plt.close()

    print(f"Gráficos salvos na pasta '{pasta_saida}/'.")
    print()


# ---------------------------------------------------------------------------
# 4. Execução principal
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    exibir_dados_utilizados()
    analisar_trabalho_e_renda(df_geral, df_referencia)
    analisar_industria_infraestrutura(df_setores)
    propor_acoes(df_setores, df_referencia)
    gerar_graficos(df_setores, df_referencia)
