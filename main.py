name=input("Enter your name")
gadget=input("Enter your favourite gadget")
agent=7
speed=9.5
is_active=True
print("name:",name,type(name))
print("speed:",speed,type(speed))
print("is_active:",is_active,type(is_active))

agent_text=str(agent)
speed_text=int(speed)
print(type(agent_text))
print(type(speed_text))

first_three= name[0:3]
print("first three leters of name",first_three)
reverse_gadget=gadget[::-1]
badge_line1=agent
badge_line2=first_three
badge_3="secret gadget code"+reverse_gadget
print("")
print("secret agent badge")
print(badge_line1)
print(badge_line2)
print(badge_3)