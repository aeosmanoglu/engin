# import torch
# import transformers
import time

from django.shortcuts import render, redirect

from .forms import InputForm


# from transformers import LlamaForCausalLM, LlamaTokenizer


def chat_view(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    form = InputForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        input_text = form.cleaned_data['input_text']

        if input_text.strip():
            start_time = time.time()

            # Model yükleme
            # model_dir = "./llama-2-7b-chat-hf"
            # model = LlamaForCausalLM.from_pretrained(model_dir)
            # tokenizer = LlamaTokenizer.from_pretrained(model_dir)
            # pipeline = transformers.pipeline(
            #     "text-generation",
            #     model=model,
            #     tokenizer=tokenizer,
            #     torch_dtype=torch.float16,
            #     device_map="auto",
            # )

            # sequences = pipeline(
            #     input_text,
            #     do_sample=True,
            #     top_k=10,
            #     num_return_sequences=1,
            #     eos_token_id=tokenizer.eos_token_id,
            #     max_length=400,
            # )
            # response_text = sequences[0]['generated_text']

            # ===============================
            # Simulate a response. Remove this line when using the model.
            time.sleep(3)  # Simulate a long response time. Remove this line when using the model.
            response_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie erat a "
                             "rhoncus aliquam. Duis sed maximus lorem. Ut malesuada pretium nisi nec iaculis. Sed "
                             "vitae ipsum nec odio gravida posuere. Donec rutrum nisl id orci pharetra eleifend. "
                             "Etiam a sem et libero congue mattis. Suspendisse id eros pellentesque purus "
                             "vulputate rutrum sit amet congue quam. Nunc lobortis sapien ut lectus tristique "
                             "fermentum. Etiam velit felis, venenatis commodo nunc et, semper posuere orci.")
            # ===============================

            response_time = time.time() - start_time

            # Save chat history
            request.session['chat_history'] += [("User", input_text, ""),
                                                ("Engin", response_text, f"{response_time:.2f} secs")]
            request.session.modified = True

            return render(request, 'chat.html', {'form': form, 'chat_history': request.session['chat_history']})

    return render(request, 'chat.html', {'form': form, 'chat_history': request.session.get('chat_history', [])})


def new_chat(request):
    if 'chat_history' in request.session:
        del request.session['chat_history']
    return redirect('/')
