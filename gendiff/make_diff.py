def make_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    diff = []

    for key in keys:
        if key not in dict1:
            diff.append({
                'key': key,
                'status': 'added',
                'value': dict2[key]})
        elif key not in dict2:
            diff.append({
                'key': key,
                'status': 'removed',
                'value': dict1[key]})
        elif dict1[key] == dict2[key]:
            diff.append({
                'key': key,
                'status': 'unchanged',
                'value': dict1[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append({
                'key': key,
                'status': 'nested',
                'children': make_diff(dict1[key], dict2[key])})
        else:
            diff.append({
                'key': key,
                'status': 'changed',
                'old_value': dict1[key],
                'new_value': dict2[key]
            })

    return diff
