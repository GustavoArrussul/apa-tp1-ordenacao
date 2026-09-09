"""
TEMPLATE PARA O ALUNO — TRABALHO PRÁTICO 1 (TP1)
Disciplina: Análise e Projetos de Algoritmos (APA)

Instruções:
1. Implemente seu método de ordenação autoral na função `my_authorial_sort`.
2. O retorno deve ser obrigatoriamente a tupla: (lista_ordenada, total_comparacoes, total_movimentacoes).
3. Execute este arquivo diretamente para rodar a suíte de testes de corretude e o benchmark rápido.
"""

from typing import Any, List, Tuple
import unittest


def my_authorial_sort(arr: List[Any]) -> Tuple[List[Any], int, int]:
    """
    Algoritmo Autoral: Min-Max Bidirecional Robusto
    """
    a = list(arr)
    n = len(a)
    comps = 0
    moves = 0

    left = 0
    right = n - 1

    while left < right:
        min_idx = left
        max_idx = left

        # Varredura para encontrar o menor e o maior no intervalo [left, right]
        for i in range(left + 1, right + 1):
            comps += 1
            if a[i] < a[min_idx]:
                min_idx = i

            comps += 1
            if a[i] > a[max_idx]:
                max_idx = i

        # Se o elemento mínimo já está na posição 'left' e o máximo na 'right',
        # e o intervalo interno estiver ordenado, podemos otimizar ou apenas prosseguir.

        # Posiciona o menor elemento na extremidade esquerda
        if min_idx != left:
            a[left], a[min_idx] = a[min_idx], a[left]
            moves += 2
            # Se o max_idx estava exatamente na posição 'left' que acabamos de trocar,
            # ele foi movido para a posição 'min_idx'. Atualizamos o rastreio dele.
            if max_idx == left:
                max_idx = min_idx

        # Posiciona o maior elemento na extremidade direita
        if max_idx != right:
            a[right], a[max_idx] = a[max_idx], a[right]
            moves += 2

        left += 1
        right -= 1

    return a, comps, moves


# =============================================================================
# SUÍTE DE TESTES AUTOMÁTICA DE VALIDAÇÃO
# =============================================================================
class TestStudentAuthorialSort(unittest.TestCase):
    def assert_sorted(self, original: List, result: List):
        self.assertEqual(len(result), len(original), "Tamanho divergente!")
        self.assertEqual(sorted(original), result, "A lista não foi ordenada corretamente!")

    def test_empty(self):
        res, _, _ = my_authorial_sort([])
        self.assert_sorted([], res)

    def test_single(self):
        res, _, _ = my_authorial_sort([99])
        self.assert_sorted([99], res)

    def test_sorted(self):
        data = list(range(100))
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_reverse(self):
        data = list(range(100, 0, -1))
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_identical(self):
        data = [5] * 50
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)

    def test_random(self):
        import random
        random.seed(42)
        data = [random.randint(-1000, 1000) for _ in range(200)]
        res, _, _ = my_authorial_sort(data)
        self.assert_sorted(data, res)


if __name__ == "__main__":
    print("🧪 Executando testes unitários no seu algoritmo autoral...")
    unittest.main(verbosity=2)
