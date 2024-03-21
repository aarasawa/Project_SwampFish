# Iced Tea

#### Difficulty: <code>Easy</code>

#### Description
> Locked within a cabin crafted entirely from ice, you're enveloped in a chilling silence. Your eyes land upon an old notebook, its pages adorned with thousands of cryptic mathematical symbols. Tasked with deciphering these enigmatic glyphs to secure your escape, you set to work, your fingers tracing each intricate curve and line with determination. As you delve deeper into the mysterious symbols, you notice that patterns appear in several pages and a glimmer of hope begins to emerge. Time is flying and the temperature is dropping, will you make it before you become one with the cabin?

#### 1. 
> I did some initial research into this problem when the event was live. However, got busy and could not commit to solving for the flag. I learned about Electronic Codebook (ECB) and Cipher Block Chaining (CBC) as they were the initial enumerated methods for the Iced Tea program. In the program, the initailization vector was set to None so the method of encryption was ECB. This means that the encryption would be block by block and would not rely on the chaining effect. 