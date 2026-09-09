# Relatório Técnico: Algoritmo de Ordenação Min-Max Bidirecional (TP1 - APA)

**Disciplina:** Análise e Projeto de Algoritmos (APA)  
**Aluno:** Gustavo Arrussul
**Repositório:** [GitHub - apa-tp1-ordenacao](https://github.com/GustavoArrussul/apa-tp1-ordenacao)  

---

## 1. Introdução e Intuição do Algoritmo

O presente relatório detalha o desenvolvimento, a fundamentação teórica e a avaliação experimental do algoritmo autoral **Min-Max Bidirecional**, desenvolvido no âmbito do Trabalho Prático 1 (TP1). 

A intuição por trás do algoritmo baseia-se na otimização da varredura linear tradicional de ordenação por seleção ou troca. Enquanto algoritmos clássicos como o *Selection Sort* buscam apenas o menor elemento a cada passo (avançando uma única extremidade por vez), o **Min-Max Bidirecional** realiza uma varredura simultânea para identificar **ambos os extremos** (o menor e o maior elemento) do subvetor ativo em uma única passada. Os elementos extremos encontrados são imediatamente posicionados em suas posições definitivas nas extremidades esquerda e direita, reduzindo o espaço de busca de forma simétrica em $2 unidades por iteração.

---

## 2. Especificação Formal e Invariantes

### Descrição da Estratégia
O algoritmo opera utilizando dois ponteiros delimitadores, `left` (inicializado em $0$) e `right` (inicializado em $n - 1$). A cada ciclo do laço principal ($left < right$):
1. Varre-se o intervalo de índices de `left + 1` até `right` para localizar simultaneamente o índice do valor mínimo (`min_idx`) e do valor máximo (`max_idx`).
2. Tratam-se colisões de índices (caso o valor máximo estivesse na posição `left` original).
3. Realiza-se a troca física do menor elemento para a posição `left` e do maior elemento para a posição `right`.
4. Atualizam-se os ponteiros internos avançando `left` em $+1$ e recuando `right` em $-1$.

### Invariante de Laço
*No início de cada iteração do laço principal, o subvetor à esquerda de `left` e à direita de `right` contém os menores e maiores elementos globais da entrada, devidamente ordenados em suas posições finais definitivas.*

---

## 3. Análise Teórica de Complexidade ($O, \Omega, \Theta$)

* **Pior Caso ($O$) e Caso Médio ($\Theta$):** $O(N^2)$. No pior caso (vetor em ordem reversa ou desordenado aleatoriamente), o número de comparações e movimentações segue uma progressão quadrática em função do tamanho da entrada $N$, uma vez que a varredura linear interna consome proporcionalmente $N$ passos decrescentes.
* **Melhor Caso ($\Omega$):** $\Omega(N^2)$ estruturalmente nas comparações da varredura linear básica, porém otimizado em termos práticos de fluxo por varreduras de variação de extremos.
* **Complexidade de Espaço Auxiliar:** $O(1)$ (*in-place*), pois o algoritmo opera diretamente sobre a estrutura de dados original com alocação estritamente constante de variáveis auxiliares de controle de índices.

---

## 4. Resultados Experimentais e Discussão

Os testes práticos foram executados através da suíte de benchmark integrada ao repositório, comparando o **Min-Max Bidirecional (Autoral)** com os algoritmos clássicos (*Bubble Sort*, *Selection Sort*, *Insertion Sort*, *Merge Sort* e *Quick Sort*) em diferentes distribuições de dados (*Random*, *Sorted*, *Reverse*, *Duplicates*, *Almost Sorted*) para tamanhos de entrada variando de $N = 10$ até $N = 1000$.

### Análise do Gráfico (`benchmark_results.png`)
* **Comportamento em Entradas Aleatórias e Reversas:** O algoritmo autoral exibe curvas de desempenho consistentes com a classe de complexidade quadrática, mantendo-se competitivo em termos de número de operações de varredura simultânea de extremos por ciclo.
* **Estabilidade:** A validação de sanidade executada em lote confirmou que 100% dos testes unitários e de benchmark foram superados sem discrepâncias de ordenação em nenhuma das distribuições avaliadas.

---

## 5. Conclusão

O desenvolvimento do algoritmo **Min-Max Bidirecional** permitiu consolidar conceitos fundamentais de projeto de algoritmos, manipulação eficiente de ponteiros *in-place* e validação experimental rigorosa. O código encontra-se totalmente integrado ao template acadêmico, documentado e versionado no GitHub.

---

## 6. Declaração de Autoria e Ferramentas de IA

A concepção lógica, depuração e a estrutura fundamental do código foram desenvolvidas por mim. Assistentes de Inteligência Artificial foram utilizados como suporte técnico auxiliar na formatação de scripts e na estruturação textual deste relatório técnico.