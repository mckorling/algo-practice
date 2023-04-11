// undirected graph
// i <--> j, etc
const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n'],
  ['j', 'k'] // cycle
];

// traversals work better on adjacency list so we can convert it to a graph
const createAdjList = (edges) => {
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

const hasPathRecursive = (graph, src, dst, visited) => {
  if (src === dst) return true;
  if (visited.has(src)) return false;
  visited.add(src);
  for (let neighbor of graph[src]) {
    if (hasPathRecursive(graph, neighbor, dst, visited) === true) {
      return true;
    }
  }
  return false;
}

// problem: undirected path
const undirectedPath = (edges, nodeA, nodeB) => {
  const graph = createAdjList(edges);
  const visited = new Set();
  return hasPathRecursive(graph, nodeA, nodeB, visited);
}

console.log(undirectedPath(edges, 'i', 'm')); // true
console.log(undirectedPath(edges, 'o', 'k')); // false