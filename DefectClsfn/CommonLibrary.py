from jira.client import JIRA

def getDefectSummary(prProject=None, prDefectId=None):
    key_list = []
    summary_list = []
    jira_options = {'server': 'https://servicedesk.oversightsystems.com'}
    jira = JIRA(options=jira_options, basic_auth=('tanmay.vaidya', 'l3tV41d41n!2019'))
    jql = 'project = {} AND key = {}'.format(prProject,prDefectId)
    issueList = jira.search_issues(jql)
    for issue in issueList:
        key_list.append(issue.key)
        summary_list.append(issue.fields.summary)
    return summary_list




#issues_in_project = jira.search_issues('project = WB AND key in ( WB-3206, WB-3205)')

#print(issues_in_project)

# key_list = []
# summary_list = []
# descr_list = []
#
# for issue in issues_in_project:
#     key_list.append(issue.key)
#     summary_list.append(issue.fields.summary)
#
# print("== summary==", summary_list)