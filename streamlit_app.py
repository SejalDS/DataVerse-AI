import streamlit as st
import asyncio
import os
from team.analyzer_gpt import getDataAnalyzerTeam

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

from config.openai_model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor,start_docker_container,stop_docker_container

# Page configuration
st.set_page_config(
    page_title="DataVerse",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.8em;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.3em;
        text-align: center;
    }
    
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.1em;
        margin-bottom: 2.5em;
        font-weight: 500;
    }
    
    .upload-label {
        font-size: 1.1em;
        font-weight: 600;
        color: #333;
        margin-bottom: 1em;
        display: block;
    }
    
    .input-label {
        font-size: 1.1em;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.8em;
        display: block;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 2em 0;
        border-radius: 1px;
    }
    
    .output-container {
        background: white;
        padding: 2em;
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        margin-top: 2em;
        border: 1px solid #e0e0e0;
    }
    
    .output-label {
        font-size: 1.1em;
        font-weight: 600;
        color: #333;
        margin-bottom: 1em;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<div class="main-title">📊 DataVerse</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Intelligent Data Analyzer Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown('<span class="upload-label">📁 Upload your CSV file</span>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader('Upload CSV', type='csv', key='file_uploader')

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown('<span class="input-label">💬 Enter your analysis task</span>', unsafe_allow_html=True)
    task = st.chat_input("e.g., 'How many columns are in my data?' or 'Create a visualization of survival rates'")

async def run_analyzer_gpt(docker,openai_model_client,task):

    try:
        await start_docker_container(docker)
        team = getDataAnalyzerTeam(docker,openai_model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)
        
        
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(msg := f"{message.source} : {message.content}")
                # yield msg
                if msg.startswith('user'):
                    with st.chat_message('user', avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith('Data_Analyzer_Agent'):
                    with st.chat_message('Data Analyst', avatar='🤖'):
                        st.markdown(msg)                
                elif msg.startswith('CodeExecutor'):
                    with st.chat_message('Code Runner', avatar='⚙️'):
                        st.markdown(msg)
                st.session_state.messages.append(msg)

            elif isinstance(message,TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                # yield msg
                with st.info("✅ Analysis Complete"):
                    st.markdown(msg)
                st.session_state.messages.append(msg)

        st.session_state.autogen_team_state = await team.save_state()
        return None
    except Exception as e:
        print(e)
        return e
    finally:
        await stop_docker_container(docker)
                
if st.session_state.messages:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #333; text-align: center; margin-bottom: 2em;">📝 Conversation History</h2>', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        st.markdown(msg)


if task:
    if uploaded_file is not None and task:
        
        if not os.path.exists('temp'):
            os.makedirs('temp')

        with open('temp/data.csv','wb') as f:
            f.write(uploaded_file.getbuffer())

    
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    with st.spinner('🔄 Analyzing your data... This may take a moment.'):
        error = asyncio.run(run_analyzer_gpt(docker, openai_model_client, task))

    if error:
        st.error(f"❌ An error occurred: {error}")

    if os.path.exists('temp/output.png'):
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="output-label">📊 Generated Analysis</div>', unsafe_allow_html=True)
        st.image('temp/output.png', caption='Analysis Result')
    
else:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.warning("⚠️ Please upload a CSV file and enter your analysis task to begin")