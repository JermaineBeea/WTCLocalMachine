# Terminal-Based AI Software & Tools

Here's a comprehensive guide to AI software that operates in the terminal:

## 🤖 Large Language Model (LLM) CLIs

### 1. **Claude Code (Anthropic)**
```bash
# Installation
pip install claude-code

# Usage
claude-code "implement a binary search algorithm"
claude-code --file myproject.py "add error handling"
```
- **Features**: Agentic coding, file editing, project understanding
- **Best for**: Development tasks, code generation
- **Link**: https://docs.claude.com/claude-code

### 2. **GitHub Copilot CLI**
```bash
# Installation
gh extension install github/gh-copilot

# Usage
gh copilot suggest "git command to undo last commit"
gh copilot explain "docker-compose up -d"
```
- **Features**: Command suggestions, explanations
- **Best for**: DevOps, Git, shell commands

### 3. **ChatGPT CLI (Shell-GPT)**
```bash
# Installation
pip install shell-gpt

# Usage
sgpt "how to find large files in linux"
sgpt --code "python script to rename files"
sgpt --shell "compress all .log files"
```
- **Features**: Code generation, shell commands, chat mode
- **Best for**: Quick queries, automation scripts

### 4. **Aider**
```bash
# Installation
pip install aider-chat

# Usage
aider
aider --model gpt-4 myfile.py
```
- **Features**: Git integration, pair programming, multi-file editing
- **Best for**: Collaborative coding, refactoring

## 🧠 Local AI Models

### 5. **Ollama**
```bash
# Installation (Linux/macOS)
curl -fsSL https://ollama.com/install.sh | sh

# Usage
ollama run llama3.2
ollama run codellama "write a fibonacci function"
ollama run mistral
```
- **Features**: Run LLMs locally, no API needed
- **Models**: Llama, Mistral, CodeLlama, Phi, Gemma
- **Best for**: Privacy, offline usage, experimentation

### 6. **LM Studio CLI**
```bash
# After installing LM Studio
lms server start
lms chat --model llama-3-8b
```
- **Features**: Local model hosting, OpenAI-compatible API
- **Best for**: Running large models locally

### 7. **LocalAI**
```bash
# Docker installation
docker run -p 8080:8080 localai/localai

# Usage
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Hello"}]}'
```
- **Features**: OpenAI-compatible, self-hosted
- **Best for**: API compatibility, local deployment

## 💬 Chat Interfaces

### 8. **ChatGPT in Terminal (chatgpt-cli)**
```bash
# Installation
npm install -g @j178/chatgpt

# Usage
chatgpt "explain kubernetes"
chatgpt -m gpt-4 "debug this error"
```

### 9. **Mods**
```bash
# Installation
brew install mods  # macOS
go install github.com/charmbracelet/mods@latest

# Usage
mods "what is the capital of France"
cat error.log | mods "explain this error"
```
- **Features**: Pipe support, multiple AI backends
- **Best for**: Unix pipeline integration

## 🔧 Specialized AI Tools

### 10. **Codeium CLI**
```bash
# Installation
curl -fsSL https://codeium.com/install | sh

# Usage - integrates with your editor
codeium auth
```
- **Features**: Autocomplete, chat, command search
- **Best for**: Editor integration, free alternative to Copilot

### 11. **Cursor (with Terminal)**
```bash
# Has built-in terminal with AI features
# AI can execute commands directly
```
- **Features**: AI-powered terminal, command generation
- **Best for**: Integrated development environment

### 12. **Warp AI**
- **Terminal**: Built-in AI terminal
- **Features**: Command search, error explanation, autocomplete
- **Best for**: Modern terminal with AI built-in
- **Link**: https://www.warp.dev/

## 📊 AI-Powered Data Tools

### 13. **GPT CLI for Data Analysis**
```bash
pip install gpt-data-analyst

# Usage
gpt-analyze sales_data.csv "show trends"
```

### 14. **Julius AI CLI**
```bash
# Data analysis and visualization
julius analyze data.csv
```

## 🎨 Creative AI Tools

### 15. **ImageMagick with AI**
```bash
# Installation
apt-get install imagemagick

# Usage with AI enhancement scripts
convert input.jpg -enhance output.jpg
```

### 16. **Stable Diffusion CLI**
```bash
# Installation
pip install diffusers transformers

# Usage
python -m scripts.txt2img --prompt "a cat in space"
```

## 🔍 Code Analysis & Review

### 17. **AI Code Review Tools**
```bash
# CodeRabbit CLI
npm install -g coderabbit

# Usage
coderabbit review --pr 123
```

### 18. **Sourcery CLI**
```bash
# Installation
pip install sourcery-cli

# Usage
sourcery review myfile.py
```

## 📝 Writing & Documentation

### 19. **Markdown AI Tools**
```bash
# AI-powered markdown linting
npm install -g markdownlint-cli

# Usage with AI suggestions
markdownlint README.md --fix
```

### 20. **Grammarly CLI**
```bash
# Community tools
pip install grammarly-api

# Usage
grammarly check document.txt
```

## 🛠️ Installation Quick Start

### Most Popular Setup (Python-based)

```bash
# Install Python package manager
pip install --upgrade pip

# Install multiple AI CLIs
pip install shell-gpt aider-chat claude-code

# Configure API keys
export OPENAI_API_KEY="your-key"
export ANTHROPIC_API_KEY="your-key"

# Test
sgpt "hello world"
```

### Local AI Setup (No API Keys)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download a model
ollama pull llama3.2

# Run
ollama run llama3.2 "write a bash script to backup files"
```

## 💡 Best Practices

### 1. **Choose Based on Use Case**
- **Quick queries**: Shell-GPT, Mods
- **Coding tasks**: Aider, Claude Code, Copilot
- **Privacy/Offline**: Ollama, LocalAI
- **Data analysis**: GPT Data Analyst

### 2. **Set Up Aliases**
```bash
# Add to ~/.bashrc or ~/.zshrc
alias ai='sgpt'
alias code-ai='aider'
alias local-ai='ollama run llama3.2'
```

### 3. **Security Considerations**
- Store API keys in environment variables
- Use `.env` files (add to `.gitignore`)
- Consider local models for sensitive data

### 4. **Cost Management**
```bash
# Use local models when possible
ollama run codellama

# Set token limits for API calls
sgpt --max-tokens 500 "your query"
```

## 🎯 Recommended Combination

For a complete terminal AI setup:

```bash
# 1. Local AI (free, private)
ollama pull llama3.2

# 2. Cloud AI for complex tasks (paid)
pip install shell-gpt

# 3. Code-specific AI (paid/free)
pip install aider-chat

# 4. Terminal enhancement
brew install warp  # or download Warp terminal
```

## 📚 Resources

- **Awesome AI CLI Tools**: https://github.com/awesome-ai-tools/awesome-cli-ai
- **Ollama Models**: https://ollama.com/library
- **LLM Comparison**: https://artificialanalysis.ai/

---

**Note**: Most cloud-based tools require API keys. Local tools like Ollama are completely free and private but may require significant computational resources (8GB+ RAM for larger models).
