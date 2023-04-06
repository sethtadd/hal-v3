import json
import os
import shutil

import openai


def copy_file(file_name, destination_file_name):
    try:
        shutil.copy(file_name, destination_file_name)
        print(f"'{file_name}' was copied to '{destination_file_name}'.")
    except Exception as e:
        print(f"An error occurred while copying the file: {e}")


def llm_digest(filename):
    print("llm_digest processing...")
    with open(filename, "r") as f:
        message_log = json.load(f)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
    )
    content = response["choices"][0]["message"]["content"]

    with open(filename, "w") as f:
        f.write(content)


if __name__ == "__main__":
    shard_filename = "copy.shard.json"
    copy_file("input.shard.json", shard_filename)
    llm_digest(shard_filename)
    print("done.")
