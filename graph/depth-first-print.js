const depthFirstPrint = (graph, source) => {
  // not accounting for cycles right now
  const stack = [source];
  while (stack.length > 0) {
    const curr = stack.pop();
    console.log(curr);
    for (let neighbor of graph[curr]) {
      stack.push(neighbor);
    }
  }
}

// recursion works of a stack, so this is a natural change to make
const dfsRecursive = (graph, source) => {
  console.log(source);
  for (let neighbor of graph[source]) {
    dfsRecursive(graph, neighbor)
  }
}

// directed graph with no cycles
// print methods above don't account for cycles
// and they don't account for separate nodes that aren't connected
const graph = {
  a: ['b', 'c'],
  b: ['d'],
  c: ['e'],
  d: ['f'],
  e: [],
  f: [],
}

// both print all elements in graph, but different orders
// recursive processes the 'b' immediately off the stack instead of pushing it, and then pushing 'c' on top of it
depthFirstPrint(graph, 'a'); // acebdf
dfsRecursive(graph, 'a'); // abdfce