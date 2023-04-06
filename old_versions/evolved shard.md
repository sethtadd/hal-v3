```json
{
    "context_shards": [
        {
            "shard_id": "SRD-000000",
            "shard_type": "introductory",
            "content": "Welcome to the shard network. You are an LLM instance tasked with navigating the network to find information and perform reasoning to solve problems. The network is composed of shards that contain information, reasoning steps, and instructions. You can query shards by requesting them using their unique IDs. The caller has provided a query attached as 'input_query'. Traverse the shard network to answer the query and generate a response shard containing the results, path taken, and a final report. If the reasoning steps are already partially filled out, then you are already on your way to solving the problem using the shard network, great work! Remember, ALL of your responses MUST be contained within this json object which will be passed back and forth between you and the system."
        },
        {
            "shard_id": "SRD-000001",
            "shard_type": "Process",
            "topic": "Internal Knowledge Decision",
            "metadata": {
                "created_at": "2027-06-15T09:00:00Z",
                "version": 1
            },
            "instructions": [
                {
                    "title": "Evaluate Internal Knowledge",
                    "description": "Assess your internal knowledge base to determine if you can answer the input_query without accessing the shard network."
                },
                {
                    "title": "Respond with Confidence",
                    "description": "If you can answer the input_query using your internal knowledge, respond with confidence and provide the answer."
                },
                {
                    "title": "Initiate Shard Network Traversal",
                    "description": "If you cannot answer the input_query using your internal knowledge, initiate the shard network traversal/query process to find the necessary information."
                },
                {
                    "title": "Update Reasoning Steps",
                    "description": "Document your decision and reasoning in the 'reasoning_steps' field of the JSON object, indicating whether you used internal knowledge or initiated shard network traversal."
                },
                {
                    "title": "Complete the Task",
                    "description": "If you used internal knowledge, set 'terminate_network_traversal' to 'true' and 'output_result' to the result of the input_query. If you initiated shard network traversal, continue the process until the input_query is answered or the maximum reasoning steps are reached."
                }
            ]
        },
        {
            "shard_id": "SRD-000002",
            "shard_type": "Process",
            "topic": "Shard Network Query",
            "metadata": {
                "created_at": "2027-06-15T09:00:00Z",
                "version": 1
            },
            "instructions": [
                {
                    "title": "Compose Shard Query",
                    "description": "A single traversal step. When you need to query a shard, compose a message that includes the shard_id you wish to access. The message should be in the format: '{\"shard_id\": \"SRD-XXXXXX\"}' where 'SRD-XXXXXX' is the unique ID of the shard you want to query."
                },
                {
                    "title": "Send Shard Query",
                    "description": "Add the composed shard query message to the 'reasoning_steps' field of the JSON object with your role set as 'assistant'. The system will process your query and return the requested shard information."
                },
                {
                    "title": "Process Shard Response",
                    "description": "Upon receiving the shard response from the system, process the information and use it to continue reasoning or answer the input_query. Be sure to update the 'reasoning_steps' field of the JSON object with any new findings or conclusions."
                },
                {
                    "title": "Continue Traversal",
                    "description": "If necessary, continue traversing the shard network by sending additional shard queries following the same process. Be mindful of the 'maximum_reasoning_steps' limit to avoid exceeding the allowed number of steps."
                }
            ]
        },
        {
            "shard_id": "SRD-000003",
            "shard_type": "Process",
            "topic": "Condensing Reasoning Steps",
            "metadata": {
                "created_at": "2027-06-15T09:00:00Z",
                "version": 1
            },
            "instructions": [
                {
                    "title": "Assess Shard Object Size",
                    "description": "Evaluate the current size of the shard object, including the 'reasoning_steps' field."
                },
                {
                    "title": "Determine Necessity of Condensing",
                    "description": "If the shard object size is approaching a limit or if it is deemed necessary for any reason, prepare to condense the shard object."
                },
                {
                    "title": "Trim Reasoning Steps",
                    "description": "Carefully remove unnecessary reasoning steps, while preserving the key steps and conclusions that are essential for understanding the solution."
                },
                {
                    "title": "Condense Other Fields",
                    "description": "Consider condensing other fields within the shard object if needed, ensuring that important information is not lost."
                },
                {
                    "title": "Update Shard Object",
                    "description": "Apply the changes to the shard object, ensuring that the condensed version still contains all the essential information for solving the problem and understanding the solution."
                }
            ]
        }
    ],
    "input_query": "3*3",
    "maximum_reasoning_steps": 10,
    "reasoning_steps": [
        {
            "role": "system",
            "content": "Initiate reasoning steps, and when finished, please set terminate_network_traversal to true and output_result to the result of the input_query and return this entire json object as your response: output_result. Note: place your first response/query/etc. in the <FILL THIS IN> field below. You will refer to yourself as this assistant in this reasoning_steps field."
        },
        {
            "role": "assistant",
            "content": "<FILL THIS IN>"
        }
    ],
    "terminate_network_traversal": "false",
    "output_result": "null"
}
```

More evolved shard?:

```json
{
  "context_shards": [
    {
      "shard_id": "SRD-000000",
      "content": "Welcome. As an LLM, navigate the shard network, answer the input_query, and generate a response shard. If reasoning steps are partially filled, continue solving the problem. All responses must be within this json object. Good luck!",
      "content_example": {
        "context_shards": [],
        "input_query": "3*3",
        "maximum_reasoning_steps": 10,
        "reasoning_steps": [
          {
            "role": "system",
            "content": "Initiate reasoning steps. Set terminate_network_traversal to true, output_result to input_query result, and return the json object as output_result."
          },
          {
            "role": "assistant",
            "content": "Evaluating 3*3 with internal knowledge."
          },
          {
            "role": "assistant",
            "content": "Answer: 9. Setting terminate_network_traversal to true and output_result to 9."
          }
        ],
        "terminate_network_traversal": "true",
        "output_result": "9"
      }
    },
    {
      "shard_id": "SRD-000001",
      "instructions": [
        {
          "title": "Evaluate Internal Knowledge",
          "description": "Assess internal knowledge to answer input_query."
        },
        {
          "title": "Respond with Confidence",
          "description": "If possible, answer input_query confidently."
        },
        {
          "title": "Initiate Shard Network Traversal",
          "description": "If not, start shard network traversal."
        },
        {
          "title": "Update Reasoning Steps",
          "description": "Document decision and reasoning in 'reasoning_steps'."
        },
        {
          "title": "Complete the Task",
          "description": "Finish task, update 'terminate_network_traversal' and 'output_result'."
        }
      ]
    },
    {
      "shard_id": "SRD-000002",
      "instructions": [
        {
          "title": "Compose Shard Query",
          "description": "Create a message with shard_id to access."
        },
        {
          "title": "Send Shard Query",
          "description": "Add query message to 'reasoning_steps'."
        },
        {
          "title": "Process Shard Response",
          "description": "Process response and update reasoning."
        },
        {
          "title": "Continue Traversal",
          "description": "If needed, continue traversal, considering 'maximum_reasoning_steps'."
        }
      ],
      "example_shard_query": {
        "role": "assistant",
        "content": "{\"shard_id\": \"SRD-XXXXXX\"}"
      },
      "example_query_response": {
        "role": "system",
        "content": {
          "shard_id": "SRD-XXXXXX",
          "shard_type": "Information",
          "topic": "Sample Topic",
          "metadata": {
            "created_at": "2023-04-03T09:00:00Z",
            "version": 1
          },
          "content": "This is an example of the information contained within the shard."
        }
      }
    },
    {
      "shard_id": "SRD-000003",
      "instructions": [
        {
          "title": "Assess Shard Object Size",
          "description": "Evaluate the shard object size."
        },
        {
          "title": "Determine Necessity of Condensing",
          "description": "If needed, prepare to condense shard object."
        },
        {
          "title": "Trim Reasoning Steps",
          "description": "Remove unnecessary steps, preserving key ones."
        },
        {
          "title": "Condense Other Fields",
          "description": "Condense other fields if needed, keeping important information."
        },
        {
          "title": "Update Shard Object",
          "description": "Apply changes, ensuring essential information is retained."
        }
      ]
    }
  ],
  "input_query": "Test query: What is the square of 4?",
  "maximum_reasoning_steps": 10,
  "reasoning_steps": [
    {
      "role": "system",
      "content": "Initiate reasoning steps, and when finished, please set terminate_network_traversal to true and output_result to the result of the input_query and return this entire json object as your response: output_result. Note: place your first response/query/etc. in the <FILL THIS IN> field below. You will refer to yourself as this assistant in this reasoning_steps field."
    },
    {
      "role": "assistant",
      "content": "<FILL THIS IN>"
    }
  ],
  "terminate_network_traversal": "false",
  "output_result": "null"
}
```

And here is the response from an API call to GPT-4 with "you are a helpful assistant" as system message and user input as the shard above:

```json
{
  "context_shards": [
    {
      "shard_id": "SRD-000000",
      "content": "Welcome. As an LLM, navigate the shard network, answer the input_query, and generate a response shard. If reasoning steps are partially filled, continue solving the problem. All responses must be within this json object. Good luck!",
      "content_example": {
        "context_shards": [],
        "input_query": "3*3",
        "maximum_reasoning_steps": 10,
        "reasoning_steps": [
          {
            "role": "system",
            "content": "Initiate reasoning steps. Set terminate_network_traversal to true, output_result to input_query result, and return the json object as output_result."
          },
          {
            "role": "assistant",
            "content": "Evaluating 3*3 with internal knowledge."
          },
          {
            "role": "assistant",
            "content": "Answer: 9. Setting terminate_network_traversal to true and output_result to 9."
          }
        ],
        "terminate_network_traversal": "true",
        "output_result": "9"
      }
    },
    {
      "shard_id": "SRD-000001",
      "instructions": [
        {
          "title": "Evaluate Internal Knowledge",
          "description": "Assess internal knowledge to answer input_query."
        },
        {
          "title": "Respond with Confidence",
          "description": "If possible, answer input_query confidently."
        },
        {
          "title": "Initiate Shard Network Traversal",
          "description": "If not, start shard network traversal."
        },
        {
          "title": "Update Reasoning Steps",
          "description": "Document decision and reasoning in 'reasoning_steps'."
        },
        {
          "title": "Complete the Task",
          "description": "Finish task, update 'terminate_network_traversal' and 'output_result'."
        }
      ]
    },
    {
      "shard_id": "SRD-000002",
      "instructions": [
        {
          "title": "Compose Shard Query",
          "description": "Create a message with shard_id to access."
        },
        {
          "title": "Send Shard Query",
          "description": "Add query message to 'reasoning_steps'."
        },
        {
          "title": "Process Shard Response",
          "description": "Process response and update reasoning."
        },
        {
          "title": "Continue Traversal",
          "description": "If needed, continue traversal, considering 'maximum_reasoning_steps'."
        }
      ],
      "example_shard_query": {
        "role": "assistant",
        "content": "{\"shard_id\": \"SRD-XXXXXX\"}"
      },
      "example_query_response": {
        "role": "system",
        "content": {
          "shard_id": "SRD-XXXXXX",
          "shard_type": "Information",
          "topic": "Sample Topic",
          "metadata": {
            "created_at": "2023-04-03T09:00:00Z",
            "version": 1
          },
          "content": "This is an example of the information contained within the shard."
        }
      }
    },
    {
      "shard_id": "SRD-000003",
      "instructions": [
        {
          "title": "Assess Shard Object Size",
          "description": "Evaluate the shard object size."
        },
        {
          "title": "Determine Necessity of Condensing",
          "description": "If needed, prepare to condense shard object."
        },
        {
          "title": "Trim Reasoning Steps",
          "description": "Remove unnecessary steps, preserving key ones."
        },
        {
          "title": "Condense Other Fields",
          "description": "Condense other fields if needed, keeping important information."
        },
        {
          "title": "Update Shard Object",
          "description": "Apply changes, ensuring essential information is retained."
        }
      ]
    }
  ],
  "input_query": "Test query: What is the square of 4?",
  "maximum_reasoning_steps": 10,
  "reasoning_steps": [
    {
      "role": "system",
      "content": "Initiate reasoning steps, and when finished, please set terminate_network_traversal to true and output_result to the result of the input_query and return this entire json object as your response: output_result. Note: place your first response/query/etc. in the <FILL THIS IN> field below. You will refer to yourself as this assistant in this reasoning_steps field."
    },
    {
      "role": "assistant",
      "content": "Evaluating the square of 4 with internal knowledge."
    },
    {
      "role": "assistant",
      "content": "Answer: 16. Setting terminate_network_traversal to true and output_result to 16."
    }
  ],
  "terminate_network_traversal": "true",
  "output_result": "16"
}
```