def arithmetic_arranger(problems, t=False):
  if len(problems) > 5:
      return "Error: Too many problems."

  arranged_problems = []
  results = []

  for problem in problems:
      operands, operator = problem.split(), problem.split()[1]

      if operator not in "+-":
          return "Error: Operator must be '+' or '-'."

      operand1, operand2 = operands[0], operands[2]

      if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."

      if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."

      max_width = max(len(operand1), len(operand2)) + 2

      if operator == "+":
          result = str(int(operand1) + int(operand2))
      else:
          result = str(int(operand1) - int(operand2))

      arranged_problem = []
      arranged_problem.append(operand1.rjust(max_width))
      arranged_problem.append(operator + operand2.rjust(max_width - 1))
      arranged_problem.append('-' * max_width)
      results.append(result.rjust(max_width))

      arranged_problems.append(arranged_problem)

  arranged_output = ['    '.join(p) for p in zip(*arranged_problems)]
  result_line = '    '.join(results)

  if t:
      return '\n'.join([*arranged_output, result_line])
  else:
      return '\n'.join(arranged_output)

