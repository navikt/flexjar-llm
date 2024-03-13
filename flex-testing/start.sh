docker run --cpus="7" -v $(pwd)/models:/models -p 8007:8000 ghcr.io/ggerganov/llama.cpp:server -m /models/Llama-2-13b-chat-norwegian.gguf --port 8000 --host 0.0.0.0 -n 256 -ngl 50
