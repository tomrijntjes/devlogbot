# Devlogbot

I've been keeping a daily developer logbook for years. Devlogbot makes it queryable with Lmstudio and ChromaDB for RAG. 

Want to start keeping your own dev logbook? Run the following at the start of your day:

`cd ~/Documents && code . && touch log/$(date +%m%d).txt && code log/$(date +%m%d).txt`

None of this is created with portability in mind, this is just for me and my macbook.

## Installation

Bootstrap lms:

```
~/.lmstudio/bin/lms bootstrap
lms load --context-length 12000 lmstudio-community/Qwen2.5-7B-Instruct-1M-GGUF/Qwen2.5-7B-Instruct-1M-Q4_K_M.gguf
lms server start
```

Install package globally:

`pipx install devlogbot`

## Running

`devlogbot what is our client credential rotation schedule`
