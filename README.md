# b618reboot

Please note this script was written for  __Python 3 and higher.__

#### About
Simple Python script for rebooting Huawei B618 and B715 LTE router via web interface.

My router occasionally drops the LTE connection (whilst still responding on the LAN interface) and the quick fix is to reboot the device using its web interface. Which was ok for a while, but as I was going on holiday and wanted to keep the LTE connection running to have access to the security camera, I decided to quickly write a script which I could run from cron on my home Linux server to trigger the reboot when the connection goes down. 

It is not pretty (sorry!) but it does the job for me. It might work with other Huawei router using SCRAM authentication but do not have any around, so cannot test. Feel free to let me know if it does.
Happy to accept improvements via pull requests!

#### Usage
Update settings in the `config.py` file and run the `reboot_router.py` script for the immediate reboot. Please note some routers (B618s, B818-623) do not support passwords longer than 32 characters. 

Thanks to [@gsdefender](https://github.com/gsdefender) there is also a script to reboot the router only if there is no connectivity (tested by an attempt to open TCP connection to the host and port of your choice - by default: 8.8.8.8:53): run `reboot_router_if_no_connection_background.sh` (or `reboot_router_if_no_connection.py`).

#### Model and firmware info

|                   | B618             | B715             |B525             |B525               |
| :---              | :---:            | :---:            |:----:           |:----:             |
| Device name:      | B618s-22d        | B715s-23c        |B525s-65a        |B525s-23a          |
| Hardware version: | WL1B610FM        | WL1B610FM05      |WL2B520M         |WL1B520FM          |
| Software version: | 11.185.01.01.104 | 11.195.03.01.965 |11.189.63.00.74  |11.189.61.00.1217  |
| Web UI version:   | 21.100.26.00.0   | 21.100.39.00.03  |21.100.44.00.03  |21.100.44.00.03    |

#### Alternative version
There is also a Go version at [b618reboot-go](https://github.com/mkorz/b618reboot-go) which additionally can pull signal stats and is available as ready to run Docker container.
