# Load Balancer for Jupyter Servers
# Stripe's notebook platform runs multiple Jupyter servers and directs developers to different servers based on load.
# Implement a function route_requests that determines the target server for each incoming request.
# Function Parameters:
# int numTargets — number of target Jupyter servers
# int maxConnectionsPerTarget — max active connections per server (Part 4, ignore for now)
# string[] requests — each request is one of:
#
# CONNECT,connectionId,userId,objectId
# DISCONNECT,connectionId,userId,objectId
#
# Returns:
# string[] — one log entry per CONNECT request in the format connectionId,userId,targetIndex (targetIndex is 1-based)
#
# Part 1 — Basic load balancing
# Route each CONNECT to the server with the fewest active connections. Break ties by choosing the smaller target index.
# Part 2 — Disconnections
# Handle DISCONNECT — remove that connection from its server, freeing up a slot. Future CONNECTs see updated load.
# Part 3 — Object ID affinity
# If an incoming CONNECT specifies an objectId that is currently active on a server, route it to that same server (regardless of load).
# If the objectId has no active connections, fall back to Part 1 load balancing.

# Part 1

def route_requests(numTargets, maxConnectionsPerTarget, requests):
    connection_count = [0] * numTargets
    conn_to_target = {}
    result = []

    for request in requests:
        parts = request.strip().split(",")
        action = parts[0]

        if action == "CONNECT":
            conn_id = parts[1]
            user_id = parts[2]

            # Pick server with fewest connections (tie → smaller index)
            best_idx = 0
            for i in range(numTargets):
                if connection_count[i] < connection_count[best_idx]:
                    best_idx = i
            target_idx = best_idx

            # Register connection
            connection_count[target_idx] += 1
            conn_to_target[conn_id] = target_idx

            # Log (1-based)
            result.append(f"{conn_id},{user_id},{target_idx + 1}")

    return result

# ── Test Cases ────────────────────────────────────────────────
print("=== Test 1: Two connections, two servers ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",
    "CONNECT,conn2,userB,obj2",
])
print("\n".join(result))
# conn1,userA,1
# conn2,userB,2

print("\n=== Test 2: Three connections, two servers (tie break) ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",
    "CONNECT,conn2,userB,obj2",
    "CONNECT,conn3,userC,obj3",
])
print("\n".join(result))
# conn1,userA,1  → server1=1, server2=0
# conn2,userB,2  → server1=1, server2=1
# conn3,userC,1  → tie → smaller index wins → server 1

print("\n=== Test 3: All to same server when only 1 target ===")
result = route_requests(1, 10, [
    "CONNECT,conn1,userA,obj1",
    "CONNECT,conn2,userB,obj2",
    "CONNECT,conn3,userC,obj3",
])
print("\n".join(result))
# conn1,userA,1
# conn2,userB,1
# conn3,userC,1

# Part 2 — Adding DISCONNECT
def route_requests(numTargets, maxConnectionsPerTarget, requests):

    # Track number of active connections per server (0-based index)
    connection_count = [0] * numTargets

    # Map connectionId → target index (0-based)
    # NEW: we need this to know WHICH server to decrement on disconnect
    conn_to_target = {}

    result = []

    for request in requests:
        parts = request.strip().split(",")
        action = parts[0]

        if action == "CONNECT":
            conn_id = parts[1]
            user_id = parts[2]

            # Pick server with fewest connections (tie → smaller index)
            target_idx = min(
                range(numTargets),
                key=lambda i: connection_count[i]
            )

            # Register connection
            connection_count[target_idx] += 1
            conn_to_target[conn_id] = target_idx  # NEW: remember which server

            # Log (1-based)
            result.append(f"{conn_id},{user_id},{target_idx + 1}")

        # NEW: handle disconnect
        elif action == "DISCONNECT":
            conn_id = parts[1]

            # Find which server this connection was on
            target_idx = conn_to_target.pop(conn_id)  # remove from map

            # Free up the slot on that server
            connection_count[target_idx] -= 1

    return result


# ── Test Cases ────────────────────────────────────────────────

print("=== Test 1: Basic disconnect frees up slot ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",    # server1=1, server2=0 → goes to server 1
    "DISCONNECT,conn1,userA,obj1", # server1=0, server2=0 → server 1 is free again
    "CONNECT,conn2,userB,obj2",    # tie → smaller index → server 1
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,1

print("\n=== Test 2: Disconnect mid-stream changes routing ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",    # server1=1, server2=0 → server 1
    "CONNECT,conn2,userB,obj2",    # server1=1, server2=1 → server 2 (tie → wait, server1=1 already so server2)
    "CONNECT,conn3,userC,obj3",    # server1=1, server2=1 → tie → server 1
    "DISCONNECT,conn1,userA,obj1", # server1=0, server2=1
    "CONNECT,conn4,userD,obj4",    # server1=0 < server2=1 → server 1
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,2
# conn3,userC,1
# conn4,userD,1

print("\n=== Test 3: Multiple disconnects ===")
result = route_requests(3, 10, [
    "CONNECT,conn1,userA,obj1",    # all zeroes → server 1
    "CONNECT,conn2,userB,obj2",    # server1=1 → server 2
    "CONNECT,conn3,userC,obj3",    # server1=1,server2=1 → server 3
    "DISCONNECT,conn2,userB,obj2", # server2 freed → server2=0
    "DISCONNECT,conn3,userC,obj3", # server3 freed → server3=0
    "CONNECT,conn4,userD,obj4",    # server1=1,server2=0,server3=0 → server 2 (tie→smaller)
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,2
# conn3,userC,3
# conn4,userD,2


# Part3
def route_requests(numTargets, maxConnectionsPerTarget, requests):

    # Track number of active connections per server (0-based)
    connection_count = [0] * numTargets

    # connectionId → target index (0-based)
    conn_to_target = {}

    # NEW: objectId → target index
    # only exists while at least one connection with that objectId is active
    object_to_target = {}

    # NEW: objectId → number of active connections using it
    # so we know when to clear object_to_target
    object_conn_count = {}

    result = []

    for request in requests:
        parts = request.strip().split(",")
        action = parts[0]

        if action == "CONNECT":
            conn_id   = parts[1]
            user_id   = parts[2]
            object_id = parts[3]

            # NEW Part 3: if objectId is active, use its server
            if object_id in object_to_target:
                target_idx = object_to_target[object_id]

            # Part 1/2: load balance normally
            else:
                target_idx = min(
                    range(numTargets),
                    key=lambda i: connection_count[i]
                )

            # Register connection
            connection_count[target_idx] += 1
            conn_to_target[conn_id] = target_idx

            # NEW: track object affinity
            object_to_target[object_id] = target_idx
            object_conn_count[object_id] = object_conn_count.get(object_id, 0) + 1

            result.append(f"{conn_id},{user_id},{target_idx + 1}")

        elif action == "DISCONNECT":
            conn_id   = parts[1]
            object_id = parts[3]  # NEW: need objectId to update affinity

            target_idx = conn_to_target.pop(conn_id)
            connection_count[target_idx] -= 1

            # NEW: decrement object connection count
            object_conn_count[object_id] -= 1

            # If no more active connections for this object → clear affinity
            if object_conn_count[object_id] == 0:
                del object_to_target[object_id]
                del object_conn_count[object_id]

    return result


# ── Test Cases ────────────────────────────────────────────────

print("=== Test 1: Same objectId → same server ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",
    "CONNECT,conn2,userB,obj1",  # obj1 active on server 1 → forced to server 1
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,1

print("\n=== Test 2: Affinity clears after all disconnect ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",    # server1=1, server2=0 → server 1
    "DISCONNECT,conn1,userA,obj1", # obj1 affinity cleared
    "CONNECT,conn2,userB,obj2",    # load balance → server 1 (tie)
    "CONNECT,conn3,userA,obj1",    # obj1 not active → load balance → server 2
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,1
# conn3,userA,2

print("\n=== Test 3: Affinity holds while ANY connection active ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",    # server 1
    "CONNECT,conn2,userB,obj1",    # obj1 active → server 1
    "DISCONNECT,conn1,userA,obj1", # obj1 still has conn2 → affinity stays
    "CONNECT,conn3,userC,obj1",    # obj1 still active → still server 1
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,1
# conn3,userC,1

print("\n=== Test 4: Different objects go to different servers ===")
result = route_requests(2, 10, [
    "CONNECT,conn1,userA,obj1",  # server 1
    "CONNECT,conn2,userB,obj2",  # obj2 not active → load balance → server 2
    "CONNECT,conn3,userC,obj1",  # obj1 active on server 1 → server 1
    "CONNECT,conn4,userD,obj2",  # obj2 active on server 2 → server 2
])
print("\n".join(result))
# Expected:
# conn1,userA,1
# conn2,userB,2
# conn3,userC,1
# conn4,userD,2