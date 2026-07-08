import httpx
def send_sprint_digest(webhook_url,project_name,sprints):
    total=sum(sum(t.get('story_points',0) for t in s.tasks) for s in sprints)
    lines=[f'*Sprint Plan: {project_name}*',f'{len(sprints)} sprints, {total} pts','']
    for s in sprints:
        summary=', '.join(t['title'] for t in s.tasks[:3])+('...' if len(s.tasks)>3 else '')
        lines.append(f'*Sprint {s.number}* ({s.used_points}/{s.capacity} pts): {summary}')
    r=httpx.post(webhook_url,json={'text':chr(10).join(lines)},timeout=10)
    r.raise_for_status(); return r.status_code
