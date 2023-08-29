## Llamka: chat interface for Llama-2.cpp 


#### Additional Repositories and HuggingFace models

```bash
$ mkdir llm-chat-local && cd llm-chat-local
$ git lfs install 
$ git clone git clone https://huggingface.co/codellama/CodeLlama-13b-hf
$ git clone https://github.com/facebookresearch/llama
$ git clone: https://github.com/ggerganov/llama.cpp
```


#### This repository

```bash
$ git clone https://github.com/Vladimirchizh/lamka.git
```

#### Building and quantizing cpp models from tensorflow/pytorch models

```bash
$ cd llama.cpp
$ python3 -m pip install -r requirements.txt
$ python3 convert.py --outfile models/7B/ggml-model-f16.bin --outtype f16 ../CodeLlama-13b-hf
$ make
$ ./quantize  ./models/7B/ggml-model-f16.bin ./models/7B/ggml-model-q4_0.bin q4_0
$ ./main -m ./models/7B/ggml-model-q4_0.bin -n 1024 --repeat_penalty 1.0 --color -i -r "User:" -f ./prompts/chat-with-bob.txt
```

For more options of building binaries with Llama.cpp - visit [their repository](https://github.com/ggerganov/llama.cpp).

After models are built add their Credentials to the `conf/Paths.yaml` and start Django web application.


![Lamka interface](pics%2Fphoto_2023-08-29%2015.03.43.jpeg)