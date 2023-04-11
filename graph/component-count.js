// 3 components
// 3
// 4, 6, 5, 7, 8
// 1, 2
const graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}

// keys will be converted to strings
// need to make sure to convert to string
// otherwise the set will see 8 and '8' differently
const exploreGraph = (graph, node, visited) => {
  if (visited.has(String(node))) return false;
  
  visited.add(String(node));

  for (let neighbor of graph[node]) {
    exploreGraph(graph, neighbor, visited);
  }

  return true; // to hit here, then it has explored all of its neighbors
}

const countComponents = (graph) => {
  let count = 0;
  const visited = new Set();
  for (let node in graph) {
    // explore that node with dfs
    if (exploreGraph(graph, node, visited) === true) {
      count++;
    } 
  }
  return count;
}

console.log(countComponents(graph));