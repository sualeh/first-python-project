"""Defines mean module."""
import pandas as pd


def mean(data) -> float:
    """Return the mean of a list of numbers.

    If no list is provided, or an empty list is provided,
    None (no mean) is returned.
    Otherwise, the mean of the list is returned as float value.

        Parameters:
            data (list[int]): A list of integers

        Returns:
            mean (float): Mean of the list of integers

        Raises
            TypeError: If data is not a list of integers
    """
    if data is None:
        return None
    if len(data) == 0:
        return None
    data_series = pd.Series(data)
    return data_series.mean()


def main():
    """Define main routine that runs mean function with some sample data."""
    a = [1, 7, 2]
    print(mean(a))


# Run main
if __name__ == '__main__':
    main()
