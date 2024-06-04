guests = ["Hunter", "Alyssa", "Keily", "Tucker", "Maddox", "Isaiah", "Kaylee"]

def remove_guest(guest_name, response):
  """
  Removes a guest from the list if their RSVP is "No".

  Args:
      guest_name: The name of the guest to remove.
      response: The guest's RSVP ("Yes" or "No").
  """
  try:
    guest_index = guests.index(guest_name)
    if response == "No" or response == 'no' or response == 'n':
      guests.pop(guest_index)
      print(f"{guest_name} has RSVPed 'No' and has been removed from the list.")
  except ValueError:
    print(f"{guest_name} was not found in the guest list.")

# Simulate guest RSVPs
remove_guest("Alyssa", "No")
remove_guest("Isaiah", "Yes")
remove_guest("Emily", "Yes")  # Guest not found

print("\nUpdated guest list:", guests)
