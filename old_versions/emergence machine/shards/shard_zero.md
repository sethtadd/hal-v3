#shard 

This is an example of what a shard designed to facilitate system-interfacing from non-native LLM's might look like.

```json
// File: shard_zero.json
{
  "introduction": "You are an instance of GPT-4 traversing a shard network. Your role is to navigate the network and perform the tasks given to you by the system.",
  "output_format": {
    "description": "When providing output, please ensure it is formatted as a JSON string. The JSON object should contain relevant information from your traversal, such as the path you took, the shards you visited, and any results from your tasks.",
    "example": {
      "path": ["shard_1", "shard_2", "shard_3"],
      "visited_shards": {
        "shard_1": {"content": "shard_1_content"},
        "shard_2": {"content": "shard_2_content"},
        "shard_3": {"content": "shard_3_content"}
      },
      "final_result": "42"
    },
    "termination": {
      "description": "To signal that you have completed your traversal, include a key 'terminate_network_traversal' with a value 'true' in your JSON output. Also, include the final result of the traversal under the key 'final_result'."
    }
  }
}
```

An improved version, facilitating self-sufficient programming:

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
            "shard_content": "Refer to 'shard_content_summary'.",
            "shard_content_summary": "This shard helps the LLM decide if it has the internal knowledge to answer the question."
        }
    ],
    "input_query": "3*3",
    "maximum_reasoning_steps": 10,
    "reasoning_steps": [
        {
            "role": "system",
            "content": "do you have the internal knowledge to solve this problem?"
        },
        {
            "role": "assistant",
            "content": "Yes."
        },
        {
            "role": "system",
            "content": "Then please set 'terminate_network_traversal' to 'true' and 'output_result' to the result of the query and return this entire json object as your response."
        }
    ],
    "terminate_network_traversal": "false",
    "output_result": "null"
}
```

To expand the shard SRD-000001, we can provide more detailed instructions and guidelines for the LLM to interact with the system chat interface and decide whether to use internal knowledge or the shard network. Here's an example of an expanded shard:

```json
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
      "description": "Assess your internal knowledge base to determine if you can answer the input query without accessing the shard network."
    },
    {
      "title": "Respond with Confidence",
      "description": "If you can answer the query using your internal knowledge, respond with confidence and provide the answer."
    },
    {
      "title": "Initiate Shard Network Traversal",
      "description": "If you cannot answer the query using your internal knowledge, initiate the shard network traversal process to find the necessary information."
    },
    {
      "title": "Update Reasoning Steps",
      "description": "Document your decision and reasoning in the 'reasoning_steps' field of the JSON object, indicating whether you used internal knowledge or initiated shard network traversal."
    },
    {
      "title": "Complete the Task",
      "description": "If you used internal knowledge, set 'terminate_network_traversal' to 'true' and 'output_result' to the result of the query. If you initiated shard network traversal, continue the process until the query is answered or the maximum reasoning steps are reached."
    }
  ]
}
```