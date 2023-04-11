const breadthFirstPrint = (graph, source) => {
  const queue = [source];
  while (queue.length > 0) {
    const curr = queue.shift();
    console.log(curr);
    for (let neighbor of graph[curr]) {
      queue.push(neighbor);
    }
  }
}

// directed graph with no cycles
const graph = {
  a: ['b', 'c'],
  b: ['d'],
  c: ['e'],
  d: ['f'],
  e: [],
  f: []
}

breadthFirstPrint(graph, 'a'); // abcdef