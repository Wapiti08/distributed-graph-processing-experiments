import numba
from numba import njit, prange
import numpy as np
from collections import deque
import time
from numba.typed import List

# ============================================================================
# Parallel BFS with Numba
# ============================================================================

@njit(parallel=True)
def parallel_bfs_numba(adjacency_list, sources, num_threads=4):
    """
    Parallel BFS using numba's prange for parallelization
    adjacency_list: List of arrays representing graph structure
    sources: Array of starting nodes
        
    """
    n = len(adjacency_list)
    visited = np.zeros(n, dtype=np.int8)
    distances = np.full(n, -1, dtype=np.int32)

    # initialize sources
    for src in sources:
        visited[src] = 1
        distances[src] = 0
    
    current_level = sources.copy()
    level = 0

    
