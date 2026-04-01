# 📄 Manipulador de PDF em Python

Ferramenta para **manipulação de arquivos PDF** desenvolvida em Python com Programação Orientada a Objetos (POO). Permite selecionar páginas de múltiplos PDFs de origem, compilá-las em um novo documento e aplicar marca d'água nas páginas desejadas.

---

## 📋 Sobre o Projeto

O projeto utiliza a biblioteca **PyPDF2** para ler, combinar e escrever arquivos PDF de forma programática. A classe `ManipuladorPDF` centraliza toda a lógica: leitura e validação de páginas, aplicação de marca d'água e salvamento do arquivo final. O código conta com tratamento robusto de erros em cada etapa do processo.

---

## 🗂️ Estrutura do Código

### `class ManipuladorPDF`

**Atributos:**
- `writer` — instância de `PdfWriter` que acumula as páginas a serem salvas no arquivo final

---

**Métodos:**

#### `processar_pdf(estrutura_dados)`
Recebe um dicionário onde cada chave é o caminho de um arquivo PDF e o valor é uma lista de índices das páginas a incluir.

- Verifica se o arquivo existe no disco
- Valida se os índices fornecidos são inteiros e estão dentro do intervalo de páginas do PDF
- Exibe avisos para páginas inválidas e ignora entradas problemáticas sem interromper o processo
- Adiciona as páginas válidas ao `writer`

```python
estrutura_dados = {
    'relatorio.pdf': [0, 1],
    'anexo.pdf': [2, 3, 4],
}
```

---

#### `aplica_watermark(watermark_file, indices_alvo)`
Aplica uma marca d'água em páginas específicas do documento em construção.

- Verifica se o arquivo de marca d'água existe
- Usa a primeira página do PDF de watermark como sobreposição (`merge_page`)
- Aplica a marca d'água apenas nos índices especificados em `indices_alvo`
- Reconstrói o `writer` com as páginas já mescladas

```python
manipulador.aplica_watermark('watermark.pdf', [0, 2])
```

---

#### `salvar_pdf(output_filename)`
Salva o documento final em disco com o nome fornecido.

- Valida se o nome do arquivo não está vazio
- Exibe aviso caso o arquivo já exista (será sobrescrito)
- Trata erros de permissão, diretório inválido e outros erros de sistema (`PermissionError`, `IsADirectoryError`, `OSError`)
- Retorna `True` em caso de sucesso ou `False` em caso de falha

```python
manipulador.salvar_pdf('PDF_final.pdf')
```

---

## 🔄 Fluxo de Uso

```
1. Criar instância de ManipuladorPDF
        ↓
2. processar_pdf()  →  lê e seleciona páginas de um ou mais PDFs
        ↓
3. aplica_watermark()  →  mescla marca d'água nas páginas desejadas (opcional)
        ↓
4. salvar_pdf()  →  grava o documento final em disco
```

---

## 💻 Exemplo de Uso

```python
from projeto_manipulador_de_Pdf import ManipuladorPDF

estrutura_dados = {
    'pdf_exemplo.pdf':  [0],
    'pdf_exemplo2.pdf': [0, 1, 2],
    'pdf_exemplo3.pdf': [2, 5],        # índices inválidos ('a', 'Portugal') são ignorados automaticamente
}

manipulador = ManipuladorPDF()
manipulador.processar_pdf(estrutura_dados)
manipulador.aplica_watermark('pdf_watermark.pdf', [0, 2])
manipulador.salvar_pdf('PDF_final.pdf')
```

**Saída esperada no terminal:**
```
-> Lendo pdf_exemplo.pdf: Total de páginas no arquivo: 3
 + Página 0 adicionada ao Writer.
-> Lendo pdf_exemplo2.pdf: Total de páginas no arquivo: 5
 + Página 0 adicionada ao Writer.
 + Página 1 adicionada ao Writer.
 + Página 2 adicionada ao Writer.
 + Marca d'agua aplicada na página 0.
 + Marca d'agua aplicada na página 2.
Marca d'agua aplicada com sucesso nas páginas: [0, 2].
Salvando o PDF processado como 'PDF_final.pdf'...
PDF processado e salvo como 'PDF_final.pdf' com sucesso.
```

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.x instalado
- Biblioteca `PyPDF2` instalada

### Instalação da dependência

```bash
pip install PyPDF2
```

### Passos

```bash
# Clone o repositório
git clone https://github.com/talesreis27/Projeto-Manipulador-de-PDF.git

# Acesse a pasta do projeto
cd Projeto-Manipulador-de-PDF

# Execute o script
python projeto_manipulador_de_Pdf.py
```

> **Atenção:** Antes de executar, certifique-se de que os arquivos PDF de entrada (`pdf_exemplo.pdf`, `pdf_exemplo2.pdf`, etc.) e o arquivo de marca d'água (`pdf_watermark.pdf`) estão na mesma pasta do script, ou ajuste os caminhos no dicionário `estrutura_dados`.

---

## ⚠️ Tratamento de Erros

| Situação | Comportamento |
|----------|---------------|
| Arquivo PDF não encontrado | Exibe `[ERRO]` e pula para o próximo |
| Índice de página inválido (fora do range ou não inteiro) | Exibe `[AVISO]` e remove o índice inválido |
| Arquivo de watermark não encontrado | Exibe `[ERRO]` e cancela a aplicação da marca d'água |
| Permissão negada ao salvar | Exibe `[ERRO]` com instrução de verificação |
| Caminho de saída é um diretório | Exibe `[ERRO]` solicitando um nome de arquivo válido |
| Erro inesperado | Capturado e exibido via `Exception` genérica |

---

## 📁 Arquivos do Repositório

```
Projeto-Manipulador-de-PDF/
├── projeto_manipulador_de_Pdf.py   # Código-fonte principal
├── LICENSE                          # Licença MIT
└── README.md                        # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **[PyPDF2](https://pypdf2.readthedocs.io/)** — leitura, escrita e manipulação de arquivos PDF

> 💡 **Nota do autor:** Para adicionar texto ou imagens a um PDF, bibliotecas como **ReportLab** ou **FPDF2** são mais indicadas, pois o PyPDF2 é focado na manipulação de páginas existentes.

---

## 💡 Conceitos Praticados

- Programação Orientada a Objetos (POO)
- Leitura e escrita de arquivos binários (PDF)
- Validação de entradas e tratamento robusto de exceções
- Manipulação de estruturas de dados (dicionários, listas)
- Uso de bibliotecas externas para processamento de documentos

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) — sinta-se livre para usar, modificar e distribuir.

---

## 👤 Autor

**Tales Reis e Silva**  
GitHub: [@talesreis27](https://github.com/talesreis27)
