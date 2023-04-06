import json
import os
import signal
import sys
import traceback
from datetime import datetime

import openai


def save_conversation_log(log):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"conversation_history/conversation_log_{timestamp}.txt"

    with open(file_name, "w") as f:
        f.write(json.dumps(log, indent=2))


def list_conversation_logs():
    directory = "conversations"
    conversation_files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.startswith("conversation_log_")
    ]
    conversation_files.sort(key=os.path.getctime, reverse=True)
    return conversation_files


def load_conversation_log(file_name):
    with open(file_name, "r") as f:
        return json.loads(f.read())


def select_model():
    print("Select a model to continue:")
    models = ["gpt-3.5-turbo", "gpt-4"]
    for idx, model in enumerate(models):
        print(f"{idx}: {model}")

    try:
        selected_idx = int(
            input("Enter the index of the conversation log (0, 1, 2, etc.): ")
        )
        return models[selected_idx]
    except (IndexError):
        print(f"Invalid index. Selecting default model: {models[0]}")
        return models[0]


def select_conversation_log():
    print("Select a conversation log to continue:")
    logs = list_conversation_logs()
    for index, log in enumerate(logs):
        print(f"{index}: {log}")

    try:
        selected_index = int(
            input("Enter the index of the conversation log (0, 1, 2, etc.): ")
        )
        return load_conversation_log(logs[selected_index])
    except (IndexError, ValueError):
        # stack trace
        traceback.print_exc()
        print("Invalid index. Starting a new conversation.")
        return [
            {
                "role": "system",
                "content": "You are an instruction-following LLM. You take json objects as input and output json objects.",
            }
        ]
        # return [{"role": "system", "content": "You are a helpful assistant."}]


def signal_handler(sig, frame):
    print("\nCtrl-C detected. Saving conversation log and exiting.")
    save_conversation_log(message_log)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

model = select_model()
message_log = select_conversation_log()
message_log.append({"role": "system", "content": "The system has been rebooted."})

while True:
    try:
        message_log.append({"role": "user", "content": input("user:\n")})
        response = openai.ChatCompletion.create(
            model=model, messages=message_log, temperature=1, top_p=1
        )

        content = response.choices[0].message["content"]
        message_log.append({"role": "assistant", "content": content})
        print(f"assistant:\n{content}")
    except EOFError:
        print("\nDetected EOF. Saving conversation log and exiting.")
        save_conversation_log(message_log)
        break
