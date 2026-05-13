# https://www.geeksforgeeks.org/problems/strongly-connected-component-tarjanss-algo-1587115621/1

# Time Complexity  : O(V + E) => Every node visited once O(v) , Every edge traversed once O(E)
# Space Complexity : O(V) disc ,low , inSt => stores of size V
class Solution:

    # Function to find all Strongly Connected Components using Tarjan's Algorithm
    def tarjans(self, V, adj):

        # Time Complexity : O(V + E)
        # Space Complexity: O(V)

        disc = [-1] * V
        low = [-1] * V

        inSt = [False] * V

        st = []

        timer = [0]

        allSCCs = []

        # DFS function
        def findSCC(u):

            # Assign discovery time and low value
            timer[0] += 1

            disc[u] = low[u] = timer[0]

            # Push into stack
            st.append(u)

            inSt[u] = True

            # Traverse neighbors
            for v in adj[u]:

                # Tree Edge
                if disc[v] == -1:

                    findSCC(v)

                    low[u] = min(low[u], low[v])

                # Back Edge
                elif inSt[v]:

                    low[u] = min(low[u], disc[v])

            # Head node of SCC
            if low[u] == disc[u]:

                scc = []

                while True:

                    x = st.pop()

                    inSt[x] = False

                    scc.append(x)

                    if x == u:
                        break

                scc.sort()

                allSCCs.append(scc)

        # Run DFS for all nodes
        for i in range(V):

            if disc[i] == -1:

                findSCC(i)

        # Lexicographical sorting
        allSCCs.sort()

        return allSCCs
