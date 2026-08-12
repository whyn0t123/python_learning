guests=['x','y','z']
message=f"Would you like to have a dinner with me? {guests[0]}?"
message+=f"\nWould you like to have a dinner with me? {guests[1]}?"
message+=f"\nWould you like to have a dinner with me? {guests[2]}?"
print(message)

print("x isn't free.")
guests[0]="s"
message=f"Would you like to have a dinner with me? {guests[0]}?"
message+=f"\nWould you like to have a dinner with me? {guests[1]}?"
message+=f"\nWould you like to have a dinner with me? {guests[2]}?"
print(message)

print("I find a bigger table.")
guests.insert(0,"a")
guests.insert(1,"b")
guests.append("c")
message=f"Would you like to have a dinner with me? {guests[0]}?"
message+=f"\nWould you like to have a dinner with me? {guests[1]}?"
message+=f"\nWould you like to have a dinner with me? {guests[2]}?"
message+=f"\nWould you like to have a dinner with me? {guests[3]}?"
message+=f"\nWould you like to have a dinner with me? {guests[4]}?"
message+=f"\nWould you like to have a dinner with me? {guests[5]}?"
print(message)

print("I can only ;invite 2 guests.")
guest=guests.pop()
print(f"Sorry {guest}, I can't invite you to my dinner.")
guest=guests.pop()
print(f"Sorry {guest}, I can't invite you to my dinner.")
guest=guests.pop()
print(f"Sorry {guest}, I can't invite you to my dinner.")
guest=guests.pop()
print(f"Sorry {guest}, I can't invite you to my dinner.")
print(f"{guests[0]},you are still on the list.")
print(f"{guests[1]},you are still on the list.")
print(len(guests))

del guests[1]
del guests[0]
print(guests) 