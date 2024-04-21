
def get_color():
    colors=["red","green","blue","yellow"]
    print("pick a color from the list:red,green,blue or yellow")
    choice =input(" >").lower()
    while choice not in list:
     print("sorry wrong answer try again")
     choice=input(" >").lower()
    return choice
def get_number(color):
 if len(color) in [3,6]:
   number=("1","2","3","4")
 else:
   numbers=("5","6","7","8")
   print("pick a number{number[::0]}")
   choice=input(" >")
 return int(choice)
def get_fortune(color,number):
  fortunes = {
      "red": {
           1: "Great passion awaits you!",
            2: "Your anger might lead you astray. Be calm.",
            5: "Success is within reach if you act boldly.",
            6: "Love is blossoming around you. Open your heart."
        },
        "green": {
            1: "Growth and new beginnings are on the horizon.",
            2: "Envy can cloud your judgment. Focus on yourself.",
            5: "Financial security is coming your way.",
            6: "Reconnect with nature for peace and clarity."
        },
        "blue": {
            3: "Knowledge is power. Keep learning and exploring.",
            4: "Speak your truth with confidence. Be heard.",
            7: "Travel and adventure await the curious soul.",
            8: "Find peace and tranquility within yourself."
        },
        "yellow": {
            3: "Your creativity is overflowing. Share your talents.",
            4: "Optimism is key. Stay positive and attract good things.",
            7: "Joy and laughter fill your days. Embrace happiness.",
            8: "Be a beacon of light for those around you."


      }
  }
  return get_fortune[color][number]
def main():
    """
    Runs the fortune teller program
    """
    color = get_color()
    number = get_number(color)
    fortune = get_fortune(color, number)

    print(f"\nYour fortune for the day: {fortune}")

if __name__ == "__main__":
    main()
