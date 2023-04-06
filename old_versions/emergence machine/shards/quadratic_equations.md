#shard #process 

This is an example of what a process shard might look like.

```json
// File: quadratic_equations.json
{
  "shard_id": "P0020",
  "shard_type": "Process",
  "topic": "Quadratic Equations",
  "metadata": {
    "created_at": "2027-06-15T09:00:00Z",
    "version": 2,
    "related_shards": ["C0101", "C0102", "M0015"]
  },
  "method": "Quadratic Formula",
  "formula": "x = (-b ± √(b² - 4ac)) / 2a",
  "steps": [
    {
      "title": "Identify Coefficients",
      "description": "Extract coefficients a, b, and c from the quadratic equation in the form ax² + bx + c = 0."
    },
    {
      "title": "Compute Discriminant",
      "description": "Calculate the discriminant Δ using the formula Δ = b² - 4ac."
    },
    {
      "title": "Evaluate Roots",
      "description": "Determine the roots x using the quadratic formula, x = (-b ± √Δ) / 2a, where ± indicates that there may be two solutions."
    }
  ],
  "conditions": [
    {
      "discriminant": "Δ > 0",
      "root_type": "Two distinct real roots",
      "description": "If the discriminant is greater than 0, the equation has two distinct real roots."
    },
    {
      "discriminant": "Δ = 0",
      "root_type": "One real root",
      "description": "If the discriminant is equal to 0, the equation has one real root (two coincident real roots)."
    },
    {
      "discriminant": "Δ < 0",
      "root_type": "Two complex roots",
      "description": "If the discriminant is less than 0, the equation has two complex roots (conjugate pairs)."
    }
  ]
}
```

And here is a more advanced version of the shard:

```json
{
  "shard_id": "P0021",
  "shard_type": "Process",
  "topic": "Quadratic Equations",
  "metadata": {
    "created_at": "2027-06-15T09:30:00Z",
    "version": 1,
    "related_shards": ["C0101", "C0102", "M0015", "P0020"]
  },
  "methods": [
    {
      "method": "Quadratic Formula",
      "formula": "x = (-b ± √(b² - 4ac)) / 2a",
      "applicable": "Always",
      "steps": [
        {
          "title": "Identify Coefficients",
          "description": "Extract coefficients a, b, and c from the quadratic equation in the form ax² + bx + c = 0."
        },
        {
          "title": "Compute Discriminant",
          "description": "Calculate the discriminant Δ using the formula Δ = b² - 4ac."
        },
        {
          "title": "Evaluate Roots",
          "description": "Determine the roots x using the quadratic formula, x = (-b ± √Δ) / 2a, where ± indicates that there may be two solutions."
        }
      ]
    },
    {
      "method": "Factoring",
      "applicable": "When the equation is factorable",
      "steps": [
        {
          "title": "Identify Coefficients",
          "description": "Extract coefficients a, b, and c from the quadratic equation in the form ax² + bx + c = 0."
        },
        {
          "title": "Factor the Equation",
          "description": "Factor the quadratic equation into the form (ax + m)(bx + n) = 0, where m and n are constants."
        },
        {
          "title": "Evaluate Roots",
          "description": "Determine the roots x by setting each factor equal to 0 and solving for x."
        }
      ]
    },
    {
      "method": "Completing the Square",
      "applicable": "When the equation is not easily factorable",
      "steps": [
        {
          "title": "Identify Coefficients",
          "description": "Extract coefficients a, b, and c from the quadratic equation in the form ax² + bx + c = 0."
        },
        {
          "title": "Transform the Equation",
          "description": "Transform the quadratic equation into the form a(x - h)² = k, where h and k are constants."
        },
        {
          "title": "Evaluate Roots",
          "description": "Determine the roots x by taking the square root of both sides and solving for x."
        }
      ]
    }
  ],
  "conditions": [
    {
      "discriminant": "Δ > 0",
      "root_type": "Two distinct real roots",
      "description": "If the discriminant is greater than 0, the equation has two distinct real roots."
    },
    {
      "discriminant": "Δ = 0",
      "root_type": "One real root",
      "description": "If the discriminant is equal to 0, the equation has one real root (two coincident real roots)."
    },
    {
      "discriminant": "Δ < 0",
      "root_type": "Two complex roots",
      "description": "If the discriminant is less than 0, the equation has two complex roots (conjugate pairs)."
    }
  ],
  "notes": [
    {
      "title": "Choosing the Best Method",
      "description": "Different methods for solving quadratic equations may be more suitable depending on the specific equation. Factoring is often the simplest method if the equation is easily factorable. If the equation is not easily factorable, completing the square can be a good option. The quadratic formula is always applicable and can be used as a fallback method if other methods are not suitable."
    }
  ]
}
```
