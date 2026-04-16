# 🌌 DataVerse AI

An intelligent multi-agent data analysis system powered by **AutoGen**, **OpenAI**, and **Docker**, with a beautiful Streamlit interface for seamless data exploration and visualization.

## 🎯 Project Overview

**DataVerse AI** combines cutting-edge multi-agent orchestration with large language models to revolutionize data analysis. Upload a CSV, ask a question in natural language, and let our AI agents collaborate to generate insights and visualizations automatically.

### Key Capabilities
- 🤖 **Multi-Agent Collaboration** - Data Analyzer + Code Executor working in harmony
- 📊 **Automatic Analysis** - Statistical analysis, pattern detection, insights
- 📈 **Smart Visualizations** - Generates charts, graphs, and visual reports
- 🔧 **Code Execution** - Safe Python execution in isolated Docker containers
- 💬 **Natural Language** - Ask questions in plain English
- 🎨 **Beautiful UI** - Modern Streamlit interface

---

## 📋 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/yourusername/dataverse-ai.git
cd dataverse-ai

# 2. Create environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Run application
streamlit run streamlit_app.py
```

Open your browser to `http://localhost:8501` 🚀


## ✨ Features

### Core Capabilities
| Feature | Description | Status |
|---------|-------------|--------|
| **CSV Upload** | Support for large CSV files | ✅ |
| **Natural Language Queries** | Ask questions in plain English | ✅ |
| **Automated Analysis** | Statistical analysis & insights | ✅ |
| **Visualization** | Auto-generated charts & graphs | ✅ |
| **Code Execution** | Safe Python code execution | ✅ |
| **Conversation History** | Full chat history management | ✅ |
| **Multi-Agent System** | Agents working together | ✅ |
| **Docker Integration** | Isolated code execution | ✅ |
| **Session Persistence** | State management | ✅ |
| **Error Handling** | Robust exception management | ✅ |

---

## 🛠️ Tech Stack

```
┌─────────────────────────────────────────────┐
│          DATAVERSE AI TECH STACK            │
├─────────────────────────────────────────────┤
│                                             │
│  Frontend:        Streamlit                 │
│  Backend:         Python 3.10+              │
│  AI/ML:          AutoGen + OpenAI           │
│  Execution:       Docker                    │
│  Database:        CSV/Pandas                │
│  Visualization:   Matplotlib/Seaborn        │
│                                             │
└─────────────────────────────────────────────┘
```

### Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `autogen-agentchat` | Latest | Multi-agent orchestration |
| `autogen-ext` | Latest | Docker & OpenAI extensions |
| `openai` | Latest | GPT-4/GPT-3.5 integration |
| `streamlit` | Latest | Web UI framework |
| `pandas` | Latest | Data manipulation |
| `matplotlib` | Latest | Visualization |
| `docker` | Latest | Container management |

---

## 🏗️ Architecture

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      DATAVERSE AI SYSTEM                     │
└──────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴──────────────┐
                │                            │
        ┌───────▼────────┐         ┌────────▼────────┐
        │   STREAMLIT    │         │   FASTAPI/CLI   │
        │   Web UI       │         │   (Optional)    │
        └───────┬────────┘         └────────┬────────┘
                │                            │
                └─────────────┬──────────────┘
                              │
                    ┌─────────▼─────────┐
                    │  REQUEST HANDLER  │
                    └─────────┬─────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    ┌───▼────────┐   ┌───────▼───────┐   ┌────────▼────┐
    │   Config   │   │   Team Init   │   │   History   │
    │  Manager   │   │   (AutoGen)   │   │  Manager    │
    └────────────┘   └───────┬───────┘   └─────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
        ┌───▼───────────────────────────────┐  │
        │   MULTI-AGENT TEAM                │  │
        │ (RoundRobinGroupChat - AutoGen)   │  │
        ├───────────────────────────────────┤  │
        │ Max Turns: 10                     │  │
        │ Termination: "STOP" keyword       │  │
        └───┬───────────────────────────┬───┘  │
            │                           │       │
    ┌───────▼──────────────┐   ┌───────▼──────────────┐
    │ DATA ANALYZER AGENT  │   │ CODE EXECUTOR AGENT  │
    ├──────────────────────┤   ├──────────────────────┤
    │ • Analyzes data      │   │ • Executes Python    │
    │ • Plans approach     │   │ • Creates plots      │
    │ • Writes Python code │   │ • Saves output       │
    │ • Generates insights │   │ • Error handling     │
    │                      │   │ • Isolated env       │
    │ LLM: OpenAI (GPT-4)  │   │                      │
    └──────────────────────┘   └──────────┬───────────┘
                                          │
                            ┌─────────────▼──────────────┐
                            │  DOCKER CONTAINER          │
                            ├────────────────────────────┤
                            │ • Python 3.11              │
                            │ • pandas, numpy            │
                            │ • matplotlib, seaborn      │
                            │ • scipy, scikit-learn      │
                            │ • Temp workdir             │
                            │ • 120s timeout             │
                            └────────────────────────────┘
```

### Data Flow

```
CSV File Upload
     │
     ▼
User Question
     │
     ▼
Data Analyzer Agent (LLM thinks)
     │ ├─ Understands task
     │ ├─ Plans approach
     │ └─ Generates Python code
     │
     ▼
Code Executor Agent
     │ ├─ Receives code
     │ ├─ Runs in Docker
     │ └─ Captures output
     │
     ▼
Data Analyzer Agent (Review)
     │ ├─ Analyzes results
     │ ├─ Extracts insights
     │ └─ Formats response
     │
     ▼
Streamlit Display
     │ ├─ Chat messages
     │ ├─ Visualizations
     │ └─ Output files
     │
     ▼
User Views Results ✅
```

### Verification

```bash
python --version      # Should be 3.10+
docker --version      # Should be installed
git --version         # Should be installed
```

---

## ⚙️ Configuration

### OpenAI Model Selection

Edit `config/openai_model_client.py`:

```python
def get_model_client():
    return OpenAIChatCompletionClient(
        model='gpt-4o',
        api_key=api_key
    )
```

### Docker Configuration

Edit `config/docker_utils.py`:

```python
def getDockerCommandLineExecutor():
    return DockerCommandLineCodeExecutor(
        work_dir='temp',      # Working directory
        timeout=120,          # Max 2 minutes per execution
        image='python-data-tools:latest'  # Docker image
    )
```

### Agent Customization

Edit `agents/prompts/DataAnalyzerAgentPrompt.py` to customize the agent's behavior:

```python
DATA_ANALYZER_MSG = '''
You are a Data analyst agent with expertise in Python and working with CSV Data.
[Customize your instructions here]
'''
```
---

## 💻 Usage

### Starting the Application

```bash
streamlit run streamlit_app.py
```

Automatically opens at: `http://localhost:8501`

### Using the Web Interface

#### 1️⃣ Upload CSV File
- Click **📁 Upload your CSV file**
- Select a `.csv` file (max 200MB)
- Wait for upload confirmation

#### 2️⃣ Enter Analysis Task
Click the input field and type your question:

```
Examples:
✓ "What are the column names and data types?"
✓ "Show me the top 5 rows of data"
✓ "Create a correlation heatmap for numerical columns"
✓ "What is the survival rate distribution?"
✓ "Calculate descriptive statistics"
✓ "Are there any missing values? Show me where"
✓ "Create a pie chart of categorical variables"
✓ "Show trends over time if applicable"
```

#### 3️⃣ Review Results
- **Data Analyst** 🤖 explains the approach
- **Code Runner** ⚙️ executes code
- Results display automatically
- Charts/images appear below

### Using from Command Line

```python
# main.py
import asyncio
from team.analyzer_gpt import getDataAnalyzerTeam
from config.openai_model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container

async def main():
    docker = getDockerCommandLineExecutor()
    client = get_model_client()
    team = getDataAnalyzerTeam(docker, client)
    
    await start_docker_container(docker)
    
    try:
        task = "Analyze data.csv and show top 5 rows"
        async for message in team.run_stream(task=task):
            print(message)
    finally:
        await stop_docker_container(docker)

asyncio.run(main())
```

Run with:
```bash
python main.py
```

---

## 🔄 How It Works

### Workflow Steps

```
1. USER SUBMITS REQUEST
   └─ CSV file + Natural language question

2. DATA ANALYZER AGENT THINKS
   ├─ Understands the question
   ├─ Plans the analysis approach
   ├─ Writes Python code
   └─ Sends code to executor

3. CODE EXECUTOR RUNS CODE
   ├─ Receives Python code
   ├─ Starts Docker container
   ├─ Executes code safely
   ├─ Captures output
   └─ Sends results back

4. DATA ANALYZER REVIEWS RESULTS
   ├─ Analyzes output
   ├─ Extracts key insights
   ├─ Formats human-readable response
   └─ Decides if more analysis needed

5. REPEAT UNTIL COMPLETE
   └─ When "STOP" is mentioned

6. STREAMLIT DISPLAYS RESULTS
   ├─ Shows conversation history
   ├─ Displays visualizations
   ├─ Exports generated files
   └─ User reviews analysis ✅
```

### Multi-Agent Communication

```python
# RoundRobinGroupChat ensures:
1. Data_Analyzer_Agent → sends task
2. CodeExecutor_Agent → executes code
3. Data_Analyzer_Agent → reviews results
4. ... repeat until "STOP" ...

# Termination Condition:
TextMentionTermination('STOP')
# Agent must explicitly say STOP to finish
```

**🚀 Ready to Transform Your Data Analysis?**

Made with 💜 and AI

</div>
