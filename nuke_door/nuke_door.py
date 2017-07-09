"""
Review the following (fictional!) code for a nuclear vault door. 

Identify potential safety or correctness issues.
(the record is 5)

The control mechanism of the lock of a vault for nuclear waste
has been designed for safe operation. It makes sure that it is
only possible to access the vault, if the radiation shields
are in place or the radiation level in the vault is below a 
threshold (DANGER_LEVEL). That means:

* If the remote-controlled radiation shields are in place, the door may be opened by an authorized operator.
* If the radiation level in the room is below the threshold, the door may be opened by an authorized operator.
* An authorized operator may open the door by entering a code.

The code below controls the door lock. Note that the safe state
is that no entry is possible. Develop an argument for safety
that shows that the code is potentially unsafe. 

(adopted from I.Sommerville, Software Engineering, 9th edition)
"""

entry_code = lock.get_entry_code()
if entry_code == lock.authorised_code:
    shield_status = shield.get_status()
    radiation_level = rad_sensor.get()
    if radiation_level < DANGER_LEVEL:
        state = SAFE
    else:
        state = UNSAFE
    if shield_status == shield.in_place():
        state = SAFE
    if state == SAFE:
        door.locked = False
        door.unlock()
    else:
        door.lock()
        door.locked = True
