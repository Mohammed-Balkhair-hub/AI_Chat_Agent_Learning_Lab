# SDKs Playground

A learning lab for exploring and comparing different AI provider SDKs through hands-on notebooks. This folder contains practical examples and tutorials for working with various AI APIs including Mistral AI, Claude (Anthropic), Google, OpenAI, Hugging Face, Cohere, and more.

## 🎯 Purpose

This playground is designed to help learners:

- **Compare SDKs**: See how different AI providers implement their APIs
- **Learn Best Practices**: Understand common patterns across SDKs
- **Build Real Projects**: Work through practical examples like CV scoring and RAG systems
- **Understand Differences**: See how each SDK handles authentication, API calls, and responses

## 📁 Structure

```
SDKs_playground/
├── README.md              # This file
├── pyproject.toml        # Separate environment configuration
├── claude/               # Claude (Anthropic) SDK examples
│   └── claude.ipynb
├── mistral/              # Mistral AI SDK examples
│   └── mistral.ipynb
├── google/               # Google Gemini SDK examples
│   ├── 1_google_prompting.ipynb
│   ├── 2_google_evaluation-and-structured-output.ipynb
│   ├── 3_google_qa_rag.ipynb
│   └── 4_google_similarity.ipynb
└── CVs/                  # Sample CVs for projects
    ├── Topic_1/
    ├── Topic_2/
    └── Topic_3/
```

## 🔧 Setup

### Separate Environment

**Important**: This folder has its own `pyproject.toml` with its own dependencies. This allows you to set up this playground independently from the main project.

### Installation Steps

1. **Navigate to the SDKs_playground directory:**
   ```bash
   cd SDKs_playground
   ```

2. **Install dependencies using `uv`:**
   ```bash
   uv sync
   ```
   
   This will create a virtual environment and install all required SDKs and dependencies.

3. **Set up environment variables:**
   
   Create a `.env` file in the `SDKs_playground` directory with your API keys:
   ```env
   # Mistral AI
   MISTRAL_API_KEY=your_mistral_api_key_here
   
   # Anthropic (Claude)
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # OpenAI
   OPENAI_API_KEY=your_openai_api_key_here
   
   # OpenRouter
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   
   # Google
   GOOGLE_API_KEY=your_google_api_key_here
   
   # Hugging Face
   HUGGINGFACE_API_KEY=your_huggingface_api_key_here
   
   # Cohere
   COHERE_API_KEY=your_cohere_api_key_here
   ```

4. **Launch Jupyter:**
   ```bash
   uv run jupyter notebook
   ```
   
   Or if using JupyterLab:
   ```bash
   uv run jupyter lab
   ```

## 📚 Core Practices

### Notebook Structure

All notebooks in this playground follow these core principles:

#### 1. **Short, Focused Cells**

Each code cell should be **5-15 lines maximum**. This makes it easy to:
- Understand what each cell does
- Debug issues quickly
- Run cells independently
- Learn step-by-step

**Good Example:**
```python
# Initialize the Mistral client
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)
print("Client initialized!")
```

**Avoid:**
```python
# Don't put 50+ lines in one cell
# It becomes hard to understand and debug
```

#### 2. **Clear Markdown Explanations**

Every code section should have a markdown cell above it explaining:
- **What** the code does
- **Why** it's important
- **How** it fits into the bigger picture

**Example:**
```markdown
### Initialize the Client

The Mistral SDK uses a `Mistral` client object to make requests. 
The client handles authentication using your API key.
```

#### 3. **Progressive Complexity**

Start simple, then build complexity:

1. **Basic**: Simple API call
2. **Intermediate**: Add parameters, handle responses
3. **Advanced**: Build complete projects (CV scoring, RAG systems)

#### 4. **Self-Contained Cells**

Each cell should be runnable after all previous cells have been executed. Avoid:
- Cells that depend on variables from cells far above
- Cells that only work in a specific order without clear indication

#### 5. **Clear Variable Names**

Use descriptive variable names:
- ✅ `cv_content` instead of `c`
- ✅ `scoring_result` instead of `r`
- ✅ `job_description` instead of `jd`

#### 6. **Comments for Complex Logic**

Add comments when the code does something non-obvious:

```python
# Convert to float32 (required by FAISS)
index.add(cv_embeddings.astype('float32'))
```

#### 7. **Display Results Clearly**

Always show what the code produces:
- Use `print()` statements
- Display formatted results with `display(Markdown(...))`
- Show shapes, lengths, and key information

## 📖 Notebook Examples

### Mistral AI Notebook (`mistral/mistral.ipynb`)

A complete tutorial covering:
1. **Getting Started**: Basic API calls, initialization, chat conversations
2. **CV Scoring Project**: Score a single CV against a job description
3. **RAG-Based Retrieval**: Use FAISS for fast retrieval + Mistral for intelligent re-ranking

### Claude Notebook (`claude/claude.ipynb`)

Similar structure to Mistral notebook, demonstrating:
- Claude SDK usage
- CV scoring with Claude
- Hybrid RAG approach (FAISS + Claude)

### Google Notebooks (`google/`)

Multiple focused notebooks:
- Prompting techniques
- Evaluation and structured outputs
- Q&A with RAG
- Similarity search

## 🎓 Learning Path

### For Beginners

1. Start with **one SDK** (e.g., Mistral or Claude)
2. Run through **Part 1** (Getting Started) to understand basic API calls
3. Try modifying the examples (change prompts, parameters)
4. Move to **Part 2** (CV Scoring) to see a practical application

### For Intermediate Learners

1. Compare how different SDKs handle the same task
2. Try implementing the CV scoring project with multiple SDKs
3. Experiment with the RAG system (Part 3)
4. Modify the projects to add your own features

### For Advanced Learners

1. Build your own projects using the patterns shown
2. Compare performance and costs across SDKs
3. Implement advanced features (streaming, function calling, etc.)
4. Create your own notebooks following the same practices

## 🔑 Key Concepts Demonstrated

### 1. SDK Initialization

Each SDK has its own way to initialize:
- **Mistral**: `Mistral(api_key=api_key)`
- **Claude**: `Anthropic(api_key=api_key)`
- **Google**: `genai.Client(api_key=api_key)`

### 2. Message Format

Most SDKs use similar message formats:
```python
messages = [
    {"role": "user", "content": "Your prompt here"}
]
```

### 3. API Calls

Patterns vary but follow similar structure:
- **Mistral**: `client.chat.complete(model="...", messages=[...])`
- **Claude**: `client.messages.create(model="...", messages=[...])`
- **Google**: `client.models.generate_content(model="...", contents="...")`

### 4. Response Handling

Each SDK returns responses differently:
- **Mistral**: `response.choices[0].message.content`
- **Claude**: `response.content[0].text`
- **Google**: `response.text`

## 🛠️ Dependencies

This playground includes SDKs for:

- **Mistral AI** (`mistralai`)
- **Anthropic/Claude** (`anthropic`)
- **OpenAI** (`openai`)
- **Google** (`google-generativeai`)
- **Hugging Face** (`huggingface-hub`, `transformers`)
- **Cohere** (`cohere`)

Plus supporting libraries:
- **FAISS** (`faiss-cpu`) - Vector similarity search
- **Sentence Transformers** (`sentence-transformers`) - Document embeddings
- **Jupyter** (`jupyter`, `ipykernel`) - Notebook environment
- **Utilities** (`pandas`, `numpy`, `python-dotenv`)

See `pyproject.toml` for complete dependency list.

## 💡 Tips

1. **Run cells sequentially**: Each notebook builds on previous cells
2. **Read the markdown cells**: They explain the "why" behind the code
3. **Experiment**: Try changing parameters, prompts, or models
4. **Compare SDKs**: Notice similarities and differences between providers
5. **Check terminal output**: Some notebooks print transparency logs

## 🚀 Getting API Keys

- **Mistral AI**: [console.mistral.ai](https://console.mistral.ai/)
- **Anthropic (Claude)**: [console.anthropic.com](https://console.anthropic.com/)
- **OpenAI**: [platform.openai.com](https://platform.openai.com/)
- **Google**: [aistudio.google.com](https://aistudio.google.com/app/api-keys)
- **Hugging Face**: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- **Cohere**: [dashboard.cohere.com](https://dashboard.cohere.com/)

## 📝 Contributing

When adding new notebooks:

1. Follow the **core practices** outlined above
2. Keep cells **short and focused** (5-15 lines)
3. Add **clear markdown explanations**
4. Use **descriptive variable names**
5. **Display results** clearly
6. Test that cells run **sequentially** without errors

## 🔗 Related Resources

- Main project README: `../README.md`
- Main project: `../App/` - Agent Explorer Learning Lab
- Customization guide: `../App/CUSTOMIZATION.md`

---

**Happy Learning! 🎉**

Explore different SDKs, compare their approaches, and build your own AI applications!
