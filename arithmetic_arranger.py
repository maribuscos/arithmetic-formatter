def arithmetic_arranger(problems, answer=False):
  # Check if the number of problems is greater than 5
  if len(problems) > 5:
    return "Error: Too many problems."

  # Initialize three empty lists to store first operand, operator and second operand of each problem
  first_operand = []
  second_operand = []
  operator = []

  # Split each problem into three parts and store in respective lists
  for problem in problems:
    pieces = problem.split()
    first_operand.append(pieces[0])
    operator.append(pieces[1])
    second_operand.append(pieces[2])

  # Check if the operator contains '*' or '/'
  if "*" in operator or "/" in operator:
    return "Error: Operator must be '+' or '-'."

  # Check if each operand contains only digits
  for i in range(len(first_operand)):
    if not (first_operand[i].isdigit() and second_operand[i].isdigit()):
      return "Error: Numbers must only contain digits."

  # Check if each operand is no more than 4 digits
  for i in range(len(first_operand)):
    if len(first_operand[i]) > 4 or len(second_operand[i]) > 4:
      return "Error: Numbers cannot be more than four digits."

  # Initialize four empty lists to store the first, second, third and fourth lines of the formatted problem
  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  # Add first operand to the first line with proper spacing
  for i in range(len(first_operand)):
    if len(first_operand[i]) > len(second_operand[i]):
      first_line.append(" " * 2 + first_operand[i])
    else:
      first_line.append(" " *
                        (len(second_operand[i]) - len(first_operand[i]) + 2) +
                        first_operand[i])

  # Add operator and second operand to the second line with proper spacing
  for i in range(len(second_operand)):
    if len(second_operand[i]) > len(first_operand[i]):
      second_line.append(operator[i] + " " + second_operand[i])
    else:
      second_line.append(operator[i] + " " *
                         (len(first_operand[i]) - len(second_operand[i]) + 1) +
                         second_operand[i])

  # Add a line of dashes to the third line with proper spacing
  for i in range(len(first_operand)):
    third_line.append("-" *
                      (max(len(first_operand[i]), len(second_operand[i])) + 2))

  # If the answer is requested, calculate the answer and add to the fourth line with proper spacing
  if answer:
    for i in range(len(first_operand)):
      if operator[i] == "+":
        # Perform addition if the operator is '+'
        ans = str(int(first_operand[i]) + int(second_operand[i]))
      else:
        # Perform subtraction if the operator is '-'
        ans = str(int(first_operand[i]) - int(second_operand[i]))

      if len(ans) > max(len(first_operand[i]), len(second_operand[i])):
        # Store the answer with a leading space if its length is greater than the maximum length of the operands
        fourth_line.append(" " + ans)
      else:
        # Store the answer with leading spaces so that it is aligned with the operands
        fourth_line.append(
          " " *
          (max(len(first_operand[i]), len(second_operand[i])) - len(ans) + 2) +
          ans)
  # Join the lists of strings into a single string with '    ' as the separator
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(
      second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(
        fourth_line)
  else:
    # Join the lists of strings into a single string with '    ' as the separator, without the answer line
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(
      second_line) + "\n" + "    ".join(third_line)


# Return the final string
  return arranged_problems
