import streamlit as st
from src.task_extractor import extract_tasks
from src.sprint_planner import plan_sprints
st.set_page_config(page_title='Agentic PM Assistant',layout='wide')
st.title('Agentic PM Assistant')
brief=st.text_area('Paste project brief',height=200)
velocity=st.slider('Team velocity (pts/sprint)',10,60,30)
if st.button('Generate Sprint Plan',type='primary'):
    if not brief: st.error('Enter a brief.'); st.stop()
    with st.spinner('Extracting...'): result=extract_tasks(brief)
    st.success(f"Project: {result['project_name']} | {len(result['tasks'])} tasks")
    for s in plan_sprints(result['tasks'],velocity):
        with st.expander(f'Sprint {s.number} ({s.used_points}/{s.capacity} pts)'):
            for t in s.tasks: st.markdown(f"- **{t['title']}** ({t.get('priority')}, {t.get('story_points')} pts)")
