# Synced

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: rsync, protocols, recon, anon/guest access

#### Description
  > 

#### Notes
  > #### **Introduction**
  > FTP slow, these days the kids use RSYNC to transfer changes from few files rather than whole files everytime. Changes are transferred are called <code>deltas</code>. Stages of rsync are: establish connection, sender and receiver processes compare what files have changed, changes get updated on remote host. Misconfigs can permit unauthorized users to sign in. 

  > #### **Enumeration**
  > Use nmap to search for open ports on the target machine. This time we use --min-rate for a more efficient search among all the ports. 

  > #### **Rsync**
  > RSYNC comes pre-installed on almost all Linux distros. The generic syntax for it is <code>rsync [option] ... [user@host] [dest]</code>. The command --list-only allows us to do a little peaksies on the files that target machine holds. Using the format above you can get the flag from the remote machine. 