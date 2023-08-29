from django.shortcuts import render, redirect
import subprocess
import yaml

with open("conf/Paths.yaml") as file:
    config = yaml.full_load(file)


def home(request):
    try:
        if 'messages' not in request.session:
            request.session['messages'] = [
                {
                    "role": "system",
                    "content": (
                        "You are now chatting with a user, provide them with "
                        "comprehensive, short and concise answers."
                    )
                },
            ]
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            temperature = float(request.POST.get('temperature', 0.8))
            # append the prompt to the messages list
            request.session['messages'].append({"role": "user", "content": prompt})
            # set the session as modified
            request.session.modified = True
            prompt = request.session['messages'][-1]["content"]
            response = subprocess.run(
                [f"{config['bin']}/main",
                 "-m", f"{config['bin']}/models/{config['parameters']}/{config['model']}",
                 "--repeat_penalty", "1.0",
                 "--temp", f"{temperature}",
                 "-i", "--prompt", prompt,
                 "-n", "-2"],
                capture_output=True, text=True,
            )
            # append the response to the messages list
            request.session['messages'].append({"role": "assistant", "content": response.stdout})
            print(request.session['messages'])
            request.session.modified = True
            # redirect to the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': temperature,
            }
            return render(request, 'home.html', context)
        else:
            # if the request is not a POST request, render the home page
            context = {
                'messages': request.session['messages'],
                'prompt': '',
                'temperature': 0.8,
            }
            return render(request, 'home.html', context)
    except Exception as e:
        print(e)
        # if there is an error, redirect to the error handler
        return redirect('error_handler')


def new_chat(request):
    # clear the messages list
    request.session.pop('messages', None)
    return redirect('home')


# handling errors
def error_handler(request):
    return render(request, '404.html')
