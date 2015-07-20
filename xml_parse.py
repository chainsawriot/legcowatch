from bs4 import BeautifulSoup

vote = open("cm_vote_20150617.xml", "r").read()
vote_bs = BeautifulSoup(vote, "html.parser")
print votebs.find("meeting")['start-date']

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

def parse_vote(vote_tree):
    res = {}
    res['number'] = vote_tree['number']
    for tag in ["vote-date", "vote-time", "motion-ch", "motion-en", 'mover-ch', 'mover-en', 'mover-type', 'vote-separate-mechanism']:
        res[tag] = fg_text(tag, vote_tree)
    vote_summary = vote_tree.find("vote-summary")
    return res
