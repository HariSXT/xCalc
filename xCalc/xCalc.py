import os
import time
import sys
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the screen
clear_screen()
ascii_art = """'##::::'##::'######:::::'###::::'##::::::::'######::
. ##::'##::'##... ##:::'## ##::: ##:::::::'##... ##:
:. ##'##::: ##:::..:::'##:. ##:: ##::::::: ##:::..::
::. ###:::: ##:::::::'##:::. ##: ##::::::: ##:::::::
:: ## ##::: ##::::::: #########: ##::::::: ##:::::::
: ##:. ##:: ##::: ##: ##.... ##: ##::::::: ##::: ##:
 ##:::. ##:. ######:: ##:::: ##: ########:. ######::
..:::::..:::......:::..:::::..::........:::......:::"""
print(ascii_art)
print("                -Made By HarisXT-")
def animated_loading(stop_condition):
  while not stop_condition():  # Loop until the stop condition is True
      for i in range(4):
          sys.stdout.write('\rLoading' + '.' * i)
          sys.stdout.flush()
          time.sleep(0.5)
  print("\nLoading stopped.")

# Example stop condition
def stop_condition():
  # Add your condition here
  # For example, stop after 10 seconds
  return time.time() > start_time + 10

# Start the loading animation
start_time = time.time()
animated_loading(stop_condition)
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the screen
clear_screen()
ascii_art = """'##::::'##::'######:::::'###::::'##::::::::'######::
. ##::'##::'##... ##:::'## ##::: ##:::::::'##... ##:
:. ##'##::: ##:::..:::'##:. ##:: ##::::::: ##:::..::
::. ###:::: ##:::::::'##:::. ##: ##::::::: ##:::::::
:: ## ##::: ##::::::: #########: ##::::::: ##:::::::
: ##:. ##:: ##::: ##: ##.... ##: ##::::::: ##::: ##:
##:::. ##:. ######:: ##:::: ##: ########:. ######::
..:::::..:::......:::..:::::..::........:::......:::"""
print(ascii_art)
print("                -Made By HarisXT-")
def calculate_percentage(numerator, denominator):
  # Check if denominator is not zero to avoid division by zero error
  if denominator != 0:
      percentage = (numerator / denominator) * 100
      return percentage
  else:
      return "Error: Denominator cannot be zero."

def main():
  numerator = float(input("Enter the numerator: "))
  denominator = float(input("Enter the denominator: "))

  percentage = calculate_percentage(numerator, denominator)
  if isinstance(percentage, float):
      print(f"The percentage is: {percentage:.2f}%")
  else:
      print(percentage)

if __name__ == "__main__":
  main()
time.sleep(5)
def animated_exiting(stop_condition):
  while not stop_condition():  # Loop until the stop condition is True
      for i in range(4):
          sys.stdout.write('\rExiting' + '.' * i)
          sys.stdout.flush()
          time.sleep(0.5)
  print("\nExiting stopped.")

# Example stop condition
def stop_condition():
  # Add your condition here
  # For example, stop after 10 seconds
  return time.time() > start_time + 5

# Start the loading animation
start_time = time.time()
animated_exiting(stop_condition)