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

def extract_tags(tags, tree, res):
    for tag in tags:
        res[re.sub(re.escape("-"), "_", tag)] = fg_text(tag, tree)
    return res

def extract_member(member):
    inv = {}
    for key in ['constituency', 'name-ch', 'name-en']:
        inv[re.sub(re.escape("-"), "_", key)] = member[key]
    inv['vote'] = member.find('vote').get_text()
    return inv

# TODO:
# vote-date and vote-time should be combined to vote-datetime
# mover-ch and mover-en and mover-type should be pushed into inviduals

def parse_vote(vote_tree):
    res = {}
    res['number'] = vote_tree['number'] # I don't think this value is important
    res = extract_tags(["vote-date", "vote-time", "motion-ch", "motion-en", 'mover-ch', 'mover-en', 'mover-type', 'vote-separate-mechanism'], vote_tree, res)
    # similarly if the movers are mover-type is Public Officer then vote-sep-mec is No.
    # Unless future change in counting (which is extremely unlikely). 
    # Still I will keep that
    vote_summary_tree = vote_tree.find("vote-summary")
    res['summaries'] = []
    for summary in vote_summary_tree.contents:
        vote_summary = {}
        vote_summary['type'] = summary.name
        vote_summary = extract_tags(['present-count', 'vote-count', 'yes-count', 'no-count', 'abstain-count', 'result'], summary, vote_summary)
        res['summaries'].append(vote_summary)
    res['individual_votes'] = []
    for member in vote_tree.find("individual-votes").find_all("member"):
        inv = extract_member(member)
        res['individual_votes'].append(inv)
    return res

print parse_meeting(vote_bs.find('meeting'))
