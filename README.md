# CYAFE

![Hello there](photo.png)

The digital landscape presents both opportunities and challenges. While technology empowers individuals and organizations, it also creates avenues for cyber threats and exploitation. Kenya, like many countries, faces a rising tide of cybercrime, including social engineering tactics used to facilitate gender-based violence (GBV). Traditional cybersecurity awareness methods often fail to reach the most vulnerable populations, particularly those in rural areas with limited internet access.

Cyafe is an innovative project designed to address this critical gap. We propose the development of an offline-first SMS chatbot, a readily accessible and culturally sensitive solution. This chatbot will deliver essential cybersecurity knowledge directly to individuals in their preferred language, leveraging the ubiquitous reach of SMS messaging while also available to online users.

Cyafe operates via both SMS interactions and an online web app. Users can initiate a conversation, ask questions, and receive information on various cybersecurity topics. The chatbot utilizes pre-programmed responses and branching dialogues to cater to diverse user needs. By providing accessible and localized information, Cyafe empowers individuals to protect themselves online, identify social engineering tactics, and will also evolve to provide a platform to report suspicious activity.

This project aims to create a safer digital environment for all Kenyans. Cyafe not only equips individuals with essential knowledge but also serves as a convenient training tool for organizations, fostering a more secure workplace culture. By bridging the cybersecurity awareness gap, Cyafe empowers communities, safeguards vulnerable populations, and contributes to the fight against online abuse.

## Features:

The chatbot processes user input and attempts to find the most appropriate response.
Responses are provided by the OPENAI API specifically gpt-3.5 turbo.

## Usage:

The bot is deployed on [this](https://chatbot-sz7q.onrender.com/) URL.

## Customization:

To customize the chatbot's behavior, you can modify this section in the app.py  
`def get_completion(prompt, model="gpt-3.5-turbo"):`  
`    initial_message = "Program the bot here"`  
`    messages = [{"role": "system", "content": initial_message}, {"role":` `"user", "content": prompt}]`

## Authors

injili  
mwanyumba7  
Carlalagat  
Lenndadeborah
