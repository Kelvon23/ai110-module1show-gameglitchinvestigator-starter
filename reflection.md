# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The first bug I notice was when I get to the end of the game wether that be through typing the correct guess right away or playing the game till it ends. Whenever I try to start a new game the game fails to allow me to play the game again. The next error I ran in to was the hints were backwards. For example if the secret number was 25 and i type 29 the game hint would tell me to guess higher. I expected it tell me to guess lower as the secret number is less than 29 and so on. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I use claude to help for this project. I used ai to help me figure out why the message for the hint were incorrect. It was not a logic error but just us wording it wrong so ai fixed that immediately. One example where ai suggested something misleading was making changes in the wrong file. I accidently provide the wrong context and make it override the previous file so i had to add it to undo those changes. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I checked whether was a bug was fixed by asking it to make pytest for the bugs I found out. And it managed to pass all the tests. I asked to ensure the hint says go lower when the guess is too high. I also verified by playing the game again after commiting the changes with the ai agent. While playing it the hint was correct this time around. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would describe as closing an app and refreshing it as streamlist reruns the entire python script from top to bottom. The session state is streamlit way of remembering things across.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I would have the ai always talk to me through their way of thinking before they make the changes to the code. One thing I would do differently is to provide as much context to the ai agent as possible as there was a case the ai rewrote the code from a file completely and lost the previous code so I need to tell the ai next time what i want it to do exactly. It help me know ai is there to help as long as i provide it with enough context 

