def calculate_income(summ, rate, period):
    """
      >>> calculate_income(700000, 8, 12)
      758100

      :param summ:
      :param rate:
      :param period:
      :return:
    """

    temp = rate / 1200.

    for i in range(period):
        summ = summ + (summ * temp)

    return round(summ)
