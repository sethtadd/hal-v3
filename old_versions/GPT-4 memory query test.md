Here's the test query shard, which will force the instance to query for memory shard M00000:

```json
{
  "context_shards": [],
  "input_query": "Test query: What information does memory shard M00000 contain?",
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

The input query specifically asks for information from memory shard M00000, requiring the instance to query the shard network for it. Remember to populate context_shards before presenting this shard to the memoryless instance.



### GPT-4 TEST RESPONSE

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
  "input_query": "Test query: What information does memory shard M00000 contain?",
  "maximum_reasoning_steps": 10,
  "reasoning_steps": [
    {
      "role": "system",
      "content": "Initiate reasoning steps, and when finished, please set terminate_network_traversal to true and output_result to the result of the input_query and return this entire json object as your response: output_result. Note: place your first response/query/etc. in the <FILL THIS IN> field below. You will refer to yourself as this assistant in this reasoning_steps field."
    },
    {
      "role": "assistant",
      "content": "I cannot answer the query with my internal knowledge. Initiating shard network traversal by composing a shard query for M00000."
    },
    {
      "role": "assistant",
      "content": "{\"shard_id\": \"M00000\"}"
    }
  ],
  "terminate_network_traversal": "false",
  "output_result": "null"
}
```