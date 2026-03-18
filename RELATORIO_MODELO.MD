# Relatório da NOME DA ATIVIDADE

**Disciplina: Sistemas de Informação** 
**Aluno(s): Luiz Miguel Caixêta Maia**
**Turma: Sistemas de Informação - Noturno**
**Professor: Rafael Marques**
**Data: 18/03/2026**

---

# 1. Descrição do Problema

O problema computacional resolvido consiste na leitura, conversão de base numérica e soma de um grande volume de números binários armazenados em um arquivo de texto. Como a conversão de strings na base 2 para inteiros decimais e a sua subsequente soma é uma operação custosa para a CPU quando executada em larga escala, o objetivo primário da paralelização é reduzir o tempo total de execução.Foi utilizado um algoritmo com a abordagem de Divisão e Conquista. O conjunto total de dados (linhas do arquivo) é fatiado em partes aproximadamente iguais (chunks). Cada parte é enviada para um processo separado que realiza as conversões e calcula uma soma local simultaneamente aos demais. Ao final, a aplicação consolida (reduz) as somas locais em um único valor final. A complexidade do algoritmo é $O(N)$, onde $N$ representa o número total de linhas do arquivo.

---

# 2. Ambiente Experimental

| Item                        |   Descrição   |
| Processador                 |    I5-12500   |
| Número de núcleos           |      6/12     |
| Memória RAM                 | 16GB 4800MHZ  |
| Sistema Operacional         |   Windows 11  |
| Linguagem utilizada         |    Python 3   |
| Biblioteca de paralelização |   concurrent.futures (ProcessPoolExecutor)  |
| Compilador / Versão         |   VSCode  |

--=

# 3. Metodologia de Testes

Para garantir rigor nas medições, a operação de leitura em disco (I/O) foi separada da operação matemática. O arquivo inteiro é carregado para a memória RAM primariamente, garantindo que o tempo de execução medido reflita exclusivamente o processamento da CPU e a sobrecarga (overhead) da criação dos processos.

O tempo de execução foi cronometrado utilizando a função time.perf_counter() nativa do Python, que possui a maior resolução disponível no sistema para medir intervalos curtos. Cada configuração de paralelismo (1, 2, 4, 8 e 12 processos) foi executada 5 vezes consecutivas. O valor anotado nas tabelas subsequentes representa a média aritmética simples dessas 5 execuções. O volume de entrada utilizado consistiu em [COLOQUE O NÚMERO DE LINHAS QUE O TERMINAL IMPRIMIU] números binários.

# 4. Resultados Experimentais


# 5. Cálculo de Speedup e Eficiência

## Fórmulas Utilizadas

### Speedup

```
Speedup(p) = T(1) / T(p)
```

Onde:

* **T(1)** = tempo da execução serial
* **T(p)** = tempo com p threads/processos

### Eficiência

```
Eficiência(p) = Speedup(p) / p
```

Onde:

* **p** = número de threads ou processos

---

# 6. Tabela de Resultados

Preencha a tabela abaixo utilizando os tempos medidos.

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
| ----------------- | --------- | ------- | ---------- |
| 1                 |           | 1.0     | 1.0        |
| 2                 |           |         |            |
| 4                 |           |         |            |
| 8                 |           |         |            |
| 12                |           |         |            |

---

# 7. Gráfico de Tempo de Execução

Construa um gráfico mostrando o **tempo de execução em função do número de threads/processos**.

## Orientações

* Eixo X: número de threads/processos
* Eixo Y: tempo de execução (segundos)

Inserir o gráfico abaixo:

![Gráfico Tempo Execução](graficos/tempo_execucao.png)

---

# 8. Gráfico de Speedup

Construa um gráfico mostrando o **speedup obtido**.

## Orientações

* Eixo X: número de threads/processos
* Eixo Y: speedup
* Incluir também a **linha de speedup ideal (linear)** para comparação

Inserir o gráfico abaixo:

![Gráfico Speedup](graficos/speedup.png)

---

# 9. Gráfico de Eficiência

Construa um gráfico mostrando a **eficiência da paralelização**.

## Orientações

* Eixo X: número de threads/processos
* Eixo Y: eficiência
* Valores entre 0 e 1

Inserir o gráfico abaixo:

![Gráfico Eficiência](graficos/eficiencia.png)

---

# 10. Análise dos Resultados

Realize uma análise crítica dos resultados obtidos.

## Questões a serem respondidas

* O speedup obtido foi próximo do ideal?
* A aplicação apresentou escalabilidade?
* Em qual ponto a eficiência começou a cair?
* O número de threads ultrapassa o número de núcleos físicos da máquina?
* Houve overhead de paralelização?

Discutir possíveis causas para:

* perda de desempenho
* gargalos no algoritmo
* sincronização entre threads/processos
* comunicação entre processos
* contenção de memória ou cache

---

# 11. Conclusão

Apresente as conclusões do experimento.

## Sugestões de pontos a comentar

* O paralelismo trouxe ganho significativo de desempenho?
* Qual foi o melhor número de threads/processos?
* O programa escala bem com o aumento do paralelismo?
* Quais melhorias poderiam ser feitas na implementação?

---
