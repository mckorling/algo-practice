graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
};

const largestComponent = (graph) => {
  let largest = 0;
  const visited = new Set();

  // loop through nodes in graph
  for (let node in graph) {
    // check if the count is new max
    const currentCount = countNodes(graph, node, visited);
    largest = Math.max(largest, currentCount);
  }

  // return max
  return largest;
}

const countNodes = (graph, node, visited) => {
  // handle any cycles, or already counted nodes
  if (visited.has(String(node))) return 0;

  visited.add(String(node));
  // can start counting here bc it will return one on ln 34 and accumulate 
  let count = 1;
  for (let neighbor of graph[node]) {
    count += countNodes(graph, neighbor, visited);
  }
  return count;
}

console.log(largestComponent(graph));