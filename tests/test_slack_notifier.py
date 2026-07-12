from unittest.mock import patch,MagicMock
from src.sprint_planner import plan_sprints
from src.slack_notifier import send_sprint_digest
def test_posts():
    s=plan_sprints([{'title':'T','story_points':5,'priority':'high'}],30)
    m=MagicMock(status_code=200); m.raise_for_status=MagicMock()
    with patch('httpx.post',return_value=m) as mp:
        assert send_sprint_digest('https://hooks.slack.com/x','P',s)==200 and mp.called
