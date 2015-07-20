from bs4 import BeautifulSoup
import re

vote = open("cm_vote_20150617.xml", "r").read()
vote_bs = BeautifulSoup(vote, "html.parser")

def parse_meeting(meeting_tree):
    res = {}
    res['start-date'] = meeting_tree['start-date']
    res['vote'] = []
    for vote in meeting_tree.find_all("vote", number = True):
        parsed_vote = parse_vote(vote)
        res['vote'].append(parsed_vote)
    return res


def fg_text(tag_name, tree):
    return tree.find(tag_name).get_text()

# TODO:
# vote-date and vote-time should be combined to vote-datetime
# mover-ch and mover-en and mover-type should be pushed into inviduals

def parse_vote(vote_tree):
    res = {}
    res['number'] = vote_tree['number'] # I don't think this value is important
    for tag in ["vote-date", "vote-time", "motion-ch", "motion-en", 'mover-ch', 'mover-en', 'mover-type', 'vote-separate-mechanism']:
        res[re.sub(re.escape("-"), "_", tag)] = fg_text(tag, vote_tree)
        # similarly if the movers are mover-type is Public Officer then vote-sep-mec is No.
        # Unless future change in counting (which is extremely unlikely). 
        # Still I will keep that
    vote_summary_tree = vote_tree.find("vote-summary")
    for summary in vote_summary_tree.contents:
        vote_summary = {}
        vote_summary['type'] = summary.name
        for tag in ['present-count', 'vote-count', 'yes-count', 'no-count', 'abstain-count', 'result']:
            vote_summary[re.sub(re.escape("-"), "_", tag)] = fg_text(tag, summary)
        print vote_summary
    return res
