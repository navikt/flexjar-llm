from huggingface_hub import snapshot_download
model_id="RuterNorway/Llama-2-13b-chat-norwegian"
snapshot_download(repo_id=model_id, local_dir="models/Llama-2-13b-chat-norwegian",
                  local_dir_use_symlinks=False, revision="main")