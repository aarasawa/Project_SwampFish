# Redeemer

#### Difficulty: <code>Very Easy</code>

#### Machine Tags: redis, vulnerability assessment, databases, recon, anonymous/guest access

#### Description
  > 

#### Notes
  > #### **Enumeration**
  > To start we ping the IP we are looking to target, I am not sure whether this is better than just going into the NMAP, it may help to verify that the NMAP does not take forever if the port is not a commonly used one. 

  > #### **What is Redis?**
  > Redis (REmote DIctionary Server) is a NoSQL key-value datastore used as a database, cache, or message broker. Server-side so it listens for connections. Thus we can use a tool like <code>redis-tools</code> to access its CLI. 

  > #### **Enumerating Redis Server**
  > Connecting with an IP would look like <code>redis-cli -h {IP}</code>. Using the keyword <code>info</code> shows information about the Redis server such as version and keyspace information. **Keyspace** info lets us know stats about the main dictionary of each database like number of keys and number of keys that expire. Running <code>keys *</code> allows us to view values stored. 