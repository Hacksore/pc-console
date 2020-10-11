# steam-pc
Make a steam powered computer that feels like a console, it runs Windows for max compatibility.

Idea is to allow for a bluetooth xbox controller to be able to power on the computer when it's asleep with some hacky magic!

## Hardware
- Raspbery Pi
- Ubertooth One SDR
- USB Bluetooth Dongle (not needed?)
- Windows PC that supports WOL
- Xbox One Wireless Controller


### Objectives
- Shell is replaced with Steam
- No Windows password/logon screen
- System can go to sleep
- Can wake up on controller power on


# Notes
Was able to use `ubertooth-rx` to see a query
`systime=1602379978 ch=68 LAP=<devicLAP> err=1 clkn=92641 clk_offset=5248 s=-63 n=-55 snr=-8`
