# Relatório Técnico: Algoritmo de Ordenação Min-Max Bidirecional (TP1 - APA)

**Disciplina:** Análise e Projeto de Algoritmos (APA)  
**Aluno:** Gustavo Borges Arrussul Veiga
**Repositório:** [GitHub - apa-tp1-ordenacao](https://github.com/GustavoArrussul/apa-tp1-ordenacao)  

---

## 1. Introdução e Intuição do Algoritmo

O presente relatório detalha a concepção, a fundamentação teórica, a implementação e a avaliação experimental do algoritmo autoral **Min-Max Bidirecional**, desenvolvido no âmbito do Trabalho Prático 1 (TP1). 

A intuição fundamental do algoritmo reside na otimização do espaço de varredura e do número de iterações do laço de controle em comparação com métodos de seleção unidirecionais clássicos (como o *Selection Sort* tradicional). Enquanto o método clássico examina a entrada iterativamente para encontrar apenas um extremo por passada (avançando uma única extremidade por vez), o **Min-Max Bidirecional** realiza uma varredura linear simultânea e convergente para identificar **ambos os extremos** (o menor e o maior elemento) do subvetor ativo em uma única passada. 

Esses elementos são imediatamente posicionados em suas localizações definitivas nas extremidades esquerda (`left`) e direita (`right`), reduzindo o espaço de busca simetricamente em duas unidades por iteração e cortando o número de ciclos do laço externo pela metade ($\approx N/2$ iterações).

---

## 2. Especificação Formal, Estratégia e Invariantes

### Descrição da Estratégia
O algoritmo opera utilizando dois ponteiros delimitadores, `left` (inicializado em $0$) e `right` (inicializado em $n - 1$). A cada ciclo do laço principal ($left < right$):
1. **Varredura Simultânea:** Percorre-se o subvetor ativo de `left + 1` até `right` para rastrear simultaneamente o índice do menor elemento (`min_idx`) e do maior elemento (`max_idx`).
2. **Tratamento de Colisão de Índices:** Caso o elemento máximo estivesse localizado exatamente na posição `left` original, o ponteiro de rastreio do máximo é atualizado corretamente para evitar perda de referência após a troca do menor elemento.
3. **Posicionamento Físico (*In-place*):** Efetuam-se as trocas necessárias para colocar o menor elemento na extremidade esquerda e o maior na extremidade direita.
4. **Contração Simétrica:** Os ponteiros internos avançam em direção ao centro (`left += 1`, `right -= 1`).

### Invariante de Laço
*No início de cada iteração do laço principal, os segmentos do vetor situados estritamente à esquerda de `left` e estritamente à direita de `right` encontram-se ordenados e contêm os menores e maiores elementos globais da entrada em suas posições finais definitivas.*

---

## 3. Análise Teórica de Complexidade ($O, \Omega, \Theta$)

* **Pior Caso ($O$) e Caso Médio ($\Theta$):** $O(N^2)$. Embora o número de iterações do laço externo seja reduzido para $\approx N/2$, a varredura linear interna para a busca dos extremos em cada ciclo ainda consome uma quantidade linear de operações proporcionais ao tamanho remanescente de $N$, mantendo a classe assintótica quadrática.
* **Melhor Caso ($\Omega$):** $\Omega(N^2)$ estruturalmente nas comparações da varredura linear de busca de extremos, uma vez que o algoritmo inspeciona o subvetor ativo independentemente da ordenação prévia dos elementos internos.
* **Complexidade de Espaço Auxiliar:** $O(1)$ (*in-place*), pois o algoritmo opera modificando diretamente a estrutura de dados de entrada, utilizando apenas um conjunto estritamente constante de variáveis escalares para controle de índices e contadores.

---

## 4. Resultados Experimentais e Discussão

Os testes práticos foram conduzidos utilizando a suíte de benchmark integrada ao repositório, que compara o **Min-Max Bidirecional (Autoral)** frente a algoritmos clássicos (*Bubble Sort*, *Selection Sort*, *Insertion Sort*, *Merge Sort* e *Quick Sort*). A avaliação cobriu cinco distribuições distintas de dados (`random`, `sorted`, `reverse`, `duplicates`, `almost_sorted`) com tamanhos de entrada variando de $N = 10$ a $N = 1000$ com múltiplas repetições (*trials*).

### Análise de Desempenho e Comportamento Gráfico (`benchmark_results.png`)
* **Eficiência Operacional:** O gráfico comparativo e os dados tabulares em Markdown evidenciam que a varredura bidirecional simultânea reduz o overhead de iterações externas em comparação direta com o *Selection Sort* clássico.
* **Robustez e Estabilidade:** A validação automatizada de sanidade garantiu que 100% dos testes unitários obrigatórios (vetores vazios, unitários, ordenados, reversos, duplicados e aleatórios) foram aprovados com sucesso, atestando a corretude lógica da implementação sob quaisquer condições de contorno.

---

## 5. Conclusão e Trabalhos Futuros

O desenvolvimento e a validação do algoritmo **Min-Max Bidirecional** permitiram aprofundar conceitos avançados de projeto de algoritmos, manipulação rigorosa de invariantes e análise de desempenho experimental.  O código encontra-se totalmente integrado ao template
acadêmico, documentado e versionado no GitHub.

---

## 6. Declaração de Autoria e Ferramentas de Apoio

A concepção lógica, depuração e a estrutura fundamental do código foram
desenvolvidas por mim. Assistentes de Inteligência Artificial foram utilizados como
suporte técnico auxiliar na formatação de scripts e na estruturação textual deste
relatório técnico. Ferramentas de Inteligência Artificial foram consultadas de forma pontual e estritamente restritas ao suporte auxiliar para esclarecimento de dúvidas de sintaxe em Python e na revisão textual deste relatório técnico.