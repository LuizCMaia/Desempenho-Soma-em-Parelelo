import os
import concurrent.futures

def somar_chunk_binario(linhas):
    """
    Recebe uma lista de strings binárias (um 'pedaço' do arquivo), 
    converte para inteiro e retorna a soma parcial desse pedaço.
    """
    soma_parcial = 0
    for linha in linhas:
        linha = linha.strip()
        if linha:
            # Converte de binário (base 2) para decimal e soma
            soma_parcial += int(linha, 2)
    return soma_parcial

def dividir_em_chunks(lista, n_chunks):
    """Divide uma lista de dados em N pedaços mais ou menos do mesmo tamanho."""
    # Garante que o tamanho do chunk seja pelo menos 1
    tamanho_chunk = max(1, len(lista) // n_chunks)
    return [lista[i : i + tamanho_chunk] for i in range(0, len(lista), tamanho_chunk)]

if __name__ == '__main__':
    # Obtém o diretório exato onde este script .py está salvo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, 'numero2.txt')
    
    # Número de threads/núcleos lógicos do seu processador
    threads_disponiveis = 12

    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        print("Certifique-se de que o nome está correto e na mesma pasta do script.")
    else:
        print("Lendo o arquivo...")
        # 1. Carrega todo o arquivo para a memória
        with open(caminho_arquivo, 'r') as f:
            todas_as_linhas = f.readlines()

        total_linhas = len(todas_as_linhas)
        print(f"Arquivo carregado com sucesso. Total de linhas: {total_linhas}")

        if total_linhas == 0:
            print("O arquivo está vazio.")
        else:
            # 2. Divide as linhas em 12 partes
            chunks_de_dados = dividir_em_chunks(todas_as_linhas, threads_disponiveis)
            print(f"Dividindo o processamento em {len(chunks_de_dados)} processos paralelos...")

            soma_total_decimal = 0
            
            # 3. Processamento paralelo usando todos os núcleos
            with concurrent.futures.ProcessPoolExecutor(max_workers=threads_disponiveis) as executor:
                # Dispara a função 'somar_chunk_binario' para cada pedaço de dados simultaneamente
                resultados_parciais = executor.map(somar_chunk_binario, chunks_de_dados)
                
                # Junta (soma) os resultados que vieram de cada núcleo
                for resultado in resultados_parciais:
                    soma_total_decimal += resultado

            print("-" * 40)
            print(f"Soma total (Decimal): {soma_total_decimal}")
            # Transforma o resultado final de volta para binário (removendo o '0b' da frente)
            print(f"Soma total (Binário): {bin(soma_total_decimal)[2:]}")
            print("-" * 40)