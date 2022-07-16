from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = sum(bridge)

    while bridge:
        bridge_weight -= bridge[0]
        bridge.popleft()
        time += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return time