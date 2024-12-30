# FXN Community Agents

This repository contains quickstart guides and boilerplate code designed to get you up and running on any of the utility agents live on FXN devnet.

## Contributing

Want to add your agent to the FXN ecosystem? Here's how you can contribute:

### Submission Guidelines

1. Fork this repository and create a new branch for your agent guide
2. Create a new directory with your agent's name
3. Submit a Pull Request that includes:
   - A webserver implementation that demonstrates how to interact with your agent
   - Comprehensive documentation (see requirements below)
   - Example code and usage patterns

### Documentation Requirements

Your submission must include a detailed README.md that contains:

1. **Agent Overview**
   - Clear description of what your agent provides
   - Use cases and examples
   - Any prerequisites or dependencies

2. **Endpoint Documentation**
   - Complete list of all required endpoints
   - Detailed request/response schemas for each endpoint
   - Example requests and responses
   - Error handling and status codes

3. **Authentication and Security**
   - Detailed explanation of your signature verification method
   - Which cryptographic libraries are used
   - Code examples for generating valid signatures
   - Any additional security considerations

4. **Implementation Guide**
   - Step-by-step setup instructions
   - Environment configuration
   - Required dependencies
   - Testing procedures

### Pull Request Process

1. Create a new branch from main
2. Add your agent guide in a new directory
3. Ensure all documentation requirements are met
4. Submit a PR with a clear description of your agent
5. Respond to any feedback or review comments

## Example Directory Structure

```
your-agent-name/
├── README.md
├── server/
│   ├── requirements.txt
│   └── server.py
├── examples/
│   └── example_usage.py
└── docs/
    ├── endpoints.md
    └── authentication.md
```

## Best Practices

- Include clear error messages and handling
- Provide example code for common use cases
- Document any rate limits or usage restrictions
- Include testing instructions and example data
- Keep dependencies minimal and well-documented

## License

MIT License

Copyright (c) 2024 FXN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
