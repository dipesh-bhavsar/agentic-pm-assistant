from dataclasses import dataclass, field
@dataclass
class Sprint:
    number:int; capacity:int; tasks:list=field(default_factory=list)
    @property
    def used_points(self): return sum(t.get('story_points',0) for t in self.tasks)
    @property
    def remaining(self): return self.capacity-self.used_points
def plan_sprints(tasks,capacity_per_sprint=30):
    order={'high':0,'medium':1,'low':2}
    sorted_tasks=sorted(tasks,key=lambda t:order.get(t.get('priority','low'),2))
    sprints,current=[],Sprint(number=1,capacity=capacity_per_sprint)
    for task in sorted_tasks:
        if task.get('story_points',1)>current.remaining:
            sprints.append(current); current=Sprint(number=len(sprints)+1,capacity=capacity_per_sprint)
        current.tasks.append(task)
    if current.tasks: sprints.append(current)
    return sprints
