import io

SCORES_FILE_NAME = "scores.csv"
LOG_FILE_NAME = "log.txt"
MAX_SCORES = 20


def get_data():
    data = []
    with open(SCORES_FILE_NAME, "r") as f:
        for line in f:
            data.append(line.strip().split(","))
    return data


def add_data(new_score):
    current_data = get_data()
    current_data.append(new_score)
    sorted_data = sorted(
        current_data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]))
    )[:MAX_SCORES]
    if player_already_exists(new_score[0]):
        update_player_score_if_higher(new_score)
        return

    with io.open(SCORES_FILE_NAME, "w", encoding="utf-8") as f:
        for line in sorted_data:
            f.write(",".join(line) + "\n")


def update_log(log_data):
    with io.open(LOG_FILE_NAME, "a", encoding="utf-8") as f:
        for key in log_data:
            f.write(f"{key}: {log_data[key]}" + "\n")


def player_already_exists(player_name):
    data = get_data()
    for line in data:
        if line[0] == player_name:
            return True
    return False


def update_player_score_if_higher(new_score):
    prev_data = get_data()
    for i, line in enumerate(prev_data):
        if line[0] == new_score[0]:
            if new_score_is_higher(new_score, line):
                prev_data[i] = (new_score[1], new_score[1], new_score[2], new_score[3])
                replace_data(prev_data)
            return


def new_score_is_higher(new_score, old_score):
    return (
        new_score[1] > old_score[1]
        or (new_score[1] == old_score[1] and new_score[2] < old_score[2])
        or (
            new_score[1] == old_score[1]
            and new_score[2] == old_score[2]
            and new_score[3] > old_score[3]
        )
    )


def replace_data(new_data):
    with io.open(SCORES_FILE_NAME, "w", encoding="utf-8") as f:
        for line in new_data:
            f.write(",".join(line) + "\n")
