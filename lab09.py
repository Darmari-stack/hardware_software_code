def print_lyrics():
  print ("I'm a programmer, and I'm okay.")
  print ("I code all night, and I code all day.")
def repeat_lyrics(count = 1):
  for number in range(count):
      print("{}".format(number))
      print_lyrics()
  print ("Done Repeating!!")
  print("{}############".format(number),end=".")
def main():
  repeat_lyrics()
  repeat_lyrics(4)
if __name__ == "__main__":
   main()
