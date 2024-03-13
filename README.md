# Flexjar-llm

## Kom igang med flexjar-llm
- Bruker Llama.cpp (repo: https://github.com/ggerganov/llama.cpp?tab=readme-ov-file)
- Last ned modell fra huggingface.com
    - Vi har bruke RuterGPT (https://huggingface.co/RuterNorway/Llama-2-13b-chat-norwegian/tree/main)
    - Kjør `python3 download-hf.py` for å laste ned modell
- Kjør `python3 convert.py models/Llama-2-13b-chat-norwegian/ --outfile models/Llama-2-13b-chat-norwegian.gguf --outtype q8_0` for å konvertere modell til .gguf
- Kjør `./start.sh` for å kjøre modellen uten lora (krever at du har en .gguf modell i `models/`)

## Kjøre modell uten docker (raskere på mac med M-chip)
- Klon repoet llama.cpp (https://github.com/ggerganov/llama.cpp)
- Kjør `make` for å bygge
- Kjør `./server -v -c 4096 -ngl 50 -n 256 -m models/Llama-2-13b-chat-norwegian.gguf --host 0.0.0.0 --port 8007` for å kjøre modellen

## Fine-tuning med lora
- Generer treningsdata med eksempler på oppgaver og respons. Se eksempler i `finetune-modell/raw-text.sjon`
- Konverter treningsdata til .jsonl-fil med `tekstformaterer.py`
- Kjør `./finetune.sh` for å trene modellen 
    - Husk å endre 
    `--model-base`, 
    `--checkpoint-in`,
    `--checkpoint-out`,
    `--lora-out` og 
    `--train-data` til riktig modell og in/output-fil

## Kjøre modellen med lora
- Legg til `--lora path-to-lora/lora-fil.gguf` etter modellnavn i enten `start.sh` eller i `./server`-komandoen for å kjøre modellen med lora

