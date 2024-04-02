# Snort Basics

## Resources
For identifying file signatures in packets: 
https://en.wikipedia.org/wiki/List_of_file_signatures

## Snort Help
Packet statstics for pcap composition, totals, etc. with minimal verbosity
```
  snort -c {rules} -r {pcap} -A console
```

Generate snort.log file for a pcap file based on a ruleset
```
  snort -A full -r {pcap} -c {rules} -l .
```

Using the **strings** command on a pcap or snort.log file can help sometimes for identifying a service or software name

Template rule for detecting a protocol or service on a port
```
  alert {protocol} any {port} <> any any (msg:"..."; sid:1; rev:1;)
  alert {protocol} any any <> any {port} (msg:"..."; sid:2; rev:1;)
```

Template rule for detecting a packet with a signature attached
```
  alert {protocol} any any <> any any (msg:"..."; sid:1; rev:1; content:"hex file signature")
```