from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
import torch

T5_PATH = 't5-base'

t5_model = T5ForConditionalGeneration.from_pretrained(T5_PATH)
t5_tokenizer = T5Tokenizer.from_pretrained(T5_PATH)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def T5_summarization(input_text , num_beams, sum_len):
    input_text = str(input_text).replace('\n', '')
    input_text = ' '.join(input_text.split())
    input_tokenized = t5_tokenizer.encode(input_text, return_tensors="pt").to(device)
    summary_ids = t5_model.generate(input_tokenized,
                                    num_beams=int(num_beams),
                                    no_repeat_ngram_size=2,
                                    min_length=int(sum_len),
                                    max_length=int(sum_len) + 20,
                                    early_stopping=True)
    output = [t5_tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
    # print("The summarized text is as follows:")
    return (output[0])

# T5_summarization()