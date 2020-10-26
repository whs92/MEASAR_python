# MEASAR_python
Test of serial interface to MEASAR Solo device

A reset command is intially sent, followed by a request to the user for a command. For example "RD" Will read the dead time variable.

If you issue a write commnad you will then be asked for a value to write in hex.

To call the script use:

  sudo python3 serTestInteractive.py


