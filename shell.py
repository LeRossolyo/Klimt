from unittest import result
import basic

while True:
  text = input('Klimt > ')
  result, error = basic.run('stdin', text)

  if error: print(error.as_string())
  else: print(result)