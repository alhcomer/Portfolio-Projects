import requests

def get_contribution_count():
    contributions_json = requests.get("https://skyline.github.com/alhcomer/2022.json").json()
    contributions = contributions_json['contributions']
    contributions_count = 0
    for weekly_stats in contributions:
        for count in weekly_stats['days']:
            contributions_count += count['count']
            
    return contributions_count