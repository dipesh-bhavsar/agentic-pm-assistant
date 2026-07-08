import json, os
from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
SCHEMA = {'name':'extract_tasks','description':'Extract tasks from brief','parameters':{'type':'object','properties':{'project_name':{'type':'string'},'tasks':{'type':'array','items':{'type':'object','properties':{'title':{'type':'string'},'priority':{'type':'string','enum':['high','medium','low']},'story_points':{'type':'integer'}},'required':['title','priority','story_points']}}},'required':['project_name','tasks']}}
def extract_tasks(brief: str) -> dict:
    r=client.chat.completions.create(model=os.getenv('MODEL','gpt-4o-mini'),messages=[{'role':'system','content':'You are an expert PM.'},{'role':'user','content':brief}],functions=[SCHEMA],function_call={'name':'extract_tasks'})
    return json.loads(r.choices[0].message.function_call.arguments)
