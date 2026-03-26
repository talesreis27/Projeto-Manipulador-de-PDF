#pip install PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import os

class ManipuladorPDF:
    def __init__(self):
        self.writer = PdfWriter()
    # O metodo processar_pdf percorre o dicionario, valida a existencia do ficheiro e os indices das paginas, e adiciona as paginas validas ao writer.
    def processar_pdf(self, estrutura_dados):
        # estrutura_dados e um dicionario onde as chaves sao os nomes dos ficheiros pdf e os valores sao listas de indices das paginas a serem processadas.
        for file_name, pages in estrutura_dados.items():
            if not os.path.exists(file_name):
                print(f"[ERRO]: {file_name} não existe.")
                continue
            # O metodo PdfReader e usado para ler o ficheiro pdf, e o PdfWriter e usado para criar um novo ficheiro pdf com as paginas selecionadas.
            try:
                reader = PdfReader(file_name)
                print(f"-> Lendo {file_name}: Total de páginas no arquivo: {len(reader.pages)}")

                #Validacao dos indices do pdf
                valid_pages = [p for p in pages if isinstance(p,int)]
                if not valid_pages:
                    print(f"[ERRO]: O ficheiro '{file_name}' nao tem paginas validas.")
                    continue
                if len(valid_pages) < len(pages):
                    print(f"[AVISO]: foram removidas paginas invalidas do ficheiro '{file_name}'.")
                for indices in valid_pages:
                    if 0 <= indices < len(reader.pages):
                        self.writer.add_page(reader.pages[indices])
                        print(f"   + Página {indices} adicionada ao Writer.")
                    else:
                        print(f"[ERRO]: O indice da pagina '{indices}' no ficheiro '{file_name}' esta fora do intervalo.")
            # O bloco try-except e usado para capturar e exibir erros que possam ocorrer durante a leitura do ficheiro pdf, como problemas de formato ou arquivos corrompidos.
            except Exception as e:
                    print(f"[ERRO]: Erro ao ler o ficheiro '{file_name}': {str(e)}")
    # O metodo aplica_watermark recebe o nome do ficheiro de marca d'agua, valida a existencia do ficheiro e aplica a marca d'agua nas paginas selecionadas.
    def aplica_watermark(self, watermark_file, indices_alvo):
        if not os.path.exists(watermark_file):
            print(f"[ERRO]: O ficheiro de marca d'agua '{watermark_file}' nao foi encontrado.")
            return
        try:
            watermark_reader = PdfReader(watermark_file)
            watermark_page = watermark_reader.pages[0]
            new_writer = PdfWriter()
            for indice, page in enumerate(self.writer.pages):
                if indice in indices_alvo:
                    page.merge_page(watermark_page)
                    print(f"   + Marca d'agua aplicada na página {indice}.")
                output_page = PdfWriter()
                output_page.add_page(page)
                new_writer.add_page(output_page.pages[0])
            self.writer = new_writer
            print(f"Marca d'agua aplicada com sucesso nas páginas: {indices_alvo}.")
        # O bloco try-except e usado para capturar e exibir erros que possam ocorrer durante a leitura do ficheiro de marca d'agua ou durante o processo de aplicacao da marca d'agua nas paginas selecionadas.
        except Exception as e:
            print(f"[ERRO]: Erro ao aplicar a marca d'agua: {str(e)}")
    # O metodo salvar_pdf recebe o nome do ficheiro de saida, e salva o novo ficheiro pdf com as paginas selecionadas e a marca d'agua aplicada.  
    def salvar_pdf(self, output_filename):
        with open(output_filename, 'wb') as f:
            self.writer.write(f)
        print (f"PDF processado e salvo como '{output_filename}' com sucesso.")

#Exemplo de uso
if __name__ == "__main__":
    estrutura_dados = { 
        'pdf_exemplo.pdf': [0],
        'pdf_exemplo2.pdf': [0, 1, 2],
        'pdf_exemplo3.pdf': [2, 'a',5,'Portugal']
    }
    manipulador = ManipuladorPDF()
    manipulador.processar_pdf(estrutura_dados)
    manipulador.aplica_watermark('pdf_watermark.pdf', [0, 1, 2, 3, 4, 5, 6])
    manipulador.salvar_pdf('PDF_final.pdf')

    #DESAFIO 
    # para adicionar texto e imagens a um PDF , o mais adequado seria usar outra biblioteca 
    # como o Repotlab ou FPDF2, assim sendo mais facil e pretico adicinoar textos e imagens a um PDF,
    #  ja que o PyPDF2 e mais focado em manipular paginas existentes do que criar novas paginas ou adicionar conteudo.

                