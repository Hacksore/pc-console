# steam-pc
Make a steam powered computer that feels like a console, it runs Windows for max compatibility.

Idea is to allow for a bluetooth xbox controller to be able to power on the computer when it's asleep with some hacky magic!

## Hardware
- Raspbery Pi
- Ubertooth One SDR
- Windows PC that supports WOL
- Xbox One Wireless Controller


### Objectives
- [x] Shell is replaced with Steam
- [x] No Windows password/logon screen
- [x] Can wake up on controller power 
- [ ] System can go to sleep (Steam seems to be holding windwos hostage 😡)


### Getting LAP address
 - Run `ubertooth-rx` and power on your controller you should see some traffic from your controller
 - You should see lines like `systime=1602379978 ch=68 LAP=<devicLAP> err=1 clkn=92641 clk_offset=5248 s=-63 n=-55 snr=-8`
 - Use the `LAP` value to target your contorller