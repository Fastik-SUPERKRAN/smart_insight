"""Calculate possibilities of flipping a coin."""


def full_probability(coin_probabilities: list[float], event_probabilities: list[float]) -> float:
    """Calculate full probability of flipping a coin and getting desired side.

    Parameters
    ----------
    coin_probabilities : list of float
        Probabilities of choosing certain coin.
    event_probabilities : list of float
        Probabilities of getting desired side for each coin.

    Returns
    -------
    float
        Probability of getting desired side.
    """
    return sum(
        coin_probability * event_probability
        for coin_probability, event_probability in zip(coin_probabilities, event_probabilities)
    )


def bayes(coin_possibility: float, event_possibility: float, full_possibility: float) -> float:
    """Get next probability of choosing certain coin.

    Parameters
    ----------
    coin_possibility : float
        Previous possibility of choosing this coin.
    event_possibility : float
        Possibility of getting desired side using this coin.
    full_possibility : float
        Probability of getting desired side.

    Returns
    -------
    float
        Next probability of choosing certain coin.
    """
    return (coin_possibility * event_possibility) / full_possibility


def get_possibility_of_sequence(sequence: list[str], number_of_coins: int, possibilities: dict) -> list[float]:
    """Get possibility of sequence of events.

    Parameters
    ----------
    sequence : list of str
        The sequence for which the possibilities will be calculated.
    number_of_coins : int
        Number of coins we can choose for flipping.py
    possibilities : dict
        Possibilities of getting desired side for each coin.

    Returns
    -------
    list of float
        Step by step possibilities of getting desired side.

    Raises
    ------
    ValueError
        If number of coins is less than 1.
    """
    if number_of_coins < 1:
        raise ValueError(f'Number of coins({number_of_coins}) is less than 1.')

    result_possibilities = []

    # possibility of choosing certain coin at first step
    coin_possibilities = [1 / number_of_coins] * number_of_coins

    for side in sequence + ['H']:
        result_possibilities.append(full_probability(coin_possibilities, possibilities['H']))

        # update possibilities of choosing certain coin
        coin_possibilities = [
            bayes(
                coin_possibilities[item],
                possibilities[side][item],
                full_probability(coin_possibilities, possibilities[side]),
            )
            for item in range(number_of_coins)
        ]

    return result_possibilities[1:]


if __name__ == '__main__':
    coin_possibilities_of_H = [0.1, 0.2, 0.4, 0.8, 0.9]
    coin_possibilities = {'H': coin_possibilities_of_H, 'T': [1 - item for item in coin_possibilities_of_H]}

    sequence = list('HHHTHTHH')

    number_of_coins = 5

    print([round(item, 2) for item in get_possibility_of_sequence(sequence, number_of_coins, coin_possibilities)])
