"""
P(h1) - got m1 coin = 0.2
P(h2) - got m2 coin = 0.2
P(h3) - got m3 coin = 0.2
P(h4) - got m4 coin = 0.2
P(h5) - got m5 coin = 0.2


Ph1(A) - got "H" = 0.1
Ph1(A) - got "H" = 0.2
Ph1(A) - got "H" = 0.4
Ph1(A) - got "H" = 0.8
Ph1(A) - got "H" = 0.9

P(A) = 0.2 * 0.1 + 0.2 * 0.2 + 0.2 * 0.4 + 0.2 * 0.8 + 0.2 * 0.9 = 0.48 # :)

Pa(h1) = (0.2 * 0.1) / 0.48
Pa(h2) = (0.2 * 0.2) / 0.48
Pa(h3) = (0.2 * 0.4) / 0.48
Pa(h4) = (0.2 * 0.8) / 0.48
Pa(h5) = (0.2 * 0.9) / 0.48

>>> p = [(0.2 * 0.1) / 0.48, (0.2 * 0.2) / 0.48, (0.2 * 0.4) / 0.48, (0.2 * 0.8) / 0.48, (0.2 * 0.9) / 0.48]
>>> 
>>> p
[0.04166666666666668, 0.08333333333333336, 0.1666666666666667, 0.3333333333333334, 0.37500000000000006]
>>> sum(i * j for i, j in zip(p, [0.1,0.2,0.4,0.8,0.9]))
0.6916666666666669 # HELL YEAH
"""
import numpy as np

POSSIBILITIES = {'H': [0.1, 0.2, 0.4, 0.8, 0.9], 'T': [0.9, 0.8, 0.6, 0.2, 0.1]}


def full_probability(coin_probabilities: list[float], event_probabilities: list[float]) -> float:
    return sum(
        coin_probability * event_probability
        for coin_probability, event_probability in zip(coin_probabilities, event_probabilities)
    )


def bayes(coin_possibility: float, event_possibility: float, full_possibility: float) -> float:
    return (coin_possibility * event_possibility) / full_possibility


def get_possibility_of_sequence(
    sequence: list[str], number_of_coins: int, possibilities: dict = POSSIBILITIES
) -> list[float]:
    result_possibilities = []
    coin_possibilities = [1 / number_of_coins] * number_of_coins
    for side in sequence:
        result_possibilities.append(full_probability(coin_possibilities, possibilities[side]))
        coin_possibilities = [
            bayes(coin_possibilities[item], possibilities[side][item], result_possibilities[-1])
            for item in range(number_of_coins)
        ]

    return result_possibilities


if __name__ == '__main__':
    sequence = list('HHHTHTHH')
    number_of_coins = 5
    print(get_possibility_of_sequence(sequence, number_of_coins))
