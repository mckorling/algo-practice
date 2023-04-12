edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

const buildGraph = (edges) => {
  const graph = {};
  for (let edge of edges) {
    const [a, b] = edge;
    if (!(a in graph)) graph[a] = [];
    if (!(b in graph)) graph[b] = [];
    graph[a].push(b);
    graph[b].push(a);
  }
  return graph;
}

// count the number of edges to get from start to end (not the number of nodes!)
const shortestPath = (edges, start, end) => {
  const graph = buildGraph(edges);
  const visited = new Set([start]);
  // use bfs because once the end node is found, we auto know it's the shortest
  const queue = [[start, 0]];

  while (queue.length > 0) {
    const [currNode, count] = queue.shift();
    if (currNode === end) {
      return count;
    }
    for (let neighbor of graph[currNode]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push([neighbor, count + 1]);

      }
    }
  }
  return -1; // no path found
}

console.log(shortestPath(edges, 'w', 'z')) // 2