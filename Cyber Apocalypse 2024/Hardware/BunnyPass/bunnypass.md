# BunnyPass

#### Difficulty: <code>Very Easy</code>

#### Description
> As you discovered in the PDF, the production factory of the game is revealed. This factory manufactures all the hardware devices and custom silicon chips (of common components) that The Fray uses to create sensors, drones, and various other items for the games. Upon arriving at the factory, you scan the networks and come across a RabbitMQ instance. It appears that default credentials will work.

#### 1.
> I do not know anything about hardware exploitation. Reading the description, we run the docker instance and come upon a terminal. I tried admin and password, which did not work, then admin and admin. I was able to login. This was easier than I thought, some digging around was able to obtain the flag. Felt more like simple web exploit than hardware. 