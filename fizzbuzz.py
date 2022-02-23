class Solution:
    def fizzBuzz(n):
        solutionArray = []
        for i in range(1, n + 1): 
            if i % 3 and i % 5 == 0:
                solutionArray.append('FizzBuzz')
                continue
            elif i % 3 == 0:
                solutionArray.append('Fizz')
                continue
            elif i % 5 == 0:
                solutionArray.append('Buzz')
                continue
            else:
                solutionArray += str(i)

print(Solution.fizzBuzz(5))