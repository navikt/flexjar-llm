# flexjar-llm

## Kom igang med flexjar-llm
- Bruker Llama.cpp (repo: https://github.com/ggerganov/llama.cpp?tab=readme-ov-file)
- Last ned modell fra huggingface.com
    - Vi har bruke RuterGPT (https://huggingface.co/RuterNorway/Llama-2-13b-chat-norwegian/tree/main)
- Kjør `python3 convert.py ../models/Llama-2-13b-chat-norwegian/ --outfile ../models/Llama-2-13b-chat-norwegian.gguf --outtype q8_0` for å konvertere modell til .gguf
- Kjør `./start.sh` for å kjøre modellen uten lora (krever at du har en modell i `../models/`)

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

