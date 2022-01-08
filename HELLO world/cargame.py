command = ""
started = False



while command != "quit" or command != "QUIT":
      command = input(">").lower() or input(">").upper()
      if command == "start" or command == "START":
          if started:
              print("car is already started")
          else:
               started = True
               print("car started")
      elif command == "stop" or command == "STOP":
          if not started:
              print("car is already stopped")
          else:
               started = False
               print("car stopped")
      elif command == "help" or command == "HELP":
          print("""
START - TO START THE CAR
STOP - TO STOP THE CAR
QUIT - TO QUIT OR EXIT FROM THE CAR
          """)
      elif command == "quit" or command == "QUIT":
          break
      else:
           print("Sorry i don't understand")