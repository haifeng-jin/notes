# Switch

Switch is in the datalink layer of the [OSI model](osi.md).
It uses the MAC address of the frame to decide where to send the frame.
It keeps a table of MAC addresses and where to send to them.
If the frame is sending to a MAC address not in the table,
it would first do a flood (asking all its neighbours to find that MAC address in their neighbours recursively) to find the MAC address and record it in the table.
Therefore, next time, it knows where to send it for the next hop when it see this MAC address.
