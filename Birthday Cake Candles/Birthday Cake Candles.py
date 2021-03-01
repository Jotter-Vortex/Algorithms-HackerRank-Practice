# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(candles):
    tallest=max(candles)
    return candles.count(tallest)