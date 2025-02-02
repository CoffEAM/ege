arr = open('txt/26_10107.txt').readlines()
events = [list(map(int, i.split())) for i in arr[1:]]
events = sorted(events, key=lambda x: (x[1], -x[0]))

true_events = [events[0]]

for event in events:
    if event[0] >= true_events[-1][1]:
        true_events.append(event)

print(len(true_events), events[-10:])

