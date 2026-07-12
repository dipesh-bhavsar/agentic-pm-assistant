from src.sprint_planner import plan_sprints
def test_single(): assert len(plan_sprints([{'title':'T','story_points':5,'priority':'high'}],10))==1
def test_overflow(): assert len(plan_sprints([{'title':f'T{i}','story_points':8,'priority':'medium'} for i in range(5)],20))>=2
def test_priority():
    tasks=[{'title':'Low','story_points':3,'priority':'low'},{'title':'High','story_points':3,'priority':'high'}]
    assert plan_sprints(tasks,10)[0].tasks[0]['title']=='High'
def test_empty(): assert plan_sprints([],30)==[]
