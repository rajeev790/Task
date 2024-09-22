from collections import defaultdict

def aggregate_data(data, key, aggregator):
    grouped_data = defaultdict(list)
    
    for item in data:
        grouped_data[item[key]].append(item)

    return {k: aggregator([d['value'] for d in v]) for k, v in grouped_data.items()}

# Example usage:
data = [{'city': 'NY', 'value': 10}, {'city': 'LA', 'value': 15}, {'city': 'NY', 'value': 20}]
result = aggregate_data(data, 'city', sum)
print(result)  # {'NY': 30, 'LA': 15}
