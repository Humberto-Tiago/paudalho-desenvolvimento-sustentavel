# 🌱 Impulsionando o Desenvolvimento Sustentável de Paudalho/PE

Projeto de Atividade Extensionista II — Centro Universitário Internacional UNINTER  
Curso: Ciência de Dados  
Aluno: Humberto Tiago Constantino de Oliveira

---

## 📌 Sobre o projeto

Análise de dados públicos do município de Paudalho/PE com foco em emprego, renda, estrutura produtiva e infraestrutura, utilizando a linguagem Python. O objetivo é identificar desafios e propor ações de melhoria alinhadas aos ODS 8 e 9 da ONU.


---

## 🎯 ODS contemplados

- **ODS 8** — Trabalho decente e crescimento econômico  
- **ODS 9** — Indústria, inovação e infraestrutura

---

## 📊 O que o script analisa

- Emprego formal e remuneração média (comparativo com Pernambuco)
- PIB municipal e PIB per capita
- Composição do PIB por setor (agropecuária, indústria, serviços, administração pública)
- Propostas de ação baseadas nos dados

---

## 🗂️ Fontes dos dados

| Indicador | Fonte | Ano |
|---|---|---|
| População, PIB, IDHM | [IBGE Cidades](https://cidades.ibge.gov.br/brasil/pe/paudalho/panorama) | 2023/2025 |
| Emprego e remuneração | [Caravela.info](https://www.caravela.info/regional/paudalho---pe) | 2023/2024 |
| Empresas ativas | [Empresaqui.com.br](https://www.empresaqui.com.br/listas-de-empresas/PE/PAUDALHO) | 2026 |
| Composição do PIB | [Caravela.info / IBGE](https://www.caravela.info/regional/paudalho---pe) | 2021 |

---

## ▶️ Como executar

1. Instale as dependências:
```bash
pip install pandas matplotlib
```
2. Execute o script:
```bash
python analise_paudalho_real.py
```
3. Os gráficos serão salvos automaticamente na pasta `graficos/`

---

## 📁 Estrutura do repositório

```
📦 paudalho-desenvolvimento-sustentavel
 ┣ 📄 analise_paudalho.py
 ┣ 📁 graficos/
 ┃ ┣ 🖼️ composicao_pib_setores.png
 ┃ ┣ 🖼️ pib_per_capita_comparativo.png
 ┃ ┗ 🖼️ remuneracao_comparativo.png
 ┗ 📄 README.md
```
