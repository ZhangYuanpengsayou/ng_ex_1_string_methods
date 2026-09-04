booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

booking = booking.strip()
parts = booking.split("|")

event_code = parts[0].strip()
name = parts[1].strip().title()
room = parts[2].strip().upper()
time = parts[3].strip()
email = parts[4].strip().lower()
vip_tag = parts[5].strip().upper()

at_position = email.find("@")
email_domain = email[at_position + 1:]
username = email[:at_position]

vip_tag_count = vip_tag.count("VIP")
valid_event_code = event_code.startswith("EVT-") and event_code[4:].isdigit()
valid_username = username == name.lower().replace("_", ".")
valid_room = room.startswith("ROOM-") and room[5:].isdigit()
valid_time = len(time) == 5 and time[2] == ":" and time[:2].isdigit() and time[3:].isdigit() and int(time[:2]) < 24 and int(time[3:]) < 60
valid_email = at_position != -1 and username != "" and email_domain.endswith(".edu")

output = f"""Event code: {event_code}
Name: {name}
Room: {room}
Time: {time}
Email domain: {email_domain}
VIP tag count: {vip_tag_count}
Valid event code: {valid_event_code}
Valid username: {valid_username}
Valid room: {valid_room}
Valid time: {valid_time}
Valid email: {valid_email}"""

print(output)
######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """

