import polars as pl
import re
import xlsxwriter
import os

pasta = r"data"

arquivos = [f for f in os.listdir(pasta) if f.endswith((".xlsx", ".xls", ".csv"))]

print("Escolha um arquivo para gerar a planilha formatada:")
for i, arquivo in enumerate(arquivos, start=1):
    print(f"{i}. {arquivo}")

escolha = int(input("Digite o número do arquivo escolhido: ")) - 1

if escolha < 0 or escolha >= len(arquivos):
    print("Escolha inválida. Encerrando o programa.")
    exit()

arquivo_selecionado = arquivos[escolha]

def carregar_arquivo(caminho):
    if caminho.endswith(".csv"):
        return pl.read_csv(caminho)
    else:
        return pl.read_excel(caminho)

df = carregar_arquivo(os.path.join(pasta, arquivo_selecionado))

empresas = (
    df["Company Name"]
    .drop_nulls()
    .unique()
    .to_list()
)

for empresa in empresas:
    
    df_filtrado = df.filter(pl.col("Company Name") == empresa)
    
    nome = re.sub(r'[\\/*?:"<>|]', "-", str(empresa))[:80]

    saida = "outputs"
    os.makedirs(saida, exist_ok=True)

    workbook = xlsxwriter.Workbook(os.path.join(saida, f"{nome}.xlsx"))
    worksheet = workbook.add_worksheet("Dados")

    # estilos
    header_format = workbook.add_format({
        "bold": True,
        "bg_color": "#752BFF",
        "border": 1
    })

    cell_format = workbook.add_format({
        "border": 1
    })

    # escrever cabeçalho
    for col_idx, col in enumerate(df_filtrado.columns):
        worksheet.write(0, col_idx, col, header_format)

    # escrever dados
    for row_idx, row in enumerate(df_filtrado.to_numpy(), start=1):
        for col_idx, value in enumerate(row):
            worksheet.write(row_idx, col_idx, value, cell_format)

    # auto ajuste de coluna
    for i, col in enumerate(df_filtrado.columns):
        max_len = max(
            df_filtrado[col].cast(str).str.len_chars().max(),
            len(col)
        )
        worksheet.set_column(i, i, min(max_len + 2, 40))

    worksheet.add_table(0, 0, row_idx, len(df_filtrado.columns) - 1, {
        'columns': [{'header': col} for col in df_filtrado.columns]
    })
    print(f'Criado: {nome}.xlsx')

    workbook.close()

print("Arquivos formatados criados!")