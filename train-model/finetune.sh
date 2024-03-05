#!/bin/bash -

../bin/finetune \
--model-base ../models/Llama-2-13b-chat-norwegian.gguf \
--checkpoint-in lora-checkpoint-flex2-LATEST.gguf \
--checkpoint-out lora-checkpoint-flex2-ITERATION.gguf \
--lora-out lora-flex2-ITERATION.gguf \
--train-data "instructed-trainingdata-flex2.jsonl" \
--save-every 20 \
--rope-freq-base 10000 \
--rope-freq-scale 1.0 \
--threads 8 --adam-iter 256 --batch 1 --ctx 512 --lora-r 8 --lora-alpha 8 \
--use-checkpointing \
--use-flash \
--seed 1 \
--sample-start "\n" \
--escape \
-ngl 50 \
--include-sample-start
