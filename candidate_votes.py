file_path = r"C:\Users\tio\Downloads\input (2).txt"


def count_votes(data: list) -> dict:
    """
    Count total votes for each candidate

    :param data: A list of strings containing candidate names and votes
    :return: A dictionary with candidate names as keys and total votes as values
    """
    votes_dict = {}
    for line in data:
        candidate, votes = line.split()
        votes = int(votes)
        votes_dict[candidate] = votes_dict.get(candidate, 0) + votes
    return votes_dict


def count_states(data: list) -> dict:
    """
    Count how many states voted for each candidate

    :param data: A list of strings that contesin candidate names
    :return: A dictionary with candidate names as keys and state counts as values
    """
    states_dict = {}
    for line in data:
        candidate = line.split()[0]
        states_dict[candidate] = states_dict.get(candidate, 0) + 1
    return states_dict


def find_winner(vote_counts: dict) -> str:
    """
    Determine the winner of the election

    :param vote_counts: A dictionary with candidate names as keys and their votes as values
    :return: The name of the winner or a message for a third part of elections
    """
    max_votes = max(vote_counts.values())
    winners = []

    for candidate, votes in vote_counts.items():
        if votes == max_votes:
            winners.append(candidate)

    if len(winners) > 1:
        return "elections need third part"
    else:
        return winners[0]


with open(file_path, mode='r', encoding='utf-8') as file:
    file_data = file.readlines()

total_votes = count_votes(file_data)
total_states = count_states(file_data)

election_winner = find_winner(total_votes)

print(total_states)
print(total_votes)
print("Elected:", election_winner)
