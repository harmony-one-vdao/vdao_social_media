from os.path import join
from time import sleep
from utils.tools import calc_extra_images
from includes.config import *
from glob import glob

spaces_len = len(glob(join(media_dir, "spaces", "*.jpg")))

send_data = {
    # HIP Proposals
    # join(tweets_dir, "hip", "hip9.txt"): join(media_dir, "HIP", "HIP9.png"),
    # join(tweets_dir, "hip", "hip10.txt"): join(media_dir, "HIP", "HIP10.png"),
    # join(tweets_dir, "hip", "hip11.txt"): join(media_dir, "HIP", "HIP11.png"),
    # join(tweets_dir, "hip", "hip12.txt"): join(media_dir, "HIP", "HIP12.png"),
    join(tweets_dir, "hip", "hip13.txt"): join(media_dir, "HIP", "HIP13.png"),
    # join(tweets_dir, "hip", "hip14.txt"): join(media_dir, "HIP", "HIP14.png"),
    # join(tweets_dir, "hip", "hip15.txt"): join(media_dir, "HIP", "HIP15.png"),
    # join(tweets_dir, "hip", "hip16.txt"): join(
    #     media_dir, "HIP", "HIP16.png"
    # ),  # reserved for BLSKeys
    # join(tweets_dir, "hip", "hip17.txt"): join(media_dir, "HIP", "HIP17.png"),
    # join(tweets_dir, "hip", "hip18.txt"): join(media_dir, "HIP", "HIP18.png"), # ON HOLD
    join(tweets_dir, "hip", "hip19.txt"): join(media_dir, "HIP", "HIP19.png"),
    # join(tweets_dir, "hip", "hip20.txt"): join(media_dir, "HIP", "HIP20.png"),
    join(tweets_dir, "hip", "hip21.txt"): join(media_dir, "HIP", "HIP21.png"),
    # join(tweets_dir, "hip", "hip22.txt"): join(media_dir, "HIP", "HIP22.png"),
    # join(tweets_dir, "hip", "hip23.txt"): join(media_dir, "HIP", "HIP23.png"),
    join(tweets_dir, "hip", "hip24.txt"): join(media_dir, "HIP", "HIP24.png"),
    # join(tweets_dir, "hip", "hip25.txt"): join(media_dir, "HIP", "HIP25.png"), 
    join(tweets_dir, "hip", "hip26.txt"): join(media_dir, "HIP", "HIP26.png"),
    join(tweets_dir, "hip", "hip27.txt"): join(media_dir, "HIP", "HIP27.png"),
    # DAO Specific
    # join(tweets_dir, "hip", "charter.txt"): join(media_dir, "HIP", "charter.png"),
    # generic
    join(tweets_dir, "generic", "dao_mission.txt"): join(
        media_dir, "generic", "Dao.png"
    ),
    join(tweets_dir, "generic", "agenda.txt"): join(media_dir, "generic", "Dao.png"),
    join(tweets_dir, "generic", "become_validator.txt"): join(
        media_dir, "generic", "new_validators.jpg"
    ),
    join(tweets_dir, "generic", "connect.txt"): join(media_dir, "generic", "Dao.png"),
    join(tweets_dir, "generic", "contact_details.txt"): None,
    # medium articles
    join(tweets_dir, "medium_articles", "volumes_expand.txt"): None,
    join(tweets_dir, "medium_articles", "what_is_vdao.txt"): None,
    join(tweets_dir, "medium_articles", "updating_node.txt"): None,
    join(tweets_dir, "medium_articles", "help_i_stopped_signing.txt"): None,
    join(tweets_dir, "medium_articles", "setup_on_testnet.txt"): None,
    join(tweets_dir, "medium_articles", "dve.txt"): None,
    join(tweets_dir, "medium_articles", "hetzner.txt"): None,
    join(tweets_dir, "medium_articles", "ovh.txt"): None,
    join(tweets_dir, "medium_articles", "all_guides.txt"): None,
    # Elections
    # join(tweets_dir, "election", "call_for_candidates.txt"): join(media_dir, "election", "call_for_candidates.png"),
    # join(tweets_dir, "election", "candidates_nominated.txt"): join(media_dir, "election", "candidates.png"),
    # join(tweets_dir, "election", "candidates_vote.txt"): join(media_dir, "election", "candidates.png"),
    # Spaces
    join(tweets_dir, "spaces", "spaces.txt"): [
        join(media_dir, "spaces", f"spaces{x}.jpg") for x in range(1, spaces_len + 1)
    ],
}

num_tweets = len(send_data.keys()) + calc_extra_images(send_data)
hours_between_tweets = (num_days_cycle * 24) / num_tweets
seconds_between_tweets = hours_between_tweets * 60 * 60

SLEEP = round(seconds_between_tweets)

p = {
    "num_days_cycle": num_days_cycle,
    "hours_between_tweets": hours_between_tweets,
    "num_tweets": num_tweets,
    "seconds_between_tweets": seconds_between_tweets,
    "SLEEP (secs)": SLEEP,
}


for k, v in p.items():
    # print(f"{k}  ::  {v}")
    log.info(f"{' '.join(k.split('_')).title():<50}  ::   {v:<30}")


# Generate
# for i in range(7, 16):
#     print(
#         "join(tweets_dir, 'hip', 'hip{}.txt'): join(media_dir, 'HIP', 'HIP{}.png'),".format(
#             i, i
#         )
#     )
